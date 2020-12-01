from abc import abstractmethod
import numpy as np
"""
This file contains the data structures used in the program.
"""


class Stock:
    def __init__(self, price: float, vol: float, name="Stock"):
        self.price = price
        self.vol = vol
        self.name = name

    def __str__(self):
        return "Stock (price = "+str(self.price)+", vol = "+str(self.vol)+")"


class Derivative:
    def __init__(self, underlying: Stock, strike: float, dte: int, name: str):
        self.underlying = underlying
        self.strike = strike
        self.dte = dte
        self.name = name

    @abstractmethod
    def payoff(self, path) -> float:
        """
        Function that gives the payout of the instrument
        """
        pass


class Call(Derivative):
    def __init__(self, underlying: Stock, strike: float, dte: int, name="Call"):
        super().__init__(underlying, strike, dte, name)

    def __str__(self):
        return "Call (underlying = "+self.underlying.name+", strike = "+str(self.strike)+", dte = "+str(self.dte)+")"

    def payoff(self, path):
        closing_price = path[self.dte - 1]
        return max(.0, (closing_price-self.strike))


class Put(Derivative):
    def __init__(self, underlying: Stock, strike: float, dte: int, name="Put"):
        super().__init__(underlying, strike, dte, name)

    def __str__(self):
        return "Put (underlying = "+self.underlying.name+", strike = "+str(self.strike)+", dte = "+str(self.dte)+")"

    def payoff(self, path):
        closing_price = path[self.dte - 1]
        return max(.0, (self.strike-closing_price))


class BinaryCall(Derivative):
    # Cash-or-nothing
    def __init__(self, underlying: Stock, strike: float, dte: int, notional=1., name="BinaryCall"):
        super().__init__(underlying, strike, dte, name)
        self.notional = notional

    def __str__(self):
        return "Binary Call (underlying = " + self.underlying.name + ", strike = " + str(self.strike) + \
               ", dte = " + str(self.dte) + ", notional = " + str(self.notional) + ")"

    def payoff(self, path):
        closing_price = path[self.dte - 1]
        return self.notional if closing_price > self.strike else 0


class BinaryPut(Derivative):
    # Cash-or-nothing
    def __init__(self, underlying: Stock, strike: float, dte: int, notional=1., name="BinaryPut"):
        super().__init__(underlying, strike, dte, name)
        self.notional = notional

    def __str__(self):
        return "Binary Put (underlying = " + self.underlying.name + ", strike = " + str(self.strike) + \
               ", dte = " + str(self.dte) + ", notional = " + str(self.notional) + ")"

    def payoff(self, path):
        closing_price = path[self.dte - 1]
        return self.notional if closing_price < self.strike else 0


class AsianCall(Derivative):
    # Fixed strike, daily arithmetic average
    def __init__(self, underlying: Stock, strike: float, dte: int, name="AsianCall"):
        super().__init__(underlying, strike, dte, name)

    def __str__(self):
        return "Asian Call (underlying = " + self.underlying.name + ", strike = " + str(self.strike) + \
               ", dte = " + str(self.dte) + ")"

    def payoff(self, path):
        average_price = np.mean(path[:self.dte - 1])
        return max(.0, (average_price-self.strike))


class AsianPut(Derivative):
    # Fixed strike, daily arithmetic average
    def __init__(self, underlying: Stock, strike: float, dte: int, name="AsianPut"):
        super().__init__(underlying, strike, dte, name)

    def __str__(self):
        return "Asian Put (underlying = " + self.underlying.name + ", strike = " + str(self.strike) + \
               ", dte = " + str(self.dte) + ")"

    def payoff(self, path):
        average_price = np.mean(path[:self.dte - 1])
        return max(.0, (self.strike-average_price))


class BarrierUpOut(Derivative):
    # spot price starts below the barrier level and has to move up for the option to be knocked out
    def __init__(self, option: Derivative, barrier: float, name="BarrierUpOut"):
        assert option.underlying.price < barrier
        super().__init__(option.underlying, option.strike, option.dte, name)
        self.option = option
        self.barrier = barrier

    def __str__(self):
        return "Up-And-Out (option = " + self.option.name + ", barrier = " + str(self.barrier) + ")"

    def payoff(self, path):
        for i in path:
            if i > self.barrier:
                return 0
        return self.option.payoff(path)


class BarrierDownOut(Derivative):
    # spot price starts above the barrier level and has to move down for the option to be knocked out
    def __init__(self, option: Derivative, barrier: float, name="BarrierDownOut"):
        assert option.underlying.price > barrier
        super().__init__(option.underlying, option.strike, option.dte, name)
        self.option = option
        self.barrier = barrier

    def __str__(self):
        return "Down-And-Out (option = " + self.option.name + ", barrier = " + str(self.barrier) + ")"

    def payoff(self, path):
        for i in path:
            if i < self.barrier:
                return 0
        return self.option.payoff(path)


class BarrierUpIn(Derivative):
    # spot price starts below the barrier level and has to move up for the option to become activated
    def __init__(self, option: Derivative, barrier: float, name="BarrierUpIn"):
        assert option.underlying.price < barrier
        super().__init__(option.underlying, option.strike, option.dte, name)
        self.option = option
        self.barrier = barrier

    def __str__(self):
        return "Up-And-In (option = " + self.option.name + ", barrier = " + str(self.barrier) + ")"

    def payoff(self, path):
        for i in path:
            if i > self.barrier:
                return self.option.payoff(path)
        return 0


class BarrierDownIn(Derivative):
    # spot price starts above the barrier level and has to move down for the option to become activated
    def __init__(self, option: Derivative, barrier: float, name="BarrierDownIn"):
        assert option.underlying.price > barrier
        super().__init__(option.underlying, option.strike, option.dte, name)
        self.option = option
        self.barrier = barrier

    def __str__(self):
        return "Down-And-In (option = " + self.option.name + ", barrier = " + str(self.barrier) + ")"

    def payoff(self, path):
        for i in path:
            if i < self.barrier:
                return self.option.payoff(path)
        return 0


####################
#    STRATEGIES    #
####################


class Strategy:
    """
    A strategy consists of any number of instruments on an underlying traded as a single block.
    """
    def __init__(self, underlying: Stock):
        self.underlying = underlying
        self.legs = list()
        self.dte = 0

    def __str__(self):
        return "Strategy (underlying = " + self.underlying.name + ")"

    def verbose(self):
        if len(self.legs) == 0:
            return str(self)
        string = str(self) + " consisting of"
        for leg in self.legs:
            string += "\n    "
            string += "short " if leg[1] else "long "
            string += str(leg[0])
        return string

    def add_leg(self, derivative, is_short=False):
        if derivative.underlying == self.underlying:
            self.dte = max(derivative.dte, self.dte)
            self.legs.append((derivative, is_short))
            return True
        return False

    def rem_leg(self, derivative, is_short=False):
        if (derivative, is_short) in self.legs:
            self.legs.remove((derivative, is_short))
            return True
        return False
