import extra as e

def sc(args):
	try:
		if args[0] != '' and args[1] != '':
			input_type = args[0]
			num = float(args[1])
	except IndexError:
		e.separator(1)
		print("Enter the input type: a, m, bm, w, bw")
		input_type = input("--> ")
		print('Enter a salary:')
		num = float(input("--> "))

	# Convert input to lowercase instead of checking variants
	input_type = str.lower(input_type)
	
	# Convert the salary to Annual
	if input_type == 'm':
		num *= 12
	elif input_type == 'bm':
		num *= 24
	elif input_type == 'w':
		num *= 52
	elif input_type == 'bw':
		num *= 26
	else:
		pass
	
	# Do calculation based on Annual
	a = num
	m = e.div(a, 12)
	bm = e.div(a, 24)
	w = e.div(a, 52)
	bw = e.div(a, 26)

	e.separator(2)

	print("Annual Salary = " + str(e.qnt(a)))
	print("Monthly Salary = " + str(e.qnt(m)))
	print("Bi-Monthly Salary = " + str(e.qnt(bm)))
	print("Weekly Salary = " + str(e.qnt(w)))
	print("Bi-Weekly Salary = " + str(e.qnt(bw)))

	e.separator(2)
