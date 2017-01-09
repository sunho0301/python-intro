# python cheat sheet

# Variable assignment (no type declaration)
x = 1

# array (called list in python)
arr = [1, 2, 3]

# dictionary
dictionary = {"key": "value", "other_thing": 2}

# Other types
t = True

f = False

s = "a string"

# for loop
for element in arr:
	print(element) # 1 ... 2 ... 3

# tuple
a = ("test", 1)

# multiple assignment
x, y = a

# For loop through a dictionary
for key, value in dictionary.items():
	print(str(key) + ": " + str(value))

	# Or...
	print("%s: %d" % (key, value))

# loop from 0 to n
for i in range(0, 10):
	print(i, end="") # prints 0 - 9

# while
x = 0
while x < 10:
	x += 1

if 1 == 2:
	# Never true

# if dict contains (also works for lists)
if "other_thing" in dictionary:
	# True

# Dict does not contain
if "test" not in dictionary:
	# True
