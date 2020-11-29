import code.strings as STR
"""
This file contains the main loop of the program. It will take inputs from the user and dispatch the right functions.
"""


def isfloat(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    # Initializing
    stocks = dict()
    derivatives = dict()
    strategies = dict()
    variables = {"r": 0.05, "n": 1000}
    print(STR.WELCOME)

    # Main control loop
    while True:
        raw_in = input("\n> ")
        parsed_in = list(filter(lambda x: x != "", raw_in.split(" ")))
        cmd = parsed_in[0].lower()
        args = parsed_in[1:]

        # Parse command line inputs
        if cmd == "help":
            if len(args) > 0:
                if args[0] in STR.USAGE:
                    print(STR.HELP_USAGE + STR.USAGE[args[0]])
                    continue
                else:
                    print(STR.ERR_UNKNOWN_CMD)
                    continue
            print(STR.HELP_MESSAGE)

        elif cmd == "list":
            print(STR.LIST(stocks, derivatives, strategies))

        elif cmd == "vars":
            print(STR.VARS(variables))

        elif cmd == "set":
            if len(args) >= 2 and args[0] in variables and isfloat(args[1]):
                variables[args[0]] = round(float(args[1])) if args[0] == "n" else float(args[1])
                continue
            print(STR.INCORRECT_USAGE + STR.USAGE["set"])

        elif cmd == "stock":
            if len(args) >= 2:
                continue
            print(STR.INCORRECT_USAGE + STR.USAGE["stock"])

        elif cmd == "deriv":
            if len(args) >= 2:
                continue
            print(STR.INCORRECT_USAGE + STR.USAGE["deriv"])

        elif cmd == "strat":
            if len(args) >= 2:
                continue
            print(STR.INCORRECT_USAGE + STR.USAGE["strat"])

        elif cmd == "quit":
            print(STR.QUIT)
            confirm = input("> ")
            if confirm == STR.QUIT_CONFIRM:
                break

        else:
            print(STR.ERR_UNKNOWN_CMD)
