#variable cars sets number of cars
cars = 100
#variable space_in_a_car sets number of seats in car
space_in_a_car = 4.0
#variable drivers sets number of drivers
drivers = 30
#variable passengers sets number of passengers
passengers = 90
#variable cars_not_driven is the difference between no. of cars and no. of drivers
cars_not_driven = cars - drivers
#variable cars_driven is equal to the no. of drivers
cars_driven = drivers
#variable carpool_capacity is the total number of available seats
carpool_capacity = cars_driven * space_in_a_car
#variable average_passengers_per_car is the no. of passengers divided between the cars
average_passengers_per_car = passengers / cars_driven

#print no. of cars available
print "There are", cars, "cars available."
#print no. of drivers available
print "There are only", drivers, "drivers available."
#print no. of empty cars
print "There will be", cars_not_driven, "empty cars today."
#print no. of available seats
print "We can transport", carpool_capacity, "people today."
#print no. of passengers 
print "We have", passengers, "to carpool today."
#print no. of passengers to go in each car
print "We need to put about", average_passengers_per_car, "in each car."
