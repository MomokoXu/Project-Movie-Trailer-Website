# step1: read files from a folder
# step2: rename file name for each file

import os

def rename_files():
	# step1
	file_list = os.listdir("/Users/momoko/Desktop/Nanodegree/Python_Basics/photos")
	print(file_list)
	# get current working directory
	path = os.getcwd()
	# change it to directory where photos are in
	os.chdir("/Users/momoko/Desktop/Nanodegree/Python_Basics/photos")
	# step2
	'''TODO: consider how to handle situations: open an file not existing 
	and create a file that is already existing'''
	for file_name in file_list:
		print("Old Name " + file_name)
		print("New name " + file_name.translate(None, "0123456789"))
		os.rename(file_name, file_name.translate(None, "0123456789"))
	# change back to orginal working directory
	os.chdir(path)
rename_files()