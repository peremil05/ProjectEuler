# Problem ID 2
a = 0
b = 1
fibSum = 0
while b < 4e6:
    if b % 2 == 0:
        fibSum += b
    b = b + a
    a = b - a

print(f"Answer: {fibSum}")
