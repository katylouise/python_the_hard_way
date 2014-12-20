#defines a function cheese_and_crackers, which takes two args
#the function prints four lines - two with the args and two with just strings
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

#prints a string then passes the function two numbers as args
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#prints a string, then defines two variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#these two variables are then passed to the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints a string, then passes the function args using maths operations
print "We can even do maths inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#prints a string, then passes the function args using a mixture of the variables, and maths operations
print "And we can combine the two, variables and maths:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)