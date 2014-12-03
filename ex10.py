# \t creates indented text
tabby_cat = "\tI'm tabbed in."
# \n creates a new line
persian_cat = "I'm split\non a line."
#to print a backslash use \\
backslash_cat = "I'm \\ a \\ cat."

#""" """ allows strings to be on multiple lines
#\t* creates indented bullet points using symbol *
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" %i,