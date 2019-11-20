import extra as e
import random

def rand_num(args):
	try:
		if args[0] != '' and args[1] != "":
			min_num = int(args[0])
			max_num = int(args[1])
			count = int(args[2])
	except IndexError:
		e.separator(1)

		print("Enter Min Number:")
		min_num = float(input("--> "))

		print("Enter Max Number:")
		max_num = float(input("--> "))

		print("Enter Number Count:")
		count = int(input("--> "))

	e.separator(2)

	roll_array = []
	for i in range(0, count):
		roll = random.randrange(min_num, max_num + 1)
		roll_array.append(roll)

	print("Unsorted List:")
	print(str(roll_array))

	print("")

	roll_array.sort()
	print("Sorted List:")
	print(str(roll_array))

	print("")

	for i in range(int(min_num), int(max_num + 1)):
		if roll_array.count(i) > 0:
			print(str(i) + " appears " + str(roll_array.count(i)) + " times")
	
	e.separator(0)
