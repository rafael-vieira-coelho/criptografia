# this is a morsecode encoder based on the
# international morsecode, spaces are not
# converted, nor the special symbols. 

import time

def beep(tipo):
	print(tipo, end='')
	if tipo == '.':
		print('\a', end='')
		time.sleep(0.2)
	else:
		print('\a\a', end='')
		time.sleep(3)

# morsecode table, index of the letter plus
# one will be the morsecode for the letter.
code = {
    'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 
    'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 
    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..', '1': '.-', '2': '..-',
    '3': '...-', '4': '....-', '5': '.....', '6': '-....',
    '7': '-...', '8': '-..', '9': '-.', '0': '-',
    '.': '.-.-.-', ',': '--..--', ':': '---...',
    '-': '-....-', '/': '-..-', '(': '-.--.-',
    '[': '-.--.-', ']': '-.--.-', ')': '-.--.-',
    '=': '-...-', '?': '..--..', ' ':'' }

# get input from the user and convert it to
# lower case, so it's not case sensitive.
string = input().upper()

# iterate through user's input and convert 
# valid symbol into morsecode, then print 
# it; else just print the symbol if it's 
# invalid. 
for letter in string:
	if letter in code:
		print(letter, " = ", end='')		
		for codigo in code[letter]:
			beep(codigo)
		print('\n')
	else:
		print(letter)


