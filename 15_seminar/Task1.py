from collections import namedtuple
import logging
import os



directory = os.getcwd()

logger = logging.getLogger(__name__)

logging.basicConfig(format = '{funcName}: name - {one_data.name}, \t expansion - .{one_data.expansion} \t type - {one_data.type}, \
                    \t weight - {one_data.weight}, \t path - {one_data.path}', filename="Logs", encoding='utf-8', style='{', 
                    level=logging.INFO
)



# _all_data = []

def find_files(directory: str):
    global _all_data
    
    files_size = 0

    with os.scandir(directory) as dir:

        for entry in dir:
            My_list = namedtuple('My_list', ['name', 'expansion', 'type', 'weight', 'path'])
            # one_data = []
            
            file = entry.name.split(".")
            name = file[0]
            path = directory
            expansion = '' 
            type = ''
            weight = ''
            path = ''

            if entry.is_file():
                if len(file) == 2:
                    expansion = file[1]
                else:
                    expansion = None


                type = "File"
                weight = entry.stat().st_size  

               
                files_size += entry.stat().st_size

            else:
                expansion = None
                type = "Not File"
               
                
                dir_size = find_files(f"{directory}/{entry.name}")
                files_size += dir_size + entry.stat().st_size
                weight = dir_size
            
            one_data = My_list(name, expansion, type, weight, path)
            
            print("1")
            print(one_data)
            # _all_data.append(one_data)
            logging.info(msg= one_data)

            # one_data = []

        
    return files_size


find_files(directory)