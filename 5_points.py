def point_position(x, y):
    if x == 0 and y == 0:
        return "Точка А знаходиться в початку координат"
    elif y == 0:
        return "Точка А лежить на осі X"
    elif x == 0:
        return "Точка А лежить на осі Y"
    elif x > 0 and y > 0:
        return "Точка А знаходиться в першому координатному куті"
    elif x < 0 and y > 0:
        return "Точка А знаходиться в другому координатному куті"
    elif x < 0 and y < 0:
        return "Точка А знаходиться в третьому координатному куті"
    else:
        return "Точка А знаходиться в четвертому координатному куті"

x_coordinate = float(input("Координата X точки А: "))
y_coordinate = float(input("Координата Y точки А: "))

position = point_position(x_coordinate, y_coordinate)
print(position)
