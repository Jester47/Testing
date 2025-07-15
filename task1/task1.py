# 1
n = int(input(f"Максимальное число в массиве: "))
m = int(input(f"Интервал проверки массива: "))
size = int(input(f"Размер массива: "))

_list_ = list(range(1, n + 1))  # Повторяющийся интервал
new_list = []  # Наш массив
result_list = []  # Массив с результатами


# Создание кругового массива
def circular_list(size, new_list, _list_):
    while size != len(new_list):
        if size > len(new_list):
            new_list += _list_
        elif size < len(new_list):
            new_list.pop(-1)
    print(f'Наш массив: {new_list}')
    return new_list


new_list = circular_list(size, new_list, _list_)
result_list.append(new_list[0])


# Перебор и движение по массиву
def enumeration_list(result_list, m, new_list):
    for i in range(m - 1, 100000, m - 1):
        result_list.append(new_list[i])
        new_list += new_list
        print(result_list)
        if result_list[0] == result_list[-1]:
            result_list.pop(-1)
            break
    return result_list


print(f"Результат: {enumeration_list(result_list, m, new_list)}")
