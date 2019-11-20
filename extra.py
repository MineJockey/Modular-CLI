from decimal import Decimal

# region Global Variables

ONEPLACE = Decimal(10) ** -1
TWOPLACES = Decimal(10) ** -2
THREEPLACES = Decimal(10) ** -3

rounding_num = THREEPLACES

separators = {
		0: "--------------------",
		1: "-Input--------------",
		2: "-Output-------------",
		3: "-Commands-----------"
}

if not __name__ == '__main__':
	def separator(separator_index):
		print("")
		print(separators[separator_index])
		print("")


	def add(x, y, fp=rounding_num):
		return Decimal(x + y).quantize(fp)


	def sub(x, y, fp=rounding_num):
		return Decimal(x - y).quantize(fp)


	def mul(x, y, fp=rounding_num):
		return Decimal(x * y).quantize(fp)


	def div(x, y, fp=rounding_num):
		try:
			val = Decimal(x / y).quantize(fp)
		except ZeroDivisionError:
			val = 0
		return val


	def qnt(x, fp=rounding_num):
		return Decimal(x).quantize(fp)