import extra as e
from math import radians, sin, cos, tan

def sct(args):
	try:
		if args[0] != '':
			angle = e.Decimal(float(args[0]))
	except IndexError:
		e.separator(1)
		print("Enter an Angle:")
		angle = e.Decimal(radians(float(input("--> "))))

	e.separator(2)

	ang_sin = sin(angle)
	ang_cos = cos(angle)
	ang_tan = tan(angle)

	print("Sine = " + str(e.qnt(ang_sin)))
	print("Cosine = " + str(e.qnt(ang_cos)))
	print("Tangent = " + str(e.qnt(ang_tan)))

	e.separator(0)
