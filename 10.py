desk1_hor = int(input())
desk1_ver = int(input())
desk2_hor = int(input())
desk2_ver = int(input())
if (desk1_hor==desk2_hor+1 and desk1_ver==desk2_ver+2)or(desk1_hor==desk2_hor-1 and desk1_ver==desk2_ver+2):
    print("Yes")
elif (desk1_hor==desk2_hor+2 and desk1_ver==desk2_ver+1)or(desk1_hor==desk2_hor+2 and desk1_ver==desk2_ver-1):
    print("Yes")
elif (desk1_hor==desk2_hor-2 and desk1_ver==desk2_ver+1)or(desk1_hor==desk2_hor-2 and desk1_ver==desk2_ver-1):
    print("Yes")
elif  (desk1_hor==desk2_hor+1 and desk1_ver==desk2_ver-2)or(desk1_hor==desk2_hor-1 and desk1_ver==desk2_ver-2):
    print("Yes")
else:
    print("NET")