size = 7
word = '*'

def square(word, size):
	for i in range(size):
		print(' ' + ( word + ' ')*size)

	print('\n')


def triangle(word, size):
	for i in range(1,size+1):
		print(' '*len(word)*(size-i) + (str(word) + (' '*len(word)))*i)
	print('\n')



square(word, size)
triangle(word, size)