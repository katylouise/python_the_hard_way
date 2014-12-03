print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

print "What is your favourite colour?",
colour = raw_input()
print "What is your favourite number?",
number = int(raw_input())
print "What is your name?",
name = raw_input()
print "What is your favourite food?",
food = raw_input()

print "Hi %r!  Do you fancy a %r %r?  I have %r of them." % (name, colour, food, number)

x = age * number

print x