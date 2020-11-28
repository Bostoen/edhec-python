import code.strings as STR
"""
This file contains the main loop of the program. It will take inputs from the user and dispatch the right functions.
"""


if __name__ == "__main__":
    # Initializing
    stocks = dict()
    derivatives = dict()
    strategies = dict()
    variables = dict()
    print(STR.WELCOME)

    # Main control loop
    while True:
        raw_in = input("\n> ")
        parsed_in = list(filter(lambda x: x != "", raw_in.split(" ")))
        cmd = parsed_in[0].lower()
        args = parsed_in[1:]

        # Parse command line inputs
        if cmd == "help":
            print(STR.HELP_MESSAGE)

        if cmd == "list":
            print(STR.LIST(stocks, derivatives, strategies))
        
        if cmd == "vars":
            print(STR.VARS(variables))

        elif cmd == "quit":
            print(STR.QUIT)
            confirm = input("> ")
            if confirm == STR.QUIT_CONFIRM:
                break

        else:
            print(STR.ERR_UNKNOWN_CMD)
