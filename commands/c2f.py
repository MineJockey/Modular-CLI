import extra as e

def c2f(args):
	try:
		if args[0] != '':
			centigrade = e.Decimal(float(args[0]))
	except IndexError:
		e.separator(1)
		print("Enter Temperature in Centigrade:")
		centigrade = float(input("--> "))

	e.separator(2)

	fahrenheit_calc = 1.8 * centigrade + 32
	print(str(e.qnt(centigrade)) + " Centigrade in Fahrenheit = " + str(e.qnt(fahrenheit_calc)))

	e.separator(0)
