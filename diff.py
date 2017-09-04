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
	
	print my_dictionary

if __name__ == "__main__":
    file1 = "temp.txt"
    mydict = {}
    create_dictionary(file1, mydict)