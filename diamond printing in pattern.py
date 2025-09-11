star = "*"
space = " "
s = 3
p = 2
print(space*4+star)
for i in range(4):
    print(space*s+star+space*p+star)
    s -= 2
    p += 3
s += 1
p -= 2
for j in range(4):
    print(space*s+star+space*p+star)
    s += 1
    p -= 2
print(space*5+star)

rows = 5
for i in range(rows):
    for j in range(rows):
        if j == 0 or j == rows - 1 or i == rows // 2:
            print("*" , end ="")
        else:
            print(" " , end = "")
    print()
