n=int(input())
m=int(input())
k=int(input())
S=n*m
if (S-k)/2>=S/2:
    print("No")
if (S-n>=k and S-m<k)or(S-m>=k and S-n<k)
else:
    print("Yes")