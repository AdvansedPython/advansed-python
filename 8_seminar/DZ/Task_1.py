# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней 
# с учётом всех вложенных файлов и директорий.


from convert import write_json
from convert import write_csv
from convert import write_pickle
import os, pprint

_all_data = []

def find_files(directory: str = os.getcwd()):
    global _all_data
    
    files_size = 0

    with os.scandir(directory) as dir:

        for entry in dir:
            one_data = []
            

            one_data.append(entry.name)
            one_data.append(directory)

            if entry.is_file():
                one_data.append("File")
                one_data.append(entry.stat().st_size)  

               
                files_size += entry.stat().st_size

            else:
                one_data.append("Not File")
               
                
                dir_size = find_files(f"{directory}/{entry.name}")
                files_size += dir_size + entry.stat().st_size
                one_data.append(dir_size)
                
            _all_data.append(one_data)

            one_data = []

        
    return files_size











find_files()

write_json(_all_data)
write_csv(_all_data)
write_pickle(_all_data)


