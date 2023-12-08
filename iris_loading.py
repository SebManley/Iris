import pyodbc
from iris_reader import *
# pd is a reference variable for pandas
import pandas as pd
from sqlalchemy import create_engine


# server = 'localhost,1433'
# database = 'Iris_project'
# username = 'SA'
# password = 'Password123!'
#
# docker_Iris = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
#                                   'SERVER='+server +
#                                   ';DATABASE='+database +
#                                   ';UID='+username +
#                                   ';PWD='+password)

username = 'SA'
password = 'Password123!'
host = 'localhost,1433'
database = 'Iris_project'

connection_string = f'mssql+pyodbc://{username}:{password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection_string)

contents = read_csv("iris.csv")

# cursor = docker_Iris.cursor()

contents.to_sql('table_name', con=engine, if_exists='replace', index=False)
