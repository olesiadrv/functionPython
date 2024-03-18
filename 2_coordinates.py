def finding_the_distance (x, y):
    return (x ** 2 + y ** 2) ** 0.5

x1 = float(input("Координата x для точки А: "))
y1 = float(input("Координата y для точки А: "))
x2 = float(input("Координата х для точки B: "))
y2 = float(input("Координата y для точки B: "))

distance_A = finding_the_distance(x1, y1)
distance_B = finding_the_distance(x2, y2)

if distance_A < distance_B:
    print("Точка A знаходиться ближче до початку координат")
elif distance_A > distance_B:
    print("Точка B знаходиться ближче до початку координат")
else:
    print("Точки А та B знаходяться на однаковій відстані від початку координат")
