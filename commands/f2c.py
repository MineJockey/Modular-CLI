import extra as e

def f2c(args):
	try:
		if args[0] != '':
			fahrenheit = e.Decimal(float(args[0]))
	except IndexError:
		e.separator(1)
		print("Enter Temperature in Fahrenheit:")
		fahrenheit = float(input("--> "))

	e.separator(2)

	centigrade_calc = (fahrenheit - 32) * (5.0 / 9.0)
	print(str(e.qnt(fahrenheit)) + " Fahrenheit in Centigrade = " + str(e.qnt(centigrade_calc)))

	e.separator(0)
