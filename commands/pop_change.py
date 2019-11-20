import extra as e

def pc(args):
	try:
		if args[0] != '' and args[1] != "":
			base_population = e.Decimal(float(args[0]))
			try:
				rate_of_change = e.Decimal(float(args[1])/100)
			except ZeroDivisionError:
				rate_of_change = 1.75
	except IndexError:
		e.separator(1)

		print("Enter Base Population:")
		base_population = e.Decimal(float(input("--> ")))

		print("Enter Rate of Change (1.4 = 1.4%):")
		try:
			rate_of_change = e.Decimal(e.div(float(input("--> ") / 100)))
		except ZeroDivisionError:
			rate_of_change = 1.75

	e.separator(2)

	annual = round(e.mul(base_population, rate_of_change, e.TWOPLACES))
	monthly = round(e.div(annual, 12, e.TWOPLACES))
	weekly = round(e.div(annual, 52, e.TWOPLACES))
	daily = round(e.div(annual, 365, e.TWOPLACES))

	print("Annual amount = " + str(annual))
	print("Monthly amount = " + str(monthly))
	print("Weekly amount = " + str(weekly))
	print("Daily amount = " + str(daily))

	e.separator(0)
