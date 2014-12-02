name = 'Zed A. Shaw'
age = 35 # not a lie
height_imp = 74.0 # inches
height_met = height_imp * 2.5 #cm
weight_imp = 180 # lbs
weight_met = weight_imp * 0.5 #kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall.  This is %d cm tall." % (height_imp, height_met)
print "He's %d pounds heavy.  This is %d kg." % (weight_imp, weight_met)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height_imp, weight_imp, age + height_imp + weight_imp)