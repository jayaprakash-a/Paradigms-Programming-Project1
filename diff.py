# Authors:
# Testers:
# Coding standards

delimiters = "\'\"/<?>,.:*-+\\=`~!@#$%^&()_ ;"

def remove_delimiters(text_line):

	for ch in delimiters:
		text_line = text_line.replace(ch, ";")
	
	return text_line

def format_text(text_line):
	
	text_line = text_line.rstrip()
	text_line = remove_delimiters(text_line)

	return text_line.split(';')


def create_dictionary(file_path, my_dictionary):
	
	text_document = open(file_path, 'r')
	
	for text_line in text_document: 
		text_line_buffer = format_text(text_line)
	
		for word in text_line_buffer:
			word = word.lower()
	
			if word != '' and word not in my_dictionary:
				my_dictionary[word] = 1
			elif word in my_dictionary:
				my_dictionary[word] += 1
	
	text_document.close()
	# print my_dictionary

def inner_product(document_one_dictionary, document_two_dictionary):
	
	sum = 0
	
	for key in document_one_dictionary.keys():
		if key in document_two_dictionary.keys():
			sum += document_one_dictionary[key] * document_two_dictionary[key]
	
	return sum

def calculate_distance(document_one_dictionary, document_two_dictionary):

	dot_product = inner_product(document_one_dictionary, document_two_dictionary)
	document_one_norm = inner_product(document_one_dictionary, document_one_dictionary)
	document_two_norm = inner_product(document_two_dictionary, document_two_dictionary)

	return dot_product / ((document_one_norm * document_two_norm) ** (1/2.0))

def text_formatting(my_dictionary):

	word_file = open('useless_words.txt', 'r')
	for word in word_file:
		word = word.rstrip()
		if word in my_dictionary:
			my_dictionary[word] = 0

	word_file.close()

	return my_dictionary

if __name__ == "__main__":
    document_one = "temp.txt"
    document_one_dictionary = {}
    create_dictionary(document_one, document_one_dictionary)

    document_two = "temp2.txt"
    document_two_dictionary = {}
    create_dictionary(document_two, document_two_dictionary)

    document_one_dictionary =  text_formatting(document_one_dictionary)
    document_two_dictionary =  text_formatting(document_two_dictionary)


    result = calculate_distance(document_one_dictionary, document_two_dictionary)

    print result