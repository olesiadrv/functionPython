def replace_numbers(x1, y1):
    if x1 != y1:
        x = (x1 + y1) / 2
        y = (y1 * x1) * 2
    else:
        x, y = 0, 0
    return x, y

number_x = float(input("Перше число: "))
number_y = float(input("Друге число: "))

result_x, result_y = replace_numbers(number_x, number_y)
print("Результат заміни чисел:")
print("Число X:", result_x)
print("Число Y:", result_y)
