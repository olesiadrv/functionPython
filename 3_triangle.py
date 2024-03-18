def checking_angles(a, b):
    c = 180 - a - b
    if c > 0 and a > 0 and b > 0: 
        return True, "Трикутник з такими кутами існує", c
    elif a == 0 or b == 0 or c == 0:
        return False, "Трикутник з кутом 0 не існує", None
    else:
        return False, "Трикутник з такими кутами не існує", None

def checking_right_angles(a, b, c):
    if a == 90 or b == 90 or c == 90:
        return True, "Трикутник прямокутний"
    else:
        return False, "Трикутник не прямокутний"


angle1 = float(input("Перший кут трикутника: "))
angle2 = float(input("Другий кут трикутника: "))


exists, msg, angle3 = checking_angles(angle1, angle2)
print(msg)

if exists:
    right, msg = checking_right_angles(angle1, angle2, angle3)
    print(msg)
