"""
This file simply contains the strings for the main program.
"""

# Communication
VERSION_NUMBER = "v1.2"
WELCOME = "\nCopyright 2020 Hector Bostoen. Intended for academic purposes.\n\n" \
          "Welcome to Python Derivative Pricer " + VERSION_NUMBER + ". Type \"help\" for a list of commands."

# Commands
HELP_MESSAGE = "Commands and syntax. Type \"help <command>\" for specific usage and parameters.\n" \
               "add    : Add a leg to a strategy\n" \
               "del    : Delete a Stock, Derivative or Strategy\n" \
               "deriv  : Create a new derivative\n" \
               "help   : Program help\n" \
               "list   : List all Stocks, Derivatives and Strategies in memory\n" \
               "price  : Return the price of a given derivative or strategy\n" \
               "quit   : Quit\n" \
               "rem    : Remove a leg from a strategy\n" \
               "set    : Set environment variables\n" \
               "show   : View the details of a Stock, Derivative or Strategy\n" \
               "stock  : Create a new stock\n" \
               "strat  : Create a new strategy, or modify an existing one\n" \
               "types  : Full list of possible derivative types\n" \
               "vars   : Show current values for environment variables"

HELP_USAGE = "Command usage:\n"
USAGE = {"set":   "    set {r|n} <value>\n\n"
                  "r: riskfree rate, default = 0.03\n"
                  "n: number of Monte Carlo iterations, default = 10^4",
         "stock": "    stock <id> [price] [volatility]\n\n"
                  "If price and volatility are not set, automatically assumes <id> is the\n"
                  "ticker, and gets data from yahoo finance.\n\n"
                  "Examples: stock my_stock 100 0.2\n"
                  "          stock aapl    # Gets Apple price & vol from Yahoo",
         "deriv": "    deriv <id> <type> <parameters>...\n\n"
                  "Use command \"types\" for a full list of possible derivatives and their\n"
                  "necessary parameters.\n\n"
                  "Example: deriv my_deriv call my_stock 110 30",
         "strat": "    strat <id> <underlying_id>\n\n"
                  "<underlying_id> must refer to a stock. Use commands \"add\" and \"rem\" to add and\n"
                  "remove legs from the strategy.\n\n"
                  "Example: strat my_strat my_stock",
         "add":   "    add <strat_id> <deriv_id> [short]\n\n"
                  "Adds the given instrument to the strategy. If [short] is set, adds a short position instead.\n\n"
                  "Example: add my_strat my_call short",
         "rem":   "    rem <strat_id> <deriv_id> [short]\n\n"
                  "Removes the given instrument from the strategy if the strategy contains it.\n\n"
                  "Example: rem my_strat my_call short",
         "show":  "    show <id>",
         "del":   "    del <id>",
         "price": "    price <id>\n\n"
                  "Return the price of an instrument. The riskfree rate and number of Monte-Carlo iterations\n"
                  "can be set with the \"set\" command. Defaults are 0.03 and 10^4 respectively."
         }

TYPES = "List of possible derivative types:\n" \
        "    <type>      <parameters>...\n" \
        "Vanilla options. Specify the id of the underlying stock, the strike and the #days to expiry.\n" \
        "    call        <underlying_id> <strike> <dte>\n" \
        "    put         <underlying_id> <strike> <dte>\n" \
        "Asian options. Same parameters.\n" \
        "    asian_call  <underlying_id> <strike> <dte>\n" \
        "    asian_put   <underlying_id> <strike> <dte>\n" \
        "Binary options. Same parameters. Optionally specify the notional amount, default is $1.\n" \
        "    binary_call <underlying_id> <strike> <dte> [notional]\n" \
        "    binary_put  <underlying_id> <strike> <dte> [notional]\n" \
        "Barrier options. Specify the id of the underlying derivative (e.g. a Call) and the barrier.\n" \
        "    up_out      <derivative_id> <barrier>\n" \
        "    up_in       <derivative_id> <barrier>\n" \
        "    down_out    <derivative_id> <barrier>\n" \
        "    down_in     <derivative_id> <barrier>"

STOCK_SUCCESS = "New Stock created."
DERIV_SUCCESS = "New Derivative created."
STRAT_SUCCESS = "New Strategy created."
ADD_SUCCESS = "Derivative added to Strategy."
REM_SUCCESS = "Derivative removed from Strategy."


def LIST(stocks, derivatives, strategies) -> str:
    string = ""
    empty = True
    if len(stocks) > 0:
        empty = False
        string += "Stocks\n"
        for i in stocks:
            string += i + " : " + str(stocks[i]) + "\n"
        string += "\n"
    if len(derivatives) > 0:
        empty = False
        string += "Derivatives\n"
        for i in derivatives:
            string += i + " : " + str(derivatives[i]) + "\n"
        string += "\n"
    if len(strategies) > 0:
        empty = False
        string += "Strategies\n"
        for i in strategies:
            string += i + " : " + str(strategies[i]) + "\n"
        string += "\n"
    return "No objects in memory." if empty else string.rstrip("\n\n")


def VARS(variables):
    return "Current environment variables\nRiskfree rate: " + str(variables["r"]) + "\nMonte Carlo iterations: "\
           + str(variables["n"])


PRICE_STOCK = "Price of Stock "
PRICE_DERIV = "Price of Derivative "
PRICE_STRAT = "Price of Strategy "


QUIT = "Do you want to quit? Data will not be saved.\nType Y to confirm."
QUIT_CONFIRM = "Y"

# Errors
ERR_UNDERLYING = "Underlying id not found in memory. Please check spelling and try again."
ERR_NAME_UNKNOWN = "No such object in memory. Please check spelling and try again."
ERR_NAME_TAKEN = "This id is already in use."
ERR_TICKER_NON_EXISTANT = "Unknown ticker. Please try again."
ERR_INCORRECT_USAGE = "Parsing error or missing arguments. Correct usage:\n"
ERR_UNKNOWN_CMD = "Unknown command. Type \"help\" for a list of commands."
ERR_ADD = "Strategy and derivative have different underlying stocks."
ERR_REM = "Strategy does not contain this derivative. Make sure to specify the [short] flag if the\n" \
          "leg is short."
