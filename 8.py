desk1_hor = int(input())
desk1_ver = int(input())
desk2_hor = int(input())
desk2_ver = int(input())
step_up=desk1_hor==desk2_hor+1 and desk1_ver==desk2_ver
step_down=desk1_hor==desk2_hor-1 and desk1_ver==desk2_ver
step_right=desk1_hor==desk2_hor and desk1_ver==desk2_ver+1
step_left=desk1_hor==desk2_hor and desk1_ver==desk2_ver-1
step_diag_up_left=desk1_hor==desk2_hor+1 and desk1_ver==desk2_ver-1
step_diag_up_right=desk1_hor==desk2_hor+1 and desk1_ver==desk2_ver+1
step_diag_down_left=desk1_hor==desk2_hor-1 and desk1_ver==desk2_ver-1
step_diag_down_right=desk1_hor==desk2_hor-1 and desk1_ver==desk2_ver+1
if step_up or step_down or step_right or step_left:
    print("YES")
elif step_diag_up_left or step_diag_up_right or step_diag_down_left or step_diag_down_right :
    print("Yes")
else:
    print("NO")