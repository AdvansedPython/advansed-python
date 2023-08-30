number = None
START_POSITION = 2

while True:
    number = input("Введите число: ")
    if number.isdigit() and int(number)>0 and int(number)<=100_000:
        break
    print("Плохое число")

number = int(number)
i = START_POSITION
while i < number:
    if number % i == 0:
        print("Число составное")
        break
    i+=1
else:
    print("Число простое")
