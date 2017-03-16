''' 
function open(): python built-in function 
that is always avaliable to use no need to import anything

function urlopen(): use urllib module in python standard library to open an url
'''
import urllib

def read_text():
	# open file
	quotes = open("/Users/momoko/Desktop/Project_Movie_Trailer_Website/related_python_lessons_with_codes/movie_quotes.txt")
	contents_of_files = quotes.read()
	quotes.close()
	check_profanity(contents_of_files)

def check_profanity(text_to_check):
	#urllib open url from website 
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	connection.close()
	if "false" in output:
		print "This document has no curse words!"
	else:
		print "Profanity Alert!"

read_text()