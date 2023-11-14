import math


def center_point(side_x1, side_y1, side_x2, side_y2):
    point_1 = math.sqrt(math.pow(side_x1, 2) + math.pow(side_y1, 2))
    point_2 = math.sqrt(math.pow(side_x2, 2) + math.pow(side_y2, 2))
    if point_1 > point_2:
        return int(side_x2), int(side_y2)
    elif point_1 < point_2:
        return int(side_x1), int(side_y1)
    elif point_1 == point_2:
        return int(side_x2), int(side_y2)


number_1 = math.floor(float(input()))
number_2 = math.floor(float(input()))
number_3 = math.floor(float(input()))
number_4 = math.floor(float(input()))

result = center_point(number_1, number_2, number_3, number_4)
print(result)


