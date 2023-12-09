# pd is a reference variable for pandas
import pandas as pd
import csv
import pyodbc


def iris_connect():
    server = 'localhost,1433'
    database = 'Iris_project'
    username = 'SA'
    password = 'Password123!'

    docker_Iris = ('DRIVER={ODBC Driver 17 for SQL Server};'
                   'SERVER=' + server +
                   ';DATABASE=' + database +
                   ';UID=' + username +
                   ';PWD=' + password)

    connection = pyodbc.connect(docker_Iris)
    cursor = connection.cursor()

    # Using two return statements will make the second unreachable
    return connection, cursor


# Function reads a csv file and formats it into a pandas dataframe
def read_csv(csvfile):
    try:
        with open(csvfile, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            list_csv_data = list(csvreader)

            result = pd.DataFrame(list(list_csv_data))

            return result

    except FileNotFoundError:
        print("An exception has occurred.")
    finally:
        csvfile.close()


# Function returns the header of each column so they can be easily referenced in the execute command
def return_header(df):
    data = read_csv(df)

    col_dict = {}
    pro_header = []
    x = 1

    # iloc is a pandas method for integer-location based indexing
    # Used to select rows and columns based on an index
    headers = data.iloc[0].tolist()

    # Converts . in column header name to SQL syntax (_)
    for p in headers:
        modified_p = p.replace(".", "_")
        pro_header.append(modified_p)

    for i in pro_header:
        col_dict[f"col{x}"] = i
        x += 1
    return col_dict


# Function writes the specified file converted to a pandas dataframe to sql server
def writing_to_sql(file, table):
    data = read_csv(file)
    # connection and cursor variables are assigned from the return in iris_connect function - otherwise they would
    # be unreferenced variables
    connection, cursor = iris_connect()
    header = return_header(file)
    table_name = table

    # Creates a SQL table within the database using the column names extracted in the return_header function
    cursor.execute(f"DROP TABLE IF EXISTS {table_name};"
                   f"CREATE TABLE {table_name} ({header["col1"]} FLOAT, {header["col2"]} FLOAT, {header["col3"]} FLOAT, {header["col4"]} FLOAT, {header["col5"]} VARCHAR(20));")

    # For loop iterates through the rows of the dataframe beginning after the header row
    # Each column in the row is assigned to a value variable for later insertion into the sql db
    for index, row in data.iloc[1:].iterrows():
        val1 = row.iloc[0]
        val2 = row.iloc[1]
        val3 = row.iloc[2]
        val4 = row.iloc[3]
        val5 = row.iloc[4]

        # Using ? creates a parameterized query - the values can then be passed on execution
        query = f"INSERT INTO {table_name} ({header['col1']}, {header['col2']}, {header['col3']}, {header['col4']}, {header['col5']}) VALUES (?, ?, ?, ?, ?)"

        cursor.execute(query, val1, val2, val3, val4, val5)

    connection.commit()
    cursor.close()
    connection.close()

