
def count_numbers(n, c):
	i = 0
	numbers = []

	while i < n:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + c
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


count_numbers(20, 2)