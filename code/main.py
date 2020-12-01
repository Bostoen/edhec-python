import strings as STR
from functions import *
"""
This file contains the main loop of the program. It will take inputs from the user and dispatch the right functions.
"""


if __name__ == "__main__":
    # Initializing
    stocks = dict()
    derivatives = dict()
    strategies = dict()
    variables = {"r": 0.03, "n": 10**4}
    print(STR.WELCOME)


    def isfloat(value: str) -> bool:
        try:
            float(value)
            return True
        except ValueError:
            return False

    def name_taken(name):
        return (name in stocks) or (name in derivatives) or (name in strategies)

    # Main control loop
    while True:
        raw_in = input("\n> ")
        parsed_in = list(filter(lambda x: x != "", raw_in.split(" ")))
        if len(parsed_in) == 0:
            continue
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

        elif cmd == "types":
            print(STR.TYPES)

        elif cmd == "show":
            if len(args) == 1:
                if args[0] in stocks:
                    print(args[0] + " : " + str(stocks[args[0]]))
                    continue
                elif args[0] in derivatives:
                    print(args[0] + " : " + str(derivatives[args[0]]))
                    continue
                elif args[0] in strategies:
                    print(args[0] + " : " + strategies[args[0]].verbose())
                    continue
                else:
                    print(STR.ERR_NAME_UNKNOWN)
                    continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["show"])

        elif cmd == "set":
            if len(args) == 2 and args[0] in variables and isfloat(args[1]):
                variables[args[0]] = round(float(args[1])) if args[0] == "n" else float(args[1])
                continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["set"])

        elif cmd == "stock":
            if len(args) >= 1 and name_taken(args[0]):
                print(STR.ERR_NAME_TAKEN)
                continue
            if len(args) == 1:
                try:
                    data = get_price_and_vol(args[0])
                except:
                    print(STR.ERR_TICKER_NON_EXISTANT)
                    continue
                new_stock = Stock(data[0], data[1], name=args[0])
                stocks[args[0]] = new_stock
                print(STR.STOCK_SUCCESS)
                continue
            if len(args) == 3 and isfloat(args[1]) and isfloat(args[2]):
                new_stock = Stock(float(args[1]), float(args[2]), name=args[0])
                stocks[args[0]] = new_stock
                print(STR.STOCK_SUCCESS)
                continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["stock"])

        elif cmd == "deriv":
            if len(args) >= 1 and name_taken(args[0]):
                print(STR.ERR_NAME_TAKEN)
                continue
            if len(args) == 4:
                # Barriers
                name, type_deriv, deriv_id, barrier = args[0], args[1], args[2], float(args[3])
                if deriv_id not in derivatives:
                    print(STR.ERR_UNDERLYING)
                    continue
                if type_deriv in ("up_out", "up_in", "down_out", "down_in"):
                    new_deriv = None
                    if type_deriv == "up_out":
                        new_deriv = BarrierUpOut(derivatives[deriv_id], barrier, name=name)
                    if type_deriv == "up_in":
                        new_deriv = BarrierUpIn(derivatives[deriv_id], barrier, name=name)
                    if type_deriv == "down_out":
                        new_deriv = BarrierDownOut(derivatives[deriv_id], barrier, name=name)
                    if type_deriv == "down_in":
                        new_deriv = BarrierDownIn(derivatives[deriv_id], barrier, name=name)
                    derivatives[name] = new_deriv
                    print(STR.DERIV_SUCCESS)
                    continue
            if len(args) == 5:
                # vanilla, asian, binary
                name, type_deriv, underlying_id, strike, dte = args[0], args[1], args[2], float(args[3]), int(args[4])
                if underlying_id not in stocks:
                    print(STR.ERR_UNDERLYING)
                    continue
                if type_deriv in ("call", "put", "asian_call", "asian_put", "binary_call", "binary_put"):
                    new_deriv = None
                    if type_deriv == "call":
                        new_deriv = Call(stocks[underlying_id], strike, dte, name=name)
                    if type_deriv == "put":
                        new_deriv = Put(stocks[underlying_id], strike, dte, name=name)
                    if type_deriv == "asian_call":
                        new_deriv = AsianCall(stocks[underlying_id], strike, dte, name=name)
                    if type_deriv == "asian_put":
                        new_deriv = AsianPut(stocks[underlying_id], strike, dte, name=name)
                    if type_deriv == "binary_call":
                        new_deriv = BinaryCall(stocks[underlying_id], strike, dte, name=name)
                    if type_deriv == "binary_put":
                        new_deriv = BinaryPut(stocks[underlying_id], strike, dte, name=name)
                    derivatives[name] = new_deriv
                    print(STR.DERIV_SUCCESS)
                    continue
            if len(args) == 6:
                # binary + notional
                name, type_deriv, underlying_id, strike, dte, notional \
                    = args[0], args[1], args[2], float(args[3]), int(args[4]), float(args[5])
                if underlying_id not in stocks:
                    print(STR.ERR_UNDERLYING)
                    continue
                if type_deriv in ("binary_call", "binary_put"):
                    new_deriv = None
                    if type_deriv == "binary_call":
                        new_deriv = BinaryCall(stocks[underlying_id], strike, dte, notional, name=name)
                    if type_deriv == "binary_put":
                        new_deriv = BinaryPut(stocks[underlying_id], strike, dte, notional, name=name)
                    derivatives[name] = new_deriv
                    print(STR.DERIV_SUCCESS)
                    continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["deriv"])

        elif cmd == "strat":
            if len(args) >= 1 and name_taken(args[0]):
                print(STR.ERR_NAME_TAKEN)
                continue
            if len(args) == 2:
                if args[1] not in stocks:
                    print(STR.ERR_UNDERLYING)
                    continue
                new_strat = Strategy(stocks[args[1]])
                strategies[args[0]] = new_strat
                print(STR.STRAT_SUCCESS)
                continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["strat"])

        elif cmd == "add":
            is_short = False
            if len(args) == 3 and args[2] == "short":
                args = args[:2]
                is_short = True
            if len(args) == 2:
                strat, deriv = args
                if (strat not in strategies) or (deriv not in derivatives):
                    print(STR.ERR_NAME_UNKNOWN)
                    continue
                check = strategies[strat].add_leg(derivatives[deriv], is_short)
                if check:
                    print(STR.ADD_SUCCESS)
                    continue
                else:
                    print(STR.ERR_ADD)
                    continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["add"])

        elif cmd == "rem":
            is_short = False
            if len(args) == 3 and args[2] == "short":
                args = args[:2]
                is_short = True
            if len(args) == 2:
                strat, deriv = args
                if (strat not in strategies) or (deriv not in derivatives):
                    print(STR.ERR_NAME_UNKNOWN)
                    continue
                check = strategies[strat].rem_leg(derivatives[deriv], is_short)
                if check:
                    print(STR.REM_SUCCESS)
                    continue
                else:
                    print(STR.ERR_REM)
                    continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["rem"])

        elif cmd == "del":
            if len(args) == 1:
                name = args[0]
                if name in stocks:
                    del stocks[name]
                    continue
                if name in derivatives:
                    del derivatives[name]
                    continue
                if name in strategies:
                    del strategies[name]
                    continue
                print(STR.ERR_NAME_UNKNOWN)
                continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["del"])

        elif cmd == "price":
            if len(args) == 1:
                name = args[0]
                if name in stocks:
                    print(STR.PRICE_STOCK + name + " : " + str(stocks[name].price))
                    continue
                if name in derivatives:
                    print(STR.PRICE_DERIV + name + " : " + str(monte_carlo(derivatives[name],
                                                               riskfree=variables["r"], n=variables["n"])))
                    continue
                if name in strategies:
                    print(STR.PRICE_STRAT + name + " : " + str(monte_carlo_strategy(strategies[name],
                                                               riskfree=variables["r"], n=variables["n"])))
                    continue
                print(STR.ERR_NAME_UNKNOWN)
                continue
            print(STR.ERR_INCORRECT_USAGE + STR.USAGE["price"])

        elif cmd == "quit":
            print(STR.QUIT)
            confirm = input("> ")
            if confirm == STR.QUIT_CONFIRM:
                break

        else:
            print(STR.ERR_UNKNOWN_CMD)
