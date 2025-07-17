# 2
import sys

circle_file = sys.argv[1]
dot_file = sys.argv[2]

# Чтение файла с параметрами окружности
def read_parametrs():
    coordinates = []
    with open(circle_file, 'r') as f:
        for line in f:
            coordinates.append([int(i) for i in line.split()])
    coord_x, coord_y, rad = coordinates[0][0], coordinates[0][1], coordinates[1][0]
    return coord_x, coord_y, rad


# Чтение файла с точками
def read_dot():
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
points_x, points_y = read_dot()
coord_x, coord_y, rad = read_parametrs()
check_location(points_x, points_y, coord_x, coord_y, rad)
