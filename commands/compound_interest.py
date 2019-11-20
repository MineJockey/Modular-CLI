import extra as e

def ci(args):
	try:
		if args[0] != '' and args[1] != "" and args[2] != "" and args[3] != "":
			principal = e.Decimal(float(args[0]))
			try:
				rate = e.Decimal(float(args[1])/100)
			except ZeroDivisionError:
				rate = 1.75
			num_times = e.Decimal(int(args[2]))
			time = e.Decimal(float(args[3]))
	except IndexError:
		e.separator(1)

		print("Enter the Principal:")
		principal = float(input("--> "))

		print("Enter the Rate (15 = 15%):")
		try:
			rate = float(input("--> ")) / 100
		except ZeroDivisionError:
			rate = 1.75

		print("Enter Number of Times Per Year:")
		num_times = float(input("--> "))

		print("Enter Time Number:")
		time = float(input("--> "))

	if num_times <= 0:
				num_times = 1

	e.separator(2)

	amount = principal * pow((1 + e.div(rate, num_times)), num_times * time)
	print("Compound Interest Amount = ", amount)

	total_amount = principal + amount
	print("Total Amount = ", total_amount)

	e.separator(0)
	