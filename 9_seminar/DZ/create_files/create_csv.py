import csv
import random

def write_csv():
    name: str = "csv_data.csv"
    with open(name, "w", encoding="utf-8", newline="") as f:
        column = ["a","b","c"]
        csv_writer = csv.writer(f, dialect="excel")
        csv_writer.writerow(column)

        for i in range(1000):
            a = random.randint(-100,100)
            b = random.randint(-100,100)
            c = random.randint(-100,100)
            csv_writer.writerow([a,b,c])
            print([a,b,c])

