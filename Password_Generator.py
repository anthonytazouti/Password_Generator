import random
import string

def password(length):
    rand_char = string.punctuation
    digi = string.digits
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) + "".join(random.choice(digi)) + ''.join(random.choice(rand_char))for i in range(length))
    print("Your random password is:", result_str)


password(6)
print("*" * 55)
password(5)
print("*" * 55)
password(4)
print("*" * 55)
password(3)
print("*" * 55)
