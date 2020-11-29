from abc import abstractmethod
"""
This file contains the data structures used in the program.
"""


class Instrument:
    @abstractmethod
    def payoff(self, price: float) -> float:
        """
        Function that gives the payout of the instrument
        """
        pass


class Stock(Instrument):
    """
    ticker: Stock ticker
    price: Last price of the stock
    vol: last volatility of the stock
    """
    def __init__(self, price: float, vol: float):
        self.price = price
        self.vol = vol

    def payoff(self, closing_price: float) -> float:
        return closing_price - self.price


class Call(Instrument):
    """
    stock: The underlying
    strike: Strike of the option
    dte: Days until expiry
    """
    def __init__(self, stock: Stock, strike: float, dte: int):
        self.strike = strike
        self.dte = dte
        super().__init__(stock)

    def payoff(self, closing_price):
        return max(.0, (closing_price-self.strike)*100)


class Put(Instrument):
    """
    stock: The underlying
    strike: Strike of the option
    dte: Days until expiry
    """
    def __init__(self, stock: Stock, strike: float, dte: int):
        self.strike = strike
        self.dte = dte
        super().__init__(stock)

    def payoff(self, closing_price):
        return max(.0, (self.strike-closing_price)*100)


####################
#    STRATEGIES    #
####################


class Strategy:
    """
    A strategy consists of any number of instruments traded as a single block.
    """
    def __init__(self):
        self.legs = list()

    def add_leg(self, instrument, is_short=False):
        self.legs.append((instrument, is_short))
        return True

    def rem_leg(self, instrument, is_short=False):
        if (instrument, is_short) in self.legs:
            self.legs.remove((instrument, is_short))
            return True
        return False
