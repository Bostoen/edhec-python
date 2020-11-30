from code.data_structures import *
import numpy as np

"""
This file contains the functions that do the necessary work.
"""
variables = {"r": 0.05, "n": 50000}
np.random.seed(1)


# instrument: Instrument
def monte_carlo_instrument(instrument_vol, S0: float, month_to_maturity) -> float:
    """
    Approximate the price of an instrument via Monte Carlo
    """
    M = 12 #interval for discretization
    T = month_to_maturity
    
    def mcs(M,n):   
        dt = T / M
        S = np.zeros((M + 1, n))
        S[0] = S0
        rn = np.random.standard_normal(S.shape)
        for t in range(1, M+1):
            S[t]=S[t-1]*np.exp((variables['r']-instrument_vol**2/2)*dt+instrument_vol*np.sqrt(dt)*rn[t])
        return S
    
    S = mcs(M,variables['n'])
    print(S[-1].mean())
    print(S0*np.exp(variables['r']*T))
    C0 = np.exp(-variables['r'] * T)*np.maximum(S0 - S[-1],0).mean()
            
    return C0


def monte_carlo_strategy(strategy: Strategy) -> float:
    """
    Approximate the price of a strategy via Monte Carlo
    """    
    total = np.array([monte_carlo_instrument(xxxxxx,xxx,xxxx,xxx)*leg.amount for leg in strategy]).sum()
    
    # attention au short qui fera un résultat négatif sur le payoff ! 

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
    return total



test = monte_carlo_instrument(0.2, 100, 12)
print(test)
