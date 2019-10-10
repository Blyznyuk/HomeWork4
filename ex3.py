# Задание 3
# Напишите функцию, которая удаляет все небуквенные символы внутри строки (ограничимся латинским алфавитом).
# Проверьте, что вы правильно закодили с помощью инструкции assert.
import string


def stroka(*args):
    a = []
    z = str(args)
    for i in z:
        if i in string.ascii_letters:
            a.append(i)
    return ''.join(map(str, a))


# c = stroka(input("Vvedi stroky: "))
# assert len(c) is None
# print(c)

