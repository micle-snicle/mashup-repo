import random

length = int(input("How many characters should your password have? (at lest 10) "))

s = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","w","x","y","z"]
#s = ["abcdefghijklmnoprstuvwxyz"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
char = ["!","@","#","$","%","^","&","*"]
cap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","X","Y","Z"]

#password = ""

def paswgen():
    letters = "".join(random.choice(s) for a in range (length - 4))
    num = "".join(random.choice(numbers) for b in range (length - 9))
    ch = "".join(random.choice(char) for c in range (length - 10))
    c = "".join(random.choice(cap) for d in range (length - 10))
    password = letters + num + ch + c
    return password

password = paswgen()
password_mod = "".join(random.sample(password, len(password)))
print(password_mod)


