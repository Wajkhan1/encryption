import string
import random
chars = " "+string.punctuation+string.digits+string.ascii_letters
chars= list(chars)
key=chars.copy()
random.shuffle(key)
#print(f"this is the key for encryption: {key}")
#print(f"these are the original letters: {chars}")
#encrytion
original=input("enter the text to be encrypted: ")
cipher= " "
for i in original:
    index=chars.index(i)
    cipher += key[index]
#print(f"this is the original text: {original}")
#print(f"this is the encrypted text: {cipher}")
#decrypt
cipher=input("enter the text to be encrypted: ")
original= " "
for i in cipher:
    index=key.index(i)
    original += chars[index]
print(f"this is the encrypted text: {cipher}")
print(f"this is the original text: {original}")
