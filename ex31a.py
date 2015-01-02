print "You are walking along and come to a fork in the road.  Do you take road 1 or road 2?"

road = raw_input("> ")

if road == "1":
	print "You keep walking and come across Justin Bieber.  Do you:"
	print "1. Scream and run away."
	print "2. Laugh at him."

	response = raw_input("> ")

	if response == "1":
		print "He chases you.  Too bad."
	elif response == "2":
		print "He cries.  Good job!"
	else:
		print "I guess you could do that."

elif road == "2":
	print "You find a group of revellers.  Do you:"
	print "1. Join the party."
	print "2. Read a book."

	party = raw_input("> ")

	if party == "1":
		print "Woohoo!  Yeah!"
	else:
		print "You're a bit boring aren't you!"

else: 
	print "Come on, take a chance!"