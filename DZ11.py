s1 = "Python"
s2 = "Programming language"

raz = set(s1) - set(s2)

print(raz)

for i in raz:
    print(i, end =" ")