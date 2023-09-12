#  Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def decode_file_path(file_path: str) -> tuple:
    *_, file_name = file_path.split("/")
    # *_, file_name = file_path.split("\\") - не понимаю почему в пути с обратным слешом в выводе он заменяет на
    return (file_path.replace(file_name,""), file_name, file_name.split(".")[-1])


print(decode_file_path("d:/qwer/zxbvb/sf/kabc.py"))
# print(decode_file_path("d:\qwer\zxbvb\sf\kabc.py"))