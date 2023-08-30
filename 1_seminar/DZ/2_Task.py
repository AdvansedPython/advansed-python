def triangle_info():
    a, b, c = input("Введите a,b,c (длина сторон треугольника) через пробел: \n").split()
    a, b, c = int(a), int(b), int(c)
    result = 1
    triangle = ""

    # Проверка на существование и равнобедренность
    first, second, theard = a, b, c
    for i in range(3):
        if first + second < theard:
            result = 0
        if first == second != theard:
            triangle = "Треугольник равнобедренный"
        first, second, theard = second, theard, first 

    #Проверка на равносторонный и разносторонний треугольники
    if a == b ==c:
        triangle = "Треугольник равносторонний"
    elif a != b and a != c and b != c:
        triangle = "Треугольник разносторонний"

    if result:
        print(f"Треугольник существует \n{triangle}")
    else:
        print("Треугольник не существует" )

triangle_info()