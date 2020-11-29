"""
This file simply contains the strings for the main program.
"""

# Communication
VERSION_NUMBER = "v0.1"
WELCOME = "Welcome to _NAME_ " + VERSION_NUMBER + ". Type \"help\" for a list of commands."

# Commands
HELP_MESSAGE = "Commands and syntax. Type \"help <command>\" for specific usage and parameters.\n" \
               "help    : Program help\n" \
               "list    : List all Stocks, Derivatives and Strategies in memory\n" \
               "quit    : Quit\n" \
               "set     : Set environment variables\n" \
               "vars    : Show current values for environment variables"

HELP_USAGE = "Command usage:\n"
USAGE = {"set"  : "    set {r|n} <value>\n"
                  "r: riskfree rate | n: number of Monte Carlo iterations\n",
         "stock": "    stock <ticker> <price> <volatility>",
         "deriv": "    deriv <type> ",
         "strat": "    strat"}


def LIST(stocks, derivatives, strategies) -> str:
    string = ""
    if len(stocks) > 0:
        string += "Stocks\n"
        for i in stocks:
            string += i + " : " + str(stocks[i]) + "\n"
    if len(derivatives) > 0:
        string += "Derivatives\n"
        for i in derivatives:
            string += i + " : " + str(derivatives[i]) + "\n"
    if len(strategies) > 0:
        string += "Strategies\n"
        for i in strategies:
            string += i + " : " + str(strategies[i]) + "\n"
    return string.rstrip("\n")


def VARS(variables):
    return "Current environment variables\nRiskfree rate: " + str(variables["r"]) + "\nMonte Carlo iterations: "\
           + str(variables["n"])


QUIT = "Do you want to quit? Data will not be saved.\nType Y to confirm."
QUIT_CONFIRM = "Y"

# Errors
INCORRECT_USAGE = "Parsing error or missing arguments. Correct usage:\n"
ERR_UNKNOWN_CMD = "Unknown command. Type \"help\" for a list of commands."
