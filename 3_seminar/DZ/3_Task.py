import string
my_str = "Python стал одним из самых популярных языков, он используется в анализе данных, машинном обучении, DevOps и веб-разработке, а также в других сферах, включая разработку игр. За счёт читабельности, простого синтаксиса и отсутствия необходимости в компиляции язык хорошо подходит для обучения программированию, позволяя концентрироваться на изучении алгоритмов, концептов и парадигм. Отладка же и экспериментирование в значительной степени облегчаются тем фактом, что язык является интерпретируемым"

my_str = my_str.translate(str.maketrans('','',string.punctuation)).lower().split()
set_str = set(my_str)

letters = dict()

for values in set_str:
    letters[values] = my_str.count(values)

#не ожидал что в list сконвертирует
letters = sorted(letters.items(), key=lambda item: item[1], reverse=True)
result = []

for i in range(10):
    print(letters[i])

