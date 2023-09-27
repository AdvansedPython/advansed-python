from typing import Callable
import csv



def find_roots_from_csv(func: Callable):

    def wrapper(*args, **kwargs):
        result_list = {}
        with open("csv_data.csv", "r", encoding="utf-8") as f:
            csv_reader = csv.reader(f, dialect="excel")
            is_head = True
            for item in csv_reader:
                if is_head:
                    is_head = False
                    continue

                a, b, c = item
                result_list[",".join([a, b, c])] = func(int(a), int(b), int(c))
            return result_list

    return wrapper