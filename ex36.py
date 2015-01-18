from sys import exit

def jewel_room():
	print "This room is full of beautiful gems."
	print "There is a dragon guarding the jewels."
	print "He asks you for the magic word."
	print "What is the magic word?"
	print "Hint: be polite."

	choice = raw_input("> ")

	if choice == "please":
		print "Correct!"
		print "The dragon moves."
		print "How many gems do you want to take?"

		how_much = int(raw_input("> "))

		if how_much <= 50:
			print "Here you go!"
			print "Thanks for playing."
			print "Enjoy your gems!"
			exit(0)

		elif how_much > 50: 
			dead("Too much!  The dragon breathes fire on you.")

		else:
			dead("You have angered the dragon.  He breathes fire on you.")

	else:
		dead("Wrong! The dragon breathes fire on you.")

def mirror_room():
	print "You are in a room full of mirrors."
	print "There is a wizard in the room."
	print "He offers you a gift."
	print "You can choose between a sweet, a key and a hammer."
	print "Which do you take?"

	choice = raw_input("> ")

	if choice == "sweet":
		dead("It is poisoned!")

	elif choice == "key":
		print "The key unlocks a hidden door and you go through it."
		water_room()

	elif choice == "hammer":
		print "You smash all the mirrors."
		snake_room()

	else:
		dead("The wizard kills you for your ungratefulness and poor spelling.")

def snake_room():
	print "You are in a room full of snakes."
	print "A boa constrictor is approaching you."
	print "How will you move the snake?"
	print "You can use your hammer, fight it or charm it."

	choice = raw_input("> ")

	if choice == "hammer":
		print "You miss and hit yourself on the head."
		print "You wake up back in the room of mirrors."
		mirror_room()

	elif choice == "fight it":
		dead("You lose and the snake squeezes you to death.")

	elif choice == "charm it":
		print "The snake falls asleep and moves out the way."
		water_room()

	else:
		print "That's not going to work!"
		dead("The snake eats your head.")

def water_room():
	print "You are in a room filled with a giant lake."
	print "In front of you is a boat, a bridge and some armbands."
	print "Which do you use to cross the lake?"

	choice = raw_input("> ")

	if choice == "boat":
		dead("The boat sinks and you drown.")

	elif choice == "bridge":
		print "You slip on the wet bridge, knocking yourself unconcious."
		mirror_room()

	elif choice == "armbands":
		print "You swim across the lake."
		jewel_room()

def dead(why):
	print why, "Shame Shame!"
	print "****************"
	print "Play Again?"

	choice = (raw_input("> ")).lower()

	if choice == "yes":
		start()

	else:
		exit(0)

def start():
	print "You are in a dark corridor."
	print "You see two doors, one on the left and one on the right."
	print "Which do you take?"

	choice = raw_input("> ") 

	if choice == "left":
		mirror_room()

	elif choice == "right":
		snake_room()

	else: 
		dead("You wander around for days until you die of starvation.")

start()



