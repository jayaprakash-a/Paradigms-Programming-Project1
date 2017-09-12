# Authors: Jayaprakash A
# Testers: 
# 

## Code that calculates the distance between two files 
## based on word frequency.


"""@package docstring
Documentation for this module."""
from __future__ import print_function
import math
import os
import operator

# @param delimiter character to differentiate words
delimiters = "\'\"/<?>,.:*-+\\=`~!@#^&()_ ;"


# Dictionary that contains words present in all the files of the folder.
document_word_count = {}


def remove_delimiters(text_line):

	""" Function name : remove_delimiters
	Input arguments :
		1. string text_line : Piece of text
	Purpose : To remove unnecessary characters 
	Return Value : The string after removing characters.
    """
	for ch in delimiters:
		text_line = text_line.replace(ch, ";")
	
	return text_line

def format_text(text_line):
	""" Function name : format_text
	Input arguments :
		1. string text_line : Piece of text
	Purpose : To format the text by removing delimiters and trailing whitespaces
	Return Value : The formatted string.
    """
	text_line = text_line.rstrip()
	text_line = remove_delimiters(text_line)

	return text_line.split(';')


def create_dictionary(file_path):
	""" Function name : create_dictionary
	Input arguments :
		1. string file_path : The path to the file to be read.
	Purpose : To create the word frequency table/ vector
	Return Value : The dictionary containing the word frequenct vector 
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
		1. dictionary document_one_dictionary : The dictionary corresponding to document one.
		2. dictionary document_two_dictionary : The dictionary corresponding to document two.
	Purpose : To find the inner product of two vectors
	Return Value : The inner product of two vectors 
    """
	sum = 0
	
	for key in document_one_dictionary.keys():
		if key in document_two_dictionary.keys():
			sum += document_one_dictionary[key] * document_two_dictionary[key]
	
	return sum

def calculate_distance(document_one_dictionary, document_two_dictionary):
	""" Function name : inner_product
	Input arguments :
		1. dictionary document_one_dictionary: The dictionary corresponding to document one.
		2. dictionary document_two_dictionary: The dictionary corresponding to document two.
	Purpose : To find the distance between two documents
	Return Value : The cosine distance of two vectors 
    """

	dot_product = inner_product(document_one_dictionary, document_two_dictionary)
	document_one_norm = inner_product(document_one_dictionary, document_one_dictionary)
	document_two_norm = inner_product(document_two_dictionary, document_two_dictionary)

	return dot_product / ((document_one_norm * document_two_norm) ** (1/2.0))

def text_formatting(my_dictionary):
	""" Function name : inner_product
	Input arguments :
		1. dictionary my_dictionary : The dictionary to be formatted
	Purpose : To remove the words which have very less importance to the meaning.
	Return Value : The modified dictionary. 
    """
	word_file = open('useless_words.txt', 'r')
	for word in word_file:
		word = word.rstrip()
		if word in my_dictionary:
			my_dictionary[word] = 0

	word_file.close()

	return my_dictionary

def ensure_dir(file_path):
""" Function name : inner_product
	Input arguments :
		1. string file_path : The path of the folder.
	Purpose : To create a directory if it does not exists.
    """
	if not os.path.exists(file_path):
		os.mkdir(file_path)

if __name__ == "__main__":
	

	folder_path = raw_input("Please input the path to the folder")
	document_dictionary = {}
	output_folder_path = raw_input("Please input the path to the output folder")

	ensure_dir(output_folder_path)
	
	result_dictionary = {}

	for filename in os.listdir(folder_path):
		document_dictionary[filename] = create_dictionary(folder_path + filename)


	for file_index_one in os.listdir(folder_path):
		for file_index_two in os.listdir(folder_path):

			document_one_dictionary = {}

			for key in document_dictionary[file_index_one].keys():

				idf_key = math.log(len(document_dictionary) / (document_word_count[key] * 1.0))
				tf_key = document_dictionary[file_index_one][key]

				document_one_dictionary[key] = tf_key * idf_key

			document_two_dictionary = {}

			for key in document_dictionary[file_index_two].keys():

				idf_key = math.log(len(document_dictionary) / (document_word_count[key] * 1.0))
				tf_key = document_dictionary[file_index_two][key]

				document_two_dictionary[key] = tf_key * idf_key


			result = calculate_distance(document_one_dictionary, document_two_dictionary)
			
			print(file_index_one, end =' ')
			print(file_index_two)

			result_dictionary[(file_index_one, file_index_two)] = math.acos(result)

	sorted_result = sorted(result_dictionary.items(), key=operator.itemgetter(1))
	os.chdir(output_folder_path)

	print("The calculation of distances has finished successfully!!!")
	result_file_name = raw_input("Please enter the name of file where you wish to save the result.")
	result_file = open(result_file_name ,'w')
	for item in sorted_result:
		print(item[0][0], end=' ',file=result_file)
		print(item[0][1], end=' ',file=result_file)
		print(item[1], end='\n',file=result_file)
	result_file.close()