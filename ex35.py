#imports exit function from sys - allows you to exit the program
from sys import exit

#defines function gold_room - it takes no arguments
def gold_room():
	print "This room is full of gold.  How much do you take?"

#var choice is user's input
#if there is a 0 or 1 in in choice then it is assigned to var how_much as an integer
#changed above to check if choice is a number
#if not then the function dead is called
	choice = raw_input("> ")
	if choice.isdigit():
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

#if the amount entered is less than 50, a string is printed and the game exits
#otherwise a string is printed and the function dead is called.
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy bastard!")

#function bear_room is defined - it takes no arguments
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False

#while loop is infinite
#user's input is assigned to var choice
	while True:
		choice = raw_input("> ")

#if choice is take honey, dead function is called
#if choice is taunt bear and the bear has not moved, print string
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door.  You can go through."

#bear_moved defined as true
			bear_moved = True
#if taunt bear and bear moved, dead function called (you can't taunt it twice)
#if open door and bear moved is true, gold_room function called
#else print string
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your face off.")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."

#define function cthulhu
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"

#var choice assigned to user input
	choice = raw_input("> ")

#if flee is in the input, call function start
#if head is in the input, call function dead
#else call function cthulhu_room (recursion)
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty!")
	else:
		cthulhu_room()

#define function dead - takes argument why
#it prints arg and a string, then calls exit(0) which exits program
def dead(why):
	print why, "Good job!"
	exit(0)

#define function start - takes no argument
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"

#var choice assigned to user input
	choice = raw_input("> ")

#if choice is left, call bear_room function
#if choice is right, call cthulhu_room function
#else call dead function
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve.")


start()