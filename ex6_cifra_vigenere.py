# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# https://www.nostarch.com/crackingcodes (BSD Licensed)

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'we are discovered, save your self.'
    myKey = 'deceptive'
    myMode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.
    translated = translateMessage(myKey, myMessage, myMode)
    print("Clear text:\n", myMessage)
    print('%sed message:' % (myMode.title()))
    print(' ' + translated)


def translateMessage(key, message, mode):
    translated = []  # Stores the encrypted/decrypted message string.
    keyIndex = 0
    key = key.upper()
    for symbol in message.upper():  # Loop through each symbol in message.
        num = LETTERS.find(symbol)
        if num != -1:  # -1 means symbol.upper() was not found in LETTERS.
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex])  # Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])  # Subtract if decrypting.
            num %= len(LETTERS)  # Handle any wraparound.
            # Add the encrypted/decrypted symbol to the end of translated:
            translated.append(LETTERS[num].lower())
            keyIndex += 1  # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # Append the symbol without encrypting/decrypting.
            translated.append(symbol)
    return ''.join(translated)


# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()
