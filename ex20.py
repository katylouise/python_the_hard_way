#import arguments from sys
from sys import argv

#arguments to import
script, input_file = argv

#define function print_all taking one arg (f) 
#the function prints the contents of f
def print_all(f):
	print f.read()

#define function rewind taking one arg (f)
#the function sets file position to 0 byte position (beginning)
def rewind(f):
	f.seek(0)

#define function print_a_line taking two args (line_count, f)
#the function prints the 1st arg and one line from f
def print_a_line(line_count, f):
	print line_count, f.readline()

#sets var current_file to the opened input_file
current_file = open(input_file)

#print string, then new line
print "First let's print the whole file: \n"

#run function print_all on current_file
print_all(current_file)

#print string
print "Now let's rewind, kind of like a tape."

#run rewind function on current_file
rewind(current_file)

#print string
print "Let's print three lines:"

#sets current_line to 1, then uses this arg with to print the 1st line of current_file
current_line = 1
print_a_line(current_line, current_file)

#keep adding one to current_line and printing subsequent lines of current_file
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)