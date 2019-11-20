import extra as e
import api as a

def commands_list(args): # args are picked up but not used
		e.separator(3)
		for i in a.help_list:
			print(i, "=", a.help_list[i])
		e.separator(0)
