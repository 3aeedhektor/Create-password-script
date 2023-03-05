import random
import string

letters = string.ascii_letters
symbols = string.punctuation
digits = string.digits

alll = letters + symbols + digits

while True:
    inp = int(input("Enter length of password: "))
    password = "".join(random.sample(alll, inp))
    print(password)
    


