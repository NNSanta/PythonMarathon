n = 0
for i in range(1000, 2300, 1):
    if ((i % 5 == 0) and (i % 7 == 0)):
        n = n + i
        print(n)
