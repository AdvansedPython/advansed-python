from create_files import write_json
from typing import Callable

def create_json(func: Callable):

    def wrapper():

        write_json(func())

    return wrapper
