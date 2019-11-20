import string
import extra as e

alphabet = string.ascii_letters + string.digits
passwords = []

def rpg(args):
	try:
		import secrets
		try:
			if args[0] != '':
				try:
					pass_length = int(args[0])
				except ValueError:
					pass_length = 8
				if pass_length == 0:
					pass_length = 8
		except IndexError:
			e.separator(1)
			try:
				pass_length = int(input("Enter password length --> "))
			except ValueError:
				pass_length = 8
			if pass_length == 0:
				pass_length = 8

		password = ''.join(secrets.choice(alphabet) for i in range(pass_length))
		passwords.append(password)

		e.separator(2)
		print(passwords[-1])
		e.separator(0)

		with open("Generated Passwords.txt", "a") as f:
			print("", file = f)
			print(passwords[-1], file = f)

	except ImportError:
		print("")
		print("The Random Password Generator only works in python 3.6 or newer!")
		print("")
