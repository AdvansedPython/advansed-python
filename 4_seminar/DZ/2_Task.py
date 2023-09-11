# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#  где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.


def create_dict(keys):
    global my_dict

    return {my_dict[key]:str(key) for key in keys}


my_dict = {"one":1,"two":2,"three":3}
print(create_dict(my_dict.keys()))