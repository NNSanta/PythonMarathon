def Convert (F):
    Celcius=(F-32)*5/9
    print(Celcius)
F=int(input("Enter a temperature in Farenheit "))
Convert (F)

def Convert (C):
    Fahrenheit = C*9/5 + 32
    print(Fahrenheit)
C=float(input("Enter a temperature in Celcius "))
Convert(C)