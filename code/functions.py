from code.data_structures import *
import numpy as np
import yfinance as yf
import datetime

"""
This file contains the functions that do the necessary work.
"""
BASE_ITERATIONS = 10**4


def get_price_and_vol(ticker: str, start='2005-1-1', end=datetime.date.today().strftime("%Y-%m-%d")):
    tickerData = yf.Ticker(ticker)
    tickerDf = tickerData.history(period='1d', start=start, end=end)
    last_price = tickerDf['Close'][-1] 
    tickerDf['returns'] = np.log(tickerDf['Close']/tickerDf['Close'].shift(-1))
    daily_vol = np.std(tickerDf['returns'])
    ann_vol = daily_vol * np.sqrt(252)
    return round(last_price,2), round(ann_vol,2)


def make_path(stock: Stock, dte: int, riskfree: float):
    t = np.arange(dte)          # time range in days
    T = t/252                   # time range in years
    vol = stock.vol

    noise = np.random.normal(size=dte)
    W = np.cumsum(noise)
    path = stock.price * np.exp((riskfree-0.5*vol**2)*T+vol/np.sqrt(252)*W)
    return path


def monte_carlo(derivative: Derivative, riskfree: float, n=BASE_ITERATIONS):

    # Make n paths for the underlying price
    total = 0
    for i in range(n):
        path = make_path(derivative.underlying, derivative.dte, riskfree)
        # Pass the path to the derivative and get the payoff
        total += derivative.payoff(path)

    # Get the mean future value
    FV = total / n

    # Discount to get present value
    PV = FV * np.exp(-riskfree*derivative.dte/252)
    return PV


def monte_carlo_strategy(strategy: Strategy, riskfree: float, n=BASE_ITERATIONS):

    # Make n paths for the underlying price
    totals = np.zeros(len(strategy.legs))
    for i in range(n):
        path = make_path(strategy.underlying, strategy.dte, riskfree)
        # Pass the path to the derivatives and get the payoffs
        # Negative if the leg is short
        payoffs = [-leg[0].payoff(path) if leg[1] else leg[0].payoff(path) for leg in strategy.legs]
        totals += payoffs

    # Get the mean future values
    FV = totals / n

    # Discount to get present values
    # This is split up in case different derivatives have different DTEs
    PV = FV * [np.exp(-riskfree*leg[0].dte/252) for leg in strategy.legs]
    return sum(PV)
