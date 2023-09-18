# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, 
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, 
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди 
# них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from queen import check_queen
from queen import create_coordinates
from queen import print_desk


# coordinates = create_coordinates()
# coordinates = [[1,4],[2,7],[3,3],[4,8],[5,2],[6,5],[7,1],[8,6]] # Выведет True
# print_desk(coordinates)
# print(check_queen(coordinates))

i = 0
while i < 4:
    coordinates = create_coordinates()
    if check_queen(coordinates):
        print_desk(coordinates)
        i+=1