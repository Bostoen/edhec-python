from code.data_structures import *
"""
This file contains the functions that do the necessary work.
"""
BASE_MONTE_CARLO_SIZE = 1000


def monte_carlo_instrument(instrument: Instrument, n=BASE_MONTE_CARLO_SIZE) -> float:
    """
    Approximate the price of an instrument via Monte Carlo
    """
    pass


def monte_carlo_strategy(strategy: Strategy, n=BASE_MONTE_CARLO_SIZE) -> float:
    """
    Approximate the price of a strategy via Monte Carlo
    """

    # idée en pseudocode:
    #
    # total = 0
    # for leg in strategy:
    #    total += leg.instrument.payoff() * leg.amount
    #
    # Ainsi donc si tu es short un call, long deux puts, short un autre call, tu auras:
    #    call_1.payoff() * -1
    #    + put_1.payoff() * 2
    #    + call_2.payoff() * -1
    pass
