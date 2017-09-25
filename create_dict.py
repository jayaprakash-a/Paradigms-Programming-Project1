# Authors: Jayaprakash A
# Testers: 
# 

## Code that creates the dictionary that contains word count 
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


if __name__ == "__main__":
	

	folder_path = raw_input("Please input the path to the folder\t")
	document_dictionary = {}
	document_word_count = {}

	for folder in os.listdir(folder_path):# Create the word vector for each and every file in the folder
		for filename in os.listdir(folder_path + folder):
			document_dictionary[filename], document_word_count = dict_functions.create_dictionary(folder_path + folder+ '/' + filename, document_word_count)
			print (filename)

	print("Finished creating dictionary saving to file!!!!")
	dict_file = open('dict.txt','w')
	for key in document_word_count.keys():
		print(key,end=' ',file=dict_file)
		print(key)

		print(document_word_count[key],end='\n',file=dict_file)

	print("Finished")

	dict_file.close()