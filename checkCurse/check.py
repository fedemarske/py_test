import urllib

def read_text():
	quotes = open("/home/fede/Dev/python/checkCurse/movie_quotes.txt")
	contents_file = quotes.read()
	print(contents_file)
	quotes.close()
	check_profanity(contents_file)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text)
	output = connection.read()
	#print(output)
	connection.close()
	#IN fot check substring
	if "true" in output:
		print("Profanity alert!")
	elif "false" in output:
		print("This document has no curse words!")
	else:
		print("Could not scan the document properly.")


read_text()