def tables_and_chairs (tables_count, chairs_count):
	print "You have %d tables!" % tables_count
	print "You have %d chairs!" % chairs_count

#One
tables_and_chairs(10, 5)

#Two
number_of_tables = 15
number_of_chairs = 30

tables_and_chairs(number_of_tables, number_of_chairs)

#Three
tables_and_chairs(2 * 10, 3 * 20)

#Four
tables_and_chairs(number_of_tables, 4 * number_of_tables)

#Five
tables = raw_input("How many tables do you have? ")
chairs = raw_input("How many chairs do you have? ")

tables_and_chairs(int(tables), int(chairs))

#Six
number_of_tables = 10
number_of_chairs = number_of_tables * 10

tables_and_chairs(number_of_tables, number_of_chairs)

#Seven

