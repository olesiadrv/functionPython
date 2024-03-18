def count_negatives_numbers(a, b, c):
    count = 0
    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count

a = int(input("Ціле число a: "))
b = int(input("Ціле число b: "))
c = int(input("Ціле число c: "))

negatives_count = count_negatives_numbers(a, b, c)
print("Кількість негативних чисел:", negatives_count)