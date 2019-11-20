import api as a
import extra as e

def help(args):
	try:
		if args[0] != '':
			cmd = args[0]
	except IndexError:
		e.separator(1)
		print("Enter a Command:")
		cmd = input("--> ")
	
	try:
		desc = a.help_list[cmd]
		e.separator(2)
		print("Command: " + desc)
		e.separator(0)
	# If the command doesn't exist, give a help message
	# Note: "has_given_help_hint" is there to make sure
	# help message is only shown once per execution
	except KeyError:
		print('"' + args[0] + '"' + " is not a command.")
