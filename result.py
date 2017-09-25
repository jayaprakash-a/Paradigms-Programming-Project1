# Authors: Jayaprakash A
 

## Code that sorts the files with their nearest files
## based on word frequency.


"""@package docstring
Documentation for this module."""


from __future__ import print_function
import os


def calculate_nearest(file_name):
	""" Function name : calculate_nearest
	Input arguments :
		1. string file_name : Name of file that contains result
	Purpose : To find the nearest file of each and every file 
	Return Value : The dictionary containing the nearest file index of each file
    """
	result_file = open(file_name ,'r')

	size = raw_input("Please tell how many files were present in calculation of result\t")
	
	result = result_file.readlines()

	result_dict = {}
	count = 0
	for line_count in range(int(size),len(result)):
		result[line_count] = result[line_count].rstrip() 
		index1, index2, index3 = result[line_count].split(' ') 
		if index1 not in result_dict.keys():
			result_dict[index1] = index2
			count += 1
		if index2 not in result_dict.keys():
			result_dict[index2] = index1
			count += 1
		if (count == size):
			break

	return result_dict


if __name__ == "__main__":

	folder_path = raw_input("Please input the path to the folder\t")
	cur_home_dir  = os.getcwd()
	os.chdir(folder_path)

	file_name = raw_input("Please input the name of result file.\t")
	result_dict = calculate_nearest(file_name)

	os.chdir(cur_home_dir + "/out_res/")

	res_out_file = open('eval_res-nearest', 'w')
	for key in result_dict.keys():
		print(key, end=' ',file=res_out_file)
		print(result_dict[key], end='\n',file=res_out_file)
	res_out_file.close()


	print("Results have been logged to file")
