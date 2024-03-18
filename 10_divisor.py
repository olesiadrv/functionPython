def find_divisors(a, b, c, k):
    divisors = []
    if a % k == 0:
        divisors.append(a)
    if b % k == 0:
        divisors.append(b)
    if c % k == 0:
        divisors.append(c)
    return divisors

a = int(input("Ціле число a: "))
b = int(input("Ціле число b: "))
c = int(input("Ціле число c: "))
k = int(input("Ціле число k: "))

divisors = find_divisors(a, b, c, k)
print("Числа, для яких число", k, "є дільником:", divisors)