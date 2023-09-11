# Напишите функцию для транспонирования матрицы
import random 

def create_matrix(len_one_element, len_matrix):
    return [[random.randint(1,100) for j in range(len_one_element)] for i in range(len_matrix)]


def overturn_matrix(my_matrix):
    result = []
    for i in range(len(my_matrix[0])):
        result.append([])
        for j in range(len(my_matrix)):
            result[i].append(my_matrix[j][i])

    return result 


def print_matrix(my_matrix):
    for i in my_matrix:
        for j in i:
            print(f"{j}\t", end="")
        print()


my_matrix = create_matrix(3,4)

print_matrix(my_matrix)
print()
print_matrix(overturn_matrix(my_matrix))


