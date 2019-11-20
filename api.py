import commands.basic_calc as basic_calc
import commands.tax_calc as tax_calc
import commands.compound_interest as compound_interest
import commands.commands as commands
import commands.credit_interest as credit_interest
import commands.pop_change as pop_change
import commands.mc_cube_calc as mc_cube_calc
import commands.sct as sct
import commands.asct as asct
import commands.c2f as c2f
import commands.f2c as f2c
import commands.numgen as numgen
import commands.rpg as rpg
import commands.sc as sc
import commands.help as cli_help

commands = {
		"bc": basic_calc.bc,
		"tc": tax_calc.tc,
		"ci": compound_interest.ci,
		"ci2": credit_interest.ci2,
		"pc": pop_change.pc,
		"sc": sc.sc,
		"sct": sct.sct,
		"asct": asct.asct,
		"c2f": c2f.c2f,
		"f2c": f2c.f2c,
		"numgen": numgen.rand_num,
		"rpg": rpg.rpg,
		"mccc": mc_cube_calc.mccc,
		# Help & Alias
		"help": cli_help.help,
		"h": cli_help.help,
		# Commands & Alias
		"commands": commands.commands_list,
		"cmds": commands.commands_list,
		# Quit & Alias
		"quit": quit,
		"q": quit
}

help_list = {
		"bc": "Basic Calculator",
		"tc": "Tax Calculator",
		"ci": "Compound Interest Calculator",
		"ci2": "Credit Interest Calculator",
		"pc": "Population Change Calculator",
		"sc": "Basic Salary Calculator",
		"sct": "Sin, Cos, Tan",
		"asct": "ASin, ACos, ATan",
		"c2f": "Centigrade to Fahrenheit",
		"f2c": "Fahrenheit to Centigrade",
		"numgen": "Random Number Generator",
		"rpg": "Random Password Generator",
		"mccc": "Get the block amount required to build a hollow cube in Minecraft",
		"help": "Shows more detailed information about a commands",
		"commands": "Displays this list of commands",
		"quit": "Quit the application"
}
