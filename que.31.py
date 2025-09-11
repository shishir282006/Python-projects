x = int(input("Enter the terms : "))
a = 0
b = 1 
for i in range(x):
    print(a , end=" ")
    a,a=b, a+b 

# 0 1 2 3 4 5 6 7 8 9 output

\nx = int(input("Enter the terms : "))
a = 0
b = 1 
for i in range(x):
    print(a , end=" ")
    a,b=b, a+b

