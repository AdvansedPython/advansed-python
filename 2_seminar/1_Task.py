
number = int(input("Введите число для преобразования:\n"))
LETTERS = "a b c d e f g".split()
result = ""

print(f"\nБездушная машина => \t{hex(number)}")

while number > 0:
    remains = number % 16
    if remains > 9:
        result = str(LETTERS[remains % 10]) + result
    else:
        result = str(remains) + result
    number //= 16

print(f"Мой результат => \t{result}")