import random
import string

val=string.ascii_letters + string.digits + string.punctuation
password=""
len_password=int(input("enter the length of the password: "))
for i in range(len_password):
    password+=random.choice(val)
print(password)
