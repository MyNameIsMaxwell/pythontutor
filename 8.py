desk1_hor = int(input())
desk1_ver = int(input())
desk2_hor = int(input())
desk2_ver = int(input())
b=desk1_ver==desk2_ver
a=desk1_hor==desk2_hor
if (a+1 and b) or (a-1 and b):
    print("YES")
elif (a and b+1) or (a and b-1):
    print("YES")
elif (a+1 and b+1)or(a-1 and b-1):
    print("Yes")
elif (a-1 and b+1)or(a+1 and b-1):
    print("Yes")
else:
    print("NO") #да епт