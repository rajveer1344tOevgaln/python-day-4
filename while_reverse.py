# for reversing.....

a = int(input("Enter st num :"))
b = int(input("Enter end num :"))
c = int(input("Enter diff :"))

num = a
while num >= b:
    cal = int(num/c)
    print(a,"X",cal,"=" ,num)
    num -= c
