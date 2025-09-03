import random
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ`~1234567890!@#$%^&*()_+=-[]\|;:',./<>?/*"
length = int(input("enter the password length"))
password = ''

for a in range(length):
    password += ''.join(random.choices(char))
print(password)



# enter the password length8
# Ks:cr/8h