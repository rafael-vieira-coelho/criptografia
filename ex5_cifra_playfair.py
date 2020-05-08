def create_alphabet():
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	LETTERS = list(alphabet)
	LETTERS.remove('j')
	LETTERS[LETTERS.index('i')] = 'ij'
	return (alphabet, LETTERS)
	
def remove_repetitions(key_with_repetitions, LETTERS, alphabet):
	key = []
	for i in range(len(key_with_repetitions) - 1, -1, -1):
		if key_with_repetitions[i] in alphabet:
			if key_with_repetitions[i] in ['i','j']:
				key_with_repetitions[i] = 'ij'
			if key_with_repetitions[i] not in key_with_repetitions[:i]:
				key.insert(0, key_with_repetitions[i])
				if (key_with_repetitions[i] in LETTERS):
					LETTERS.remove(key_with_repetitions[i])
	return key
		
def fill_key_matrix(key, LETTERS):
	matrix = [['']*5,['']*5,['']*5,['']*5,['']*5]
	print('Matrix Key:')
	count_letters = 0
	count_key = 0
	for i in range(5):
		for j in range(5):
			if count_key < len(key):
				matrix[i][j] = key[count_key]
				count_key += 1
			else:
				matrix[i][j] = LETTERS[count_letters]
				count_letters += 1
			print(matrix[i][j], ' ', end='')
		print('')
	return matrix
			
def get_clear_text(alphabet):
	text_with_special_caracters = list(input('What is the text? ').lower().strip())
	text = ''
	for letter in text_with_special_caracters:
		if letter in alphabet:
			text += letter
	return text
	
def arrange_pair_letters(text, alphabet):
	digraphs = []
	i = 0
	while i < len(text):
		if text[i] in alphabet:
			if (i + 1) >= len(text):
				digraphs.append((text[i], 'x'))	
				i += 1
			elif text[i] == text[i+1]:
				digraphs.append((text[i], 'x'))	
				i += 1
			else:
				digraphs.append((text[i], text[i+1]))
				i += 2
		else:
			i += 1	
	return digraphs
	
def are_on_same_line(a, b, m):
	for i in range(5):
		if a in m[i] and b in m[i]:
			return (True, m[i].index(a), m[i].index(b), i)
	return (False, -1, -1, -1)

def are_on_same_column(a, b, m):
	for i in range(5):
		first_in_column = False
		first_pos = -1
		second_in_column = False
		second_pos = -1
		for j in range(5):
			if (a in m[j][i]):
				first_in_column = True
				first_pos = j 
			if (b in m[j][i]):
				second_in_column = True
				second_pos = j
		if first_in_column and second_in_column:
			return (True, first_pos, second_pos, i)
	return (False, -1, -1, -1)

def get_letters_on_same_line(pos_a, pos_b, line, matrix):
	if pos_a + 1 == 5:
		first = matrix[line][0]
	else:	
		first = matrix[line][pos_a + 1]
	if pos_b + 1 == 5:
		second = matrix[line][0]
	else:	
		second = matrix[line][pos_b + 1]
	return (first, second)		

def get_letters_on_same_column(pos_a, pos_b, column, matrix):
	if pos_a + 1 == 5:
		first = matrix[0][column]
	else:	
		first = matrix[pos_a + 1][column]
	if pos_b + 1 == 5:
		second = matrix[0][column]
	else:	
		second = matrix[pos_b + 1][column]
	return (first, second)

def get_position(matrix, letter):
	for i in range(5):
		for j in range(5):	
			if letter == matrix[i][j]:
				return (i, j)
	return (-1, -1)			

def encrypt_text(text, matrix, digraphs):
	cipher_text = ''
	for digraph in digraphs:
		letter1 = digraph[0]
		letter2 = digraph[1]
		if letter1 in ['i','j']:
			letter1 = 'ij'
		if letter2 in ['i','j']:
			letter2 = 'ij'
		(same_line, pos_a, pos_b, line)  = are_on_same_line(letter1, letter2, matrix)
		if same_line:
			(new_letter1, new_letter2) = get_letters_on_same_line(pos_a, pos_b, line, matrix)
		else:
			(same_column, pos_a, pos_b, column) = are_on_same_column(letter1, letter2, matrix)
			if same_column:
				(new_letter1, new_letter2) = get_letters_on_same_column(pos_a, pos_b, column, matrix)
			else:
				(x_a, y_a) = get_position(matrix, letter1)
				(x_b, y_b) = get_position(matrix, letter2)
				new_letter1 = matrix[x_a][y_b]
				new_letter2 = matrix[x_b][y_a]			
		if new_letter1 == 'ij':
			new_letter1 = 'i'
		if new_letter2 == 'ij':
			new_letter2 = 'i'					
		print((letter1, letter2),'->', (new_letter1, new_letter2), 'line:', same_line, 'column:', same_column)
		cipher_text += new_letter1 + new_letter2
	return cipher_text

def main():
	(alphabet, LETTERS) = create_alphabet()
	key_with_repetitions = list(input('Which is the key password? ').lower().strip())
	key = remove_repetitions(key_with_repetitions, LETTERS, alphabet)
	print('key:\n', key)
	print('Alphabet:\n', LETTERS)
	matrix = fill_key_matrix(key, LETTERS)
	text = get_clear_text(alphabet)
	print('Clear Text:\n', text)
	digraphs = arrange_pair_letters(text, alphabet)	
	print('Pairs:\n', digraphs)
	cipher_text = encrypt_text(text, matrix, digraphs)
	print('Encrypted Text:',cipher_text)	

if __name__ == '__main__':
	main()
