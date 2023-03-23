# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


def input_num(message: str) -> int:
    input_error: bool = True
    while input_error:
        try:
            temp = int(input(message))
        except ValueError:
            print("Вы ввели не число!")
        else:
            input_error = False
            return temp


def input_list(size_l: int) -> list:
    s = []
    for i in range(size_l):
        s.append(input_num(f'input {i + 1} element: '))
    return s


n_size = input_num('Please input size n list: ')
n = input_list(n_size)
m_size = input_num('Please input size m list: ')
m = input_list(m_size)

print(f'finally sets: {set(n)}, {set(m)}\nUnion is {(sorted(list(set(n) & set(m))))}')
