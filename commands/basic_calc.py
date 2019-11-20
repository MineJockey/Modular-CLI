import extra as e

def bc(args):
	try:
		if args[0] != '' and args[1] != "":
			num1 = e.Decimal(float(args[0]))
			num2 = e.Decimal(float(args[1]))
	except IndexError:
		e.separator(1)

		print("Enter Number 1:")
		num1 = e.Decimal(float(input("--> ")))

		print("Enter Number 2:")
		num2 = e.Decimal(float(input("--> ")))

	e.separator(2)

	print("Addition = " + str(e.add(num1, num2)))
	print("Subtraction = " + str(e.sub(num1, num2)))
	print("Multiplication = " + str(e.mul(num1, num2)))
	print("Division = " + str(e.div(num1, num2)))
	
	e.separator(0)