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
import time
import dict_functions
# @param delimiter character to differentiate words
delimiters = "\'\"/<?>,.:*-+\\=`~!@#^&()_ ;{}[]|"


# Dictionary that contains words present in all the files of the folder.
document_word_count = {}



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


def ensure_dir(file_path):
	""" Function name : inner_product
	Input arguments :
		1. string file_path : The path of the folder.
	Purpose : To create a directory if it does not exists."""

	if not os.path.exists(file_path):
		os.mkdir(file_path)

if __name__ == "__main__":
	
	start = time.clock()

	folder_path = raw_input("Please input the path to the folder\t")
	document_dictionary = {}
	output_folder_path = raw_input("Please input the path to the output folder\t")

	ensure_dir(output_folder_path)
	
	result_dictionary = {}
	temp={}

	for filename in os.listdir(folder_path):# Create the word vector for each and every file in the folder
		document_dictionary[filename], temp = dict_functions.create_dictionary(folder_path + filename,temp)

	dict_file = open('dict.txt','r')
	for text_line in dict_file:
		text_line = text_line.rstrip()
		text_line_divided = text_line.split(' ')

		document_word_count[text_line_divided[0]] = int(text_line_divided[1])

	dict_file.close()
	for filename in os.listdir(folder_path):# Calculating the tf-idf weights
		temp_dictionary = {}

		for key in document_dictionary[filename].keys():

			idf_key = math.log(len(document_dictionary) / (document_word_count[key] * 1.0))
			tf_key = document_dictionary[filename][key]

			temp_dictionary[key] = tf_key * idf_key		

		document_dictionary[filename] = temp_dictionary

	file_index = os.listdir(folder_path)

	for index_one in range(len(file_index)):
		for index_two in range(index_one , len(file_index)):
			
			file_index_one = file_index[index_one]
			file_index_two = file_index[index_two]
			# Take any two files compute their cosine distance
			document_one_dictionary = document_dictionary[file_index_one]

			document_two_dictionary = document_dictionary[file_index_two]

			result = calculate_distance(document_one_dictionary, document_two_dictionary)
			
			print(file_index_one, end =' ')
			print(file_index_two)

			result_dictionary[(file_index_one, file_index_two)] = math.acos(result)

	# Calculating the result and save it to the output f
	sorted_result = sorted(result_dictionary.items(), key=operator.itemgetter(1))
	os.chdir(output_folder_path)

	print("The calculation of distances has finished successfully!!!")
	result_file_name = raw_input("Please enter the name of file where you wish to save the result.\t")
	result_file = open(result_file_name ,'w')
	for item in sorted_result:
		print(item[0][0], end=' ',file=result_file)
		print(item[0][1], end=' ',file=result_file)
		print(item[1], end='\n',file=result_file)
	result_file.close()

	print("The result has been logged to the file successfully!!!")

	print("The total time taken is", end=' ')
	print(time.clock() - start)