a=input("Enter value :")
a=int(a)
for i in range(1,a,1):
    if a % i==0:
        print(i)
print(a)