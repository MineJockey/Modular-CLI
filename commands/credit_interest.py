import extra as e

def ci2(args):
	try:
		if args[0] != '' and args[1] != "":
			principal = e.Decimal(float(args[0]))
			try:
				rate = e.Decimal(float(args[1])/100)
			except ZeroDivisionError:
				rate = 1.75
	except IndexError:
		e.separator(1)

		print("Enter the Principal:")
		principal = float(input("--> "))

		print("Enter the Rate (15 = 15%):")
		try:
			rate = float(input("--> ")) / 100
		except ZeroDivisionError:
			rate = 1.75

	e.separator(2)

	ca = principal * (rate/12)
	print("Credit Interest Amount = ", e.qnt(ca, e.TWOPLACES))

	e.separator(0)
