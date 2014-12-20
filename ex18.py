#this one is like your scripts with argv
#this function takes some arguments - these are defined on the first line of the function
#the function then prints the two arguments
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok, that *args is actually pointless, we can just do this
#this function takes two arguments and prints them out
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument and then prints it out
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments so only prints the same string each time.
def print_none():
	print "I got nothin'."

#these lines call the four functions defined above
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()