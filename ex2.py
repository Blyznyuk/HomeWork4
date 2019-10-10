# Задание 2
# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов. Учитываем, что может быть повторяющиеся значения аргументов.


def func(*args):
    a = list(args)
    out = []  # список
    a.sort()
    for i in range(1, len(a)):  # добавим в список значения
        if a[i] > a[i - 1]:
            out.append(a[i])
    out.sort()
    return out[0]


c = func(25,2,3,31,6,5,5,88,55,88,54,5654,32,84,321)
print(c)
