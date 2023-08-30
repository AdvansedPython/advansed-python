import fractions

# first_number = input("Введите первую дробь вида 1/2:\n").split("/")
# second_number = input("Введите вторую дробь вида 1/2:\n").split("/")
first_number = ("7","21")
second_number = ("4","2")
first_number = list(map(int, first_number))
second_number = list(map(int, second_number))
result = None

# Сложение дробей
if not first_number[1] % second_number[1]:
    denominator = first_number[1]
    numerator = second_number[0] * (first_number[1] // second_number[1]) + first_number[0]

elif not second_number[1] % first_number[1]:
    denominator = second_number[1] 
    numerator = first_number[0] * (second_number[1] // first_number[1]) + second_number[0]
else:
    denominator = first_number[1] * second_number[1] 
    numerator = first_number[0] * second_number[1] + second_number[0] * first_number[1]



result = f"{numerator}/{denominator}"if numerator % denominator else int(numerator/denominator)
print(f"\nМой результат(+) => \t{result}")


# Умножение дробей
numerator = first_number[0] * second_number[0]
denominator = first_number[1] * second_number[1]

result = f"{numerator}/{denominator}"if numerator % denominator else int(numerator/denominator)
print(f"Мой результат(*) => \t{result}")




# Проверка с помощью fractions
first_number = fractions.Fraction(first_number[0], first_number[1])
second_number = fractions.Fraction(second_number[0], second_number[1])

print(f"\nБездушная машина(+) => \t{first_number + second_number}")
print(f"Бездушная машина(*) => \t{first_number * second_number}")