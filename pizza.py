# from a module sys, import the feature named argv
from sys import argv
import math
# unpack argv into script and attendees
script, attendees = argv

print "{} attendees? If this is correct, \
hit ENTER. If not, exit with CTRL-C.".format(attendees)
raw_input()

# calculates amount of total slices, assuming 3 per person
total_slices = int(attendees) * 3
print "That's a total of {} slices!".format(total_slices)

# calculates amount of boxes to be ordered, assuming 8 slices per box
total_boxes = (total_slices // 8) + 1
print "And {} boxes in total.".format(total_boxes)
print ""
print "Please enter the flavor breakdowns below! \
You'll have a choice of 4 non- gluten-free flavors and 1 gluten-free flavor:"
print ""

# takes flavor input
firstChoice = raw_input("35% should be: ")
# calculates percentage from total boxes
firstChoice_boxes = total_boxes * 0.35
print "firstChoice_boxes is currently at {}".format(firstChoice_boxes)
print "total_boxes is currently at {}".format(total_boxes)

secondChoice = raw_input("30% should be: ")
secondChoice_boxes = total_boxes * 0.30
print "secondChoice_boxes is currently at {}".format(secondChoice_boxes)
print "total_boxes is currently at {}".format(total_boxes)

thirdChoice = raw_input("20% should be: ")
thirdChoice_boxes = total_boxes * 0.20
print "thirdChoice_boxes is currently at {}".format(secondChoice_boxes)
print "total_boxes is currently at {}".format(total_boxes)

fourthChoice = raw_input("10% should be: ")
fourthChoice_boxes = total_boxes * 0.10
print "fourthChoice_boxes is currently at {}".format(fourthChoice_boxes)
print "total_boxes is currently at {}".format(total_boxes)

glutenFreeChoice = raw_input("The gluten-free should be: ")
glutenFreeChoice_boxes = total_boxes * 0.05
print "glutenFreeChoice_boxes is currently at {}".format(glutenFreeChoice_boxes)
print "total_boxes is currently at {}".format(total_boxes)

print ""
print "You should order {} boxes of {!s}, \
{} of {!s}, {} of {!s}, and {} of gluten-free {!s}".format(firstChoice_boxes, firstChoice, secondChoice_boxes, secondChoice, thirdChoice_boxes, thirdChoice, fourthChoice_boxes, fourthChoice, glutenFreeChoice_boxes, glutenFreeChoice)
print "That's a total of {} boxes of pizza. Yum!".format(firstChoice_boxes + secondChoice_boxes + thirdChoice_boxes + fourthChoice_boxes + glutenFreeChoice_boxes)
