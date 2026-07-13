import random
import string 
password = ""

passwordChar = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


password =   "".join(random.choice(passwordChar)for char in range(10))

print(password)  