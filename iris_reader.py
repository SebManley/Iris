import pandas as pd
import csv


def read_csv(csvfile):
    try:
        with open(csvfile, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',')

            list_csv_data = list(csvreader)

            result = pd.DataFrame(list(list_csv_data))

            return result

    except:
        print("An exception has occurred.")


print(read_csv("iris.csv"))
