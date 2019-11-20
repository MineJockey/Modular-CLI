import extra as e

def mccc(args):
	try:
		if args[0] != '':
			width = e.Decimal(float(args[0]))
	except IndexError:
		e.separator(1)
		print("Enter an Width:")
		width = abs(int(input("--> ")))

	required_blocks = 0
	if width <= 1:
		width = 1
		required_blocks = 1
	if width == 2:
		required_blocks = 8
	if width >= 3:
		required_blocks = ((width*width) + (width*(width-2)) + ((width-2)*(width-2)))*2

	e.separator(2)

	print("Required Blocks = " + str(required_blocks))

	e.separator(0)
