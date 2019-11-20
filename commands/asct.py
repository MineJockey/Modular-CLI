import extra as e
from math import radians, asin, acos, atan

def asct(args):
	try:
		if args[0] != '':
			angle = e.Decimal(float(args[0]))
	except IndexError:
		e.separator(1)
		print("Enter an Angle:")
		angle = e.Decimal(radians(float(input("--> "))))

	e.separator(2)

	arc_sin = asin(angle)
	arc_cos = acos(angle)
	arc_tan = atan(angle)

	print("Sine = " + str(e.qnt(arc_sin)))
	print("Cosine = " + str(e.qnt(arc_cos)))
	print("Tangent = " + str(e.qnt(arc_tan)))

	e.separator(0)
