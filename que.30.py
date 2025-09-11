x = int(input("Enter the number : "))# Number of terms you want

# First two Fibonacci numbers
a, b = 0, 1
count = 0

while count < x:
    print(a, end=" ")
    a, b = b, a + b   # a , b ki value lelega aur b me a+b add ho jayega 
    count += 1 # count ki value ko 1 -1 increase kerta rahega