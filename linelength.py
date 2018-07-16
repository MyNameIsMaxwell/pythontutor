def distance(x1, y1, x2, y2):
    a=(x2-x1)+(y1-y1)
    b=(x2-x2)+(y2-y1)
    c=(a**2+b**2)**(1/2)
    return c
    
x1, y1 ,x2, y2=input().split()
x1,y1,x2,y2=[int(x1),int(y1),int(x2),int(y2)]
print(distance(x1,y1,x2,y2))