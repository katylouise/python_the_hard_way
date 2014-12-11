#import argument variables from sys module
from sys import argv

#argument variables to use are script and filename
script, filename = argv

#define variable txt as the opened file named above.
txt = open(filename)

#print the filename
print "Here's your file %r:" % filename

#print the content of txt (which is the content of the file)
print txt.read()

#print string
print "Type the filename again:"

#define variable file_again as user's input using prompt >
file_again = raw_input("> ")

#define variable txt_again as the opened file given above
txt_again = open(file_again)

#print the contents of the above file
print txt_again.read()

txt.close()
txt_again.close()