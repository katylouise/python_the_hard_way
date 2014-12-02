#declares variable formatter
formatter = "%r %r %r %r"
#print formatter using numbers
print formatter % (1, 2, 3, 4)
#print formatter using strings
print formatter % ("one", "two", "three", "four")
#print formatter using booleans
print formatter % (True, False, False, True)
#print formatter using itself
print formatter % (formatter, formatter, formatter, formatter)
#print formatter taking four longer strings on one line
print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.", #this line comes out with "" because of didn't
		"So I said goodnight."
)