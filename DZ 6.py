n = int(input("ENTER the number: "))

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10

print("sum of a number:", n + d1 + d2)