import api as a

def command_failed(command, has_given_help_hint):
	print("")
	if command == "":
		print("Not a valid command!")
	else:
		print(command + " is not a valid command!")
	if not has_given_help_hint:
		print('Enter commands to see a list of available commands.')
	print("")

def main():
	loop = True
	has_given_help_hint = False

	# This is an infinite loop, the application is quit using quit()
	while loop:
		print("Enter a command: ")
		user_input = input("--> ")

		args = user_input.split()

		command = ''

		try:
			# Take the first argument as the command you
			# wish to use, then remove it from the array
			command = args[0]
			args.pop(0)

			# Try to call the command from the api
			try:
				func = a.commands[command]
				func(args)
			# If the command doesn't exist, give a help message
			# Note: "has_given_help_hint" is there to make sure
			# help message is only shown once per execution
			except KeyError:
				command_failed(command, has_given_help_hint)
				has_given_help_hint = True
		except IndexError or KeyError:
			command_failed(command, has_given_help_hint)
			has_given_help_hint = True

# On this script is the main program instead of a module call main()
if __name__ == '__main__':
	main()
