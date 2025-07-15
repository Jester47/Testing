# 2
# Ввод параметров окружности
def parametrs():
    centre_x = int(input('Введите координату x: '))
    centre_y = int(input('Введите координату y: '))
    radius = int(input('Введите радиус окружности: '))
    centre_xy = [str(centre_x), '\t', str(centre_y), '\n', str(radius)]
    return centre_x, centre_y, radius, centre_xy


# Загрузка параметров окружности в файл
def write_parametrs():
    with open('circle.txt', 'w') as f:
        f.writelines(parametrs()[3])


# Загрузка точек в файл
def write_dot():
    count_points = int(input("Введите количество точек: "))
    open('dot.txt', 'w').close()
    for i in range(1, count_points + 1):
        with open('dot.txt', 'a') as f:
            point_x = int(input(f'Введите x{i} точку: '))
            point_y = int(input(f'Введите y{i} точку: '))
            point_xy = [str(point_x) + '\t', str(point_y) + '\n']
            f.writelines(point_xy)


# Чтение файла с параметрами окружности
def read_parametrs(circle_file):
    coordinates = []
    with open(circle_file, 'r') as f:
        for line in f:
            coordinates.append([int(i) for i in line.split()])
    coord_x, coord_y, rad = coordinates[0][0], coordinates[0][1], coordinates[1][0]
    return coord_x, coord_y, rad


# Чтение файла с точками
def read_dot(dot_file):
    points = []
    points_x = []
    points_y = []
    with open(dot_file, 'r') as file:
        for line in file:
            points.append([int(i) for i in line.split()])
    for i in range(len(points)):
        points_x.append(points[i][0])
        points_y.append(points[i][1])
    return points_x, points_y


# Проверка местоположения точек по теореме Пифагора
def check_location(points_x, points_y, coord_x, coord_y, rad):
    for i in range(len(points_x)):
        if (points_x[i] - coord_x) ** 2 + (points_y[i] - coord_y) ** 2 < rad ** 2:
            print(1)
        elif (points_x[i] - coord_x) ** 2 + (points_y[i] - coord_y) ** 2 > rad ** 2:
            print(2)
        else:
            print(0)


# Результат
write_parametrs()
write_dot()
points_x, points_y = read_dot('dot.txt')
coord_x, coord_y, rad = read_parametrs('circle.txt')
check_location(points_x, points_y, coord_x, coord_y, rad)
