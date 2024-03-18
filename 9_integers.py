def count_integer_numbers(a, b, c):
    count = 0
    if a.is_integer():
        count += 1
    if b.is_integer():
        count += 1
    if c.is_integer():
        count += 1
    return count

a = float(input("Введіть число a: ").replace(',', '.'))
b = float(input("Введіть число b: ").replace(',', '.'))
c = float(input("Введіть число c: ").replace(',', '.'))

integer_count = count_integer_numbers(a, b, c)
print("Кількість цілих чисел серед введених: ", integer_count)
