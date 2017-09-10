# Authors: Jayaprakash A
# Testers: 
# 

## Code that calculates the distance between two files 
## based on word frequency.

from __future__ import print_function
import math
import os

delimiters = "\'\"/<?>,.:*-+\\=`~!@#$%^&()_ ;"
document_word_count = {}


def remove_delimiters(text_line):

	""" Function name : remove_delimiters
	Input arguments :
		1. string : Piece of text
	Purpose : To remove unnecessary characters 
	Return Value : The string after removing characters.
    """
	for ch in delimiters:
		text_line = text_line.replace(ch, ";")
	
	return text_line

def format_text(text_line):
	""" Function name : format_text
	Input arguments :
		1. string : Piece of text
	Purpose : To format the text by removing delimiters and tariling whitespaces
	Return Value : The formatted string.
    """
	text_line = text_line.rstrip()
	text_line = remove_delimiters(text_line)

	return text_line.split(';')


def create_dictionary(file_path):
	""" Function name : create_dictionary
	Input arguments :
		1. string : The path to the file to be read.
		2. dictionary : To save the word frequency
	Purpose : To create the word frequency table/ vector 
    """
	my_dictionary ={}
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

	for key in my_dictionary.keys():
		if key != '' and key not in document_word_count:
			document_word_count[key] = 1
		elif key in document_word_count:
			document_word_count[key] += 1
		my_dictionary[key] /= (len(my_dictionary.keys()) * 1.0)

	return my_dictionary

def inner_product(document_one_dictionary, document_two_dictionary):
	""" Function name : inner_product
	Input arguments :
		1. dictionary : The dictionary corresponding to document one.
		2. dictionary : The dictionary corresponding to document two.
	Purpose : To find the inner product of two vectors
	Return Value : The inner product of two vectors 
    """
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
    

	folder_path = './testing/'

	document_dictionary = {}


	for filename in os.listdir(folder_path):
		document_dictionary[filename] = create_dictionary(folder_path + filename)


	print("Please input the two document files whose distance you wish to compute\n\n")

	print("Please have a look of documents present in the folder.\n\n")

	for filename in os.listdir(folder_path):
		print(filename, end = '\t')
	print()

	file_one_path = raw_input("Please input the first filename.\t")
	file_two_path = raw_input("Please input the second filename.\t")

	file_one_path

	document_one_dictionary = {}

	for key in document_dictionary[file_one_path].keys():

		idf_key = math.log(len(document_dictionary) / (document_word_count[key] * 1.0))
		tf_key = document_dictionary[file_one_path][key]

		document_one_dictionary[key] = tf_key * idf_key

	document_two_dictionary = {}

	for key in document_dictionary[file_two_path].keys():

		idf_key = math.log(len(document_dictionary) / (document_word_count[key] * 1.0))
		tf_key = document_dictionary[file_two_path][key]

		document_two_dictionary[key] = tf_key * idf_key


	for key in document_one_dictionary.keys():
		if (document_one_dictionary[key] != document_two_dictionary[key]):
			
			print(document_one_dictionary[key], end='  ')
			print(document_two_dictionary[key])

	print(cmp (document_one_dictionary, document_two_dictionary))

	result = calculate_distance(document_one_dictionary, document_two_dictionary)

	print("The distance between the files ", end='')
	print(file_one_path, end=' and ')
	print(file_two_path, end=' (in radians) is ')
	print(math.acos(result))
