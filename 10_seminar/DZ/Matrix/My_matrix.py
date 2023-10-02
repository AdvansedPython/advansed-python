import random 


class Matrix:

    def __init__(self, len_one_element, len_matrix):
        self.my_matrix = self.create_matrix(len_one_element, len_matrix)


    def create_matrix(self, len_one_element, len_matrix):
        return [[random.randint(1,100) for j in range(len_one_element)] for i in range(len_matrix)]


    def overturn_matrix(self):
        result = []
        for i in range(len(self.my_matrix[0])):
            result.append([])
            for j in range(len(self.my_matrix)):
                result[i].append(self.my_matrix[j][i])

        self.my_matrix = result 


    def print_matrix(self):
        for i in self.my_matrix:
            for j in i:
                print(f"{j}\t", end="")
            print()



