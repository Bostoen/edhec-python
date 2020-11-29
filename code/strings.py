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
         "stock": "    stock <id> <price> <volatility>",
         "deriv": "    deriv <id> <type> <parameters>...\n\n"
                  "<type> specifies which derivative to create, use command \"instruments\"\n"
                  "for full list and necessary parameters\n\n"
                  "Example: deriv my_call call aapl 110 30",
         "strat": "    strat <id> [subcommand]...\n\n"
                  "Subcommands:\n"
                  "    none             : simply creates a new strategy\n"
                  "    add <id> [short] : adds the given instrument to the strategy (long)\n"
                  "                       if [short] is set, adds a short position instead\n"
                  "    rem <id> [short] : removes the given instrument from the strategy if\n"
                  "                       the strategy contains it\n\n"
                  "Example: strat my_strat add my_call short"
         }


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
