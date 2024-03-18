def replace_numbers(a, b):
    if a != b:
        maximum = max(a, b)
        a = maximum
        b = maximum
    else:
        a = 0
        b = 0
    return a, b

a = int(input("Ціле число a: "))
b = int(input("Ціле число b: "))

a, b = replace_numbers(a, b)
print("Числа після заміни:", "число а - ", a, ", число b - ", b)