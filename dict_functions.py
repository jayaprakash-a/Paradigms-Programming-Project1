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
# @param delimiter character to differentiate words
delimiters = "\'\"/<?>,.:*-+\\=`~!@#^&()_ ;{}[]|"




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
	text_line = text_line.replace("\t", ";")
	return text_line.split(';')


def create_dictionary(file_path,document_word_count):
	""" Function name : create_dictionary
	Input arguments :
		1. string file_path : The path to the file to be read.
		2. dictionary document_word_count : The dicitonary responsible for training
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


	return my_dictionary, document_word_count


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