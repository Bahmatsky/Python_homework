import random

x = [random.randint(0, 10) for i in range(10)]
print(x)
print("number 5 in the list ", x.index(5)+1)