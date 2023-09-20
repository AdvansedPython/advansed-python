# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. 
# При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. 
# Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени. 
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение. 

import os

def rename_files(file_name:str, numbers:list=0, appended:bool=False):
    i=0

    for *_, files in os.walk(os.getcwd()):

        for old_file_name in files:

            if not old_file_name.endswith(".txt"):
                continue

            old_only_name = old_file_name.split(".")[0]
            if appended:
                new_file_name = f"{old_only_name[int(numbers[0]):int(numbers[1])]}{file_name}{i}.txt"
            else:
                new_file_name = f"{file_name}{i}.txt"

            try:
                with (
                    open(old_file_name,"r", encoding = "utf-8") as f_read, 
                    open(new_file_name,"w", encoding = "utf-8") as f_write
                ):
                    f_write.writelines(list(f_read))
                
                os.remove(old_file_name)

                i+=1
            except:
                print("Что-то пошло не так")

# на семинаре os.walk находил только нужные файлы, а у меня находит кучу других, но мб это из-за убунты.
# в начале файлы текущей директории, потом кучу других вроде системных и говорит не могу открыть на чтение как с этим бороться?


rename_files("new", [1,3])

