import csv

def write_csv(data: list = [], name: str = "csv_data.csv"):
    with open(name, "w", encoding="utf-8") as f:
        column = ["Directory name","Parent","Type", "size"]
        csv_writer = csv.writer(f, dialect="excel")
        csv_writer.writerow(column)

        for item in data:
            csv_writer.writerow(item)

