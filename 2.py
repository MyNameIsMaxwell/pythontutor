desk1_hor = int(input())
desk1_ver = int(input())
desk2_hor = int(input())
desk2_ver = int(input())

colorIsSame = ((desk1_hor+desk1_ver)%2) == ((desk2_hor+desk2_ver)%2)

if (colorIsSame):
    print("YES")
else:
    print("NO")
