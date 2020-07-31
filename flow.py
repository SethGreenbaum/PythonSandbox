for i in range(1, 13):
    print("this hole is {} centimeters wide".format(i))

name = input("Please enter your name: ")
age = int(input("How old are you, {}?".format(name)))
print("So you're " + str(age) + "?")

if age > 18:
    print("You better vote!  or else!")
elif age == 18:
    print("First Election? You better vote!  or else!")
else:
    print("In {0} years you better vote! "
          "\n (assuming democracy is still intact) ".format(18-age))
