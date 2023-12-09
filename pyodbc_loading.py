from Iris_functions import *

table = "Iris_2"

iris_connect()

writing_to_sql("iris.csv", table)

extract_sql_to_txt(table, (f"SELECT variety, ROUND(AVG(sepal_length), 2), ROUND(AVG(sepal_width), 2), "
                           f"ROUND(AVG(petal_length), 2), "f"ROUND(AVG(petal_width), 2) FROM {table} GROUP BY variety;")
                        , "plant_variety_properties.txt")
