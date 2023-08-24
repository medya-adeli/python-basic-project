import random
import string
import time

# Get the current time as a string
current_time = str(float(time.time()))

# Combine time with other characters in the `chars` variable
chars = string.punctuation + string.digits + string.ascii_letters + current_time 

chars = list(chars)
key = chars.copy()

random.shuffle(key)

while True:
    plain_text = input("Enter the text: ")
    if plain_text.upper() == "TAMAM":
        break
    else:
        cipher_text = ""

        for letter in plain_text:
            index = chars.index(letter)
            cipher_text += key[index]

        int("-------------------------------------")
        int(f"Original message: {plain_text}")
        int("-------------------------------------")
        int(f"Encrypted message: {cipher_text}")
        int("-------------------------------------")
