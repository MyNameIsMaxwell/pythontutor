x1=x1=int(input())
x2=int(input())
x3=int(input())
if x1==x2==x3:
    print ("3")
elif x1==x2 or x1==x3 or x2==x3:
    print("2")
else: print("0")