from Iris_functions import *
from sqlalchemy import create_engine


username = 'SA'
password = 'Password123!'
host = 'localhost,1433'
database = 'Iris_project'

connection_string = f'mssql+pyodbc://{username}:{password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection_string)

contents = read_csv("iris.csv")

contents.to_sql('table_name', con=engine, if_exists='replace', index=False)
