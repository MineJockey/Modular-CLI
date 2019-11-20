import extra as e

def tc(args):
	try:
		if args[0] != '' and args[1] != "":
			money_amount = e.Decimal(float(args[0]))
			tax_percent = e.Decimal(float(args[1])/100)
	except IndexError:
		e.separator(1)

		print("Enter Money Amount:")
		money_amount = e.Decimal(float(input("--> ")))
		print("Enter Tax Percent (15 is 15%):")
		tax_percent = e.Decimal(float(input("--> "))/100)

	e.separator(2)

	tax_amount = e.mul(money_amount, tax_percent)
	total_amount = e.add(money_amount, tax_amount)

	print("Tax amount = " + "$"+ str(e.qnt(tax_amount, e.TWOPLACES)))
	print("Total amount = " + "$" + str(e.qnt(total_amount, e.TWOPLACES)))

	e.separator(0)