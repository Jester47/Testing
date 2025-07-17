# 4
import sys

number_file = sys.argv[1]

# Чтение файла
def read_file():
    array = []
    arr = []
    with open(number_file, 'r') as f:
        for line in f:
            array.append([int(i) for i in line.split()])
    for i in range(len(array)):
        arr.append(array[i][0])
    return arr


# Среднее значение в массиве
def average_item():
    my_list = read_file()
    mean = sum(my_list) / len(my_list)
    distance_list = [abs(mean - num) for num in my_list]
    return my_list[distance_list.index(min(distance_list))]


# Нахождение минимального количества шагов
def step():
    step_max = 0  # Шаги от максимального числа
    step_min = 0  # Шаги от минимального числа

    # Читаем файл
    my_list = read_file()  #
    print(f'Наш массив: {my_list}')

    average = average_item()
    print(f'Среднее: {average}')

    # Нахождение шагов от максимума
    for i in range(0, 100000):
        if max(my_list) != average:
            my_list[my_list.index(max(my_list))] = max(my_list) - 1
        else:
            step_max = i
            break

    # Нахождение шагов от минимума
    for k in range(0, 100000):
        if min(my_list) != average:
            my_list[my_list.index(min(my_list))] = min(my_list) + 1
        else:
            step_min = k
            break
    return print(f'Получившийся массив: {my_list} и Количество шагов: {step_max + step_min}')


# Результаты
step()  # Чтение и вывод
