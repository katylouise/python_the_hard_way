#use argument variable from sys module
from sys import argv

#unpack variables
script, user_name, age = argv
#user --> as prompt
prompt = '-->'

#print three lines using user variables
print "Hi %s, I'm the %s script. You are %r years old." % (user_name, script, age)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
#display prompt and save input as likes
likes = raw_input(prompt)

#print question using user variable
print "Where to you live %s?" % user_name
#display prompt and save input as lives
lives = raw_input(prompt)

#print question then display prompt and save input as computer
print "What kind of computer do you have?"
computer = raw_input(prompt)

#print multiple lines using inputs from above.
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
