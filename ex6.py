#variable x set to a string with a number variable inserted using %d
x = "There are %d types of people." % 10
#variable binary set to a string
binary = "binary"
#variable do_not set to a string
do_not = "don't"
#variable y set to a string containing the two above strings using %s.
y = "Those who know %s and those who %s." % (binary, do_not)

#print x then print y
print x
print y

#print string containing x (which also contains a number variable)
print "I said: %r." % x
#print string containining y - using %s because y only contains strings?
print "I also said: '%s'." % y

#defining variable hilarious as False
hilarious = False
#variable joke_evaluation 
joke_evaluation = "Isn't that joke so funny?! %r"
#print joke_evaluation including hilarious variable inside string
print joke_evaluation % hilarious

#variables w and e defined as strings
w = "This is the left side of..."
e = "a string with a right side."

#print w and e as one string (I think)
print w + e