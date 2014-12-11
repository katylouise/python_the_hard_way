#import argv from sys module
from sys import argv

#variables to use
script, filename = argv

#print three lines - first one uses the filename given above.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#prompt user for input using ?
raw_input("?")

#print string
print "Opening the file..."

#define file object as the file given above.  It is writable.
target = open(filename, 'w')

#print string
print "Truncating the file.  Goodbye!"

#empty the file object
target.truncate()

#print string
print "Now I'm going to ask you for three lines."

#prompt user for three lines of input
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#print string
print "I'm going to write these to the file."

#define variable content as user's three line inputs
content = "%s \n %s \n %s" % (line1, line2, line3)

#write content to file named above
target.write(content)


#print string
print "And finally, we close it."

#close file object
target.close()