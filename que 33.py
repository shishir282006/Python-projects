

# WAP for queue sum of first n natural number
for i in range(1,50):
    n = (i*(i+1)//2)
print(n)
# wap array ratation

# wap to add two matrix
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c)
# wap to sort word in alphabetic order
words = ["banana", "apple" , "elephant" , "moblie" , "book" , "pen" , "tushar"]
sort = sorted(words ,key = lambda w : ord(w[0]))
print(sort)

# wap to print pronic numnber between 1 to 100  
for i in range(1,101):
    n = i*(i+1)
    print(n , end= " , ")
# wap to cloning a list 
l = [1,2,3,4,5,6,7,8,9]
x = l.copy()
print(x)

# wap to find uncommon words from two string 
s1 = "hii I am Tushar"
s2 = "Hello hii I am Tushar"
set1 = set(s1.split())
set2 = set(s2.split())
uncommon = list(set1 ^ set2)
print(uncommon)


