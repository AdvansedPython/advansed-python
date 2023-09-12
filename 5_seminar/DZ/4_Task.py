#  Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib_numbers(len_numbers):
    last_number = 1
    number = 1

    if last_number == number:
        yield number
        yield number
    for i in range(2, len_numbers):
        last_number, number = number, last_number + number 
        yield number

for i in fib_numbers(10):
    print(i, end=" ")