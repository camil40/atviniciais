x = int(input("entre com o numero: "))
s = 0
import random
for i in range(x):
    r = random.randint(0, 10)
    s = s + r
    print(r)

print(s)