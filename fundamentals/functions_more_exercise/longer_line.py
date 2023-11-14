import math


def longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    side_a = x_1 - x_2
    side_b = y_1 - y_2
    side_c = x_3 - x_4
    side_d = y_3 - y_4
    line_1 = math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))
    line_2 = math.sqrt(math.pow(side_c, 2) + math.pow(side_d, 2))
    if line_1 > line_2:
        if (abs(x_1) + abs(y_1)) < (abs(x_2) + abs(y_2)):
            return f"({math.floor(x_1)}, {math.floor(y_1)})({math.floor(x_2)}, {math.floor(y_2)})"
        return f"({math.floor(x_2)}, {math.floor(y_2)})({math.floor(x_1)}, {math.floor(y_1)})"
    else:
        if (abs(x_3) + abs(y_3)) < (abs(x_4) + abs(y_4)):
            return f"({math.floor(x_3)}, {math.floor(y_3)})({math.floor(x_4)}, {math.floor(y_4)})"
        return f"({math.floor(x_4)}, {math.floor(y_4)})({math.floor(x_3)}, {math.floor(y_3)})"


point_1 = float(input())
point_2 = float(input())
point_3 = float(input())
point_4 = float(input())
point_5 = float(input())
point_6 = float(input())
point_7 = float(input())
point_8 = float(input())
result = longer_line(point_1, point_2, point_3, point_4, point_5, point_6, point_7, point_8)
print(result)


