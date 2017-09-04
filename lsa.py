delimiters = "\'\"/<?>,.:*-+\\=`~!@#$%^&()_ ;"


def format_text(text_line):
	
	text_line = text_line.rstrip()
	text_line = text_line.split('.')


def remove_delimiters(text_line):

	for ch in delimiters:
		text_line = text_line.replace(ch, ";")
	
	return text_line


def create_dictionary(file_path, my_dictionary):
	
	text_document = open("temp.txt", 'r')
	text_line = text_document.readlines()

	for line in text_line:
		print line
	return

	for text_line in text_document: 
		text_line_buffer = format_text(text_line)
	
		for word in text_line_buffer:
			word = word.lower()
	
			if word != '' and word not in my_dictionary:
				my_dictionary[word] = 1
			elif word in my_dictionary:
				my_dictionary[word] += 1

mydict= {}
create_dictionary("d", mydict)