def evaluation_to_a_degree(x):
    if x >= 0:
        return x ** 2
    else:
        return x ** 4

number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
number3 = float(input("Введіть третє число: "))

result1 = evaluation_to_a_degree(number1)
result2 = evaluation_to_a_degree(number2)
result3 = evaluation_to_a_degree(number3)

print("Результати піднечення чисел до другого та четвертого степенів:")
print("Перше число:", result1)
print("Друге число:", result2)
print("Третє число:", result3)