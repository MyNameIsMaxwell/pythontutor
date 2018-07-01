s=input()
free=''
for i in range(len(s)):
    if i % 3 != 0:
        free+=s[i]
print(free)