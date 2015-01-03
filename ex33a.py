def count_numbers(n, c):
	
	numbers = []

	for i in range(0, 11, 2):
		print "At the top i is %d" % i
		numbers.append(i)

		
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i


count_numbers(20, 2)