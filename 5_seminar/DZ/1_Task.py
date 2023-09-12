# Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


def is_prime(number):

    for i in range(2, int(number * 0.5) + 1):
        if number % i == 0:
            return False       
    return True

    
def create_prime_numbers(count_prime):
    number = 2
    count_numbers = 0
    # for i in range(count_prime):
    while count_numbers < count_prime:
        if is_prime(number): 
            count_numbers += 1           
            yield number
        number += 1

for i in create_prime_numbers(20):
    print(i)