"""
This file simply contains the strings for the main program.
"""

# Communication
VERSION_NUMBER = "v0.1"
WELCOME = "Welcome to _NAME_ " + VERSION_NUMBER + ". Type \"help\" for a list of commands."

# Commands
HELP_MESSAGE = "Commands and syntax. Refer to the \n" \
               "help        : Program help" \
               "quit        : Quit"


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


def VARS(variables) -> str:
    string = "Environment Variables\n"
    if len(variables) > 0:
        for i in variables:
            string += i + ": " + str(variables[i]) + "\n"
    return string.rstrip("\n")


QUIT = "Do you want to quit? Data will not be saved.\nType Y to confirm."
QUIT_CONFIRM = "Y"

# Errors
ERR_UNKNOWN_CMD = "Unknown command. Type \"help\" for a list of commands."
