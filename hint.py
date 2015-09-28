# '#' is a comment character in Python. So don't put it in front of your lines!
# Python uses spacing instead of brackets {} and ; to tell where statements end.
# So, the whole body of a for-loop has to be tabbed once more than the "for" statement. The for-loop ends when a line is tabbed less than the "for" statement.
# Also, arrays are called "lists" in Python.
# Here is how the logic of your 7-line code will look:

#binarydump = "[paste the giant binary string here]"
#import sys (this allows printing characters without newlines between them)

#declare a for loop to read from the beginning (0) to the end (hint: use "len()") that "steps" 6 characters ahead between each read (because each word is 6 bits long)
	#hexc = "{0:0>2}".format([hex value of the 6 binary characters you read][2:])
	#find the position (index) of each hex value you read in hexlist
	#find the character in asciilist corresponding to that position
	#sys.stdout.write(the character)
