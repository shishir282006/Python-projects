# WPA to print all prime in a interval of 1 to 10
#  wap to convert decimal to binary ,decimal to hexadecimal 
# wap to find the LCM 
# wap to calculae the natural log of any number


'''
for num in range(1 , 11):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)



import math
x = int(input("Enter the number : "))
print(math.log(x)) '''

# Decmial to binary
Dec = int(input("Enter the number"))
bin = ''
while Dec > 0:
    bin = str(Dec % 2) + bin
print(bin)