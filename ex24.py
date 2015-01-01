#print two strings
#the second string has escapes for a backslash, new line and tab
print "Let's practise everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#variable poem is a multi-line string (uses """ """) containing new line and tab escapes
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""

#print two strings with the poem variable in the middle
print "--------------"
print poem
print "--------------"

#variable five has value 5
five = 10 - 2 + 3 - 6
#print string with variable five at end (as string not integer)
print "This should be five: %s" % five

#define function taking one arg
#three variables create within it which are returned
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#variable start_point assigned value 10000
start_point = 10000
#beans, jars, crates assigned values returned from secret_formula function
beans, jars, crates = secret_formula(start_point)

#print string with integer start_point
print "With a starting point of: %d" % start_point
#print string with integers beans, jars, crates
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#start_point redefined as start_point divided by 10
start_point = start_point / 10

#print string
print "We can also do that this way:"
#print string with integers the three returned values from secret_formula function
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)