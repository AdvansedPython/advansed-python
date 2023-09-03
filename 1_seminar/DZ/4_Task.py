import random

number = random.randint(0, 1000)
user_number = None

i = 0
while i<10:
    user_number = int(input("Введите число:\n"))
    if number == user_number: 
        print("Вы угадали!")
        break

    if user_number > number:
        print("Число меньше")
    else:
        print("Число больше")
    i+=1
else:
    print("Вы проиграли(")

    