plain_text = "Hello World"
cipher_text = ""
key = 0

for letter in plain_text:
    if letter.isalpha():
        val = ord(letter)
        val = val + key
        if letter.isupper():
            if val > ord('Z'):
                val -= 26
            elif val < ord('A'):
                val += 26
        elif letter.islower():
            if val > ord('z'):
                val -= 26
            elif val < ord('a'):
                val += 26
        new_letter = chr(val)
        cipher_text += new_letter
    else:
        cipher_text += letter
print(cipher_text)
