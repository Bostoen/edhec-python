# Python Interactive Monte-carlo Pricer
EDHEC Business school - 2020 - Python for finance.  
For academic purposes.

## Introduction

This python software allows Monte-Carlo pricing of 10 different kinds of derivatives on underlying equities. Additionally, it expands on the assignment by offering modular strategy pricing: derivatives can be bundled into strategies which are priced in a single Monte-Carlo simulation.

In case of any trouble while using PIMP, please email hector.bostoen@edhec.com

## Usage

PIMP is run from the command line, and comes equipped with a "help" command to guide users. To start, run "main.py". An example usage notebook is also provided to showcase the software's internal workings.

### Commands

Commands and syntax. Type "help <command>" for specific usage and parameters.  
add    : Add a leg to a strategy  
del    : Delete a Stock, Derivative or Strategy  
deriv  : Create a new derivative  
help   : Program help  
list   : List all Stocks, Derivatives and Strategies in memory  
price  : Return the price of a given derivative or strategy  
quit   : Quit  
rem    : Remove a leg from a strategy  
set    : Set environment variables  
show   : View the details of a Stock, Derivative or Strategy  
stock  : Create a new stock  
strat  : Create a new strategy, or modify an existing one  
types  : Full list of possible derivative types  
vars   : Show current values for environment variables  

### Workflow

The recommended workflow for PIMP is straightforward:  
1) Create one (or more) underlying Stock(s)  
2) Create Derivatives on an underlying  
3) Combine Derivatives into Strategies  
Repeat for as many Stocks, Derivatives and Strategies as desired. At any point, one can use the "price" command to calculate the price of an instrument. This command will execute a Monte-Carlo simulation for Derivatives and Strategies.

We encourage you to try it out for yourself. Make use of "help <command>" whenever a command is unclear.

## Internal Workings

The software for PIMP consists of three major sections: the data structures, the functions and the interface.

### Data Structures

Each instrument is instanciated as a separate class within memory.

This object represents a stock. Stocks are used as underlying equities for derivatives.
```python
Class Stock(price: float, vol: float)
```

This abstract class will define the architecture of the derivatives. Each derivative must define the payoff method, which returns the payoff at maturity, and is used in Monte-Carlo pricing.
```python
Class Derivatives(underlying: Stock, strike: float, dte: int) 
@abstractmethod
def payoff(path) -> float:
```

The first two derivatives are vanilla calls and puts.
```python
Class Call(underlying: Stock, strike: float, dte: int)

Class Put(underlying: Stock, strike: float, dte: int)
```

Further, binary options which payout either a notional amount or 0. The notional is set to $1 by default.
```python
Class BinaryCall(underlying: Stock, strike: float, dte: int, notional=1)

Class BinaryPut(underlying: Stock, strike: float, dte: int, notional=1)
```
Asian options pay out based on the average price of the security over a predefined period, rather than the price at maturity. This means that their price is path-dependant, which means the whole path must be simulated in Monte-Carlo to accurately determine their price.  
For this implementation, the average is always computed as the daily arithmetic average from purchase until expiry.
```python
Class AsianCall(underlying: Stock, strike: float, dte: int)

Class AsianPut(underlying: Stock, strike: float, dte: int)
```

Finally, we support four types of barrier options:  
* Up-and-out: The spot price starts below the barrier. If it goes above, the option becomes void.  
* Down-and-out: The spot price starts above the barrier. If it goes below, the option becomes void.  
* Up-and-in: The spot price starts below the barrier. It must go above for the option to become active.  
* Down-and-in: The spot price starts above the barrier. It must go below for the option to become active.  

Barriers can be placed on any other derivative, including exotic options, or even other barrier options. This way, multiple barriers could be added to a single derivative.
```python
Class BarrierUpOut(option: Derivative, barrier: float)

Class BarrierDownOut(option: Derivative, barrier: float)

Class BarrierUpIn(option: Derivative, barrier: float)

Class BarrierDownIn(option: Derivative, barrier: float)
```

As mentioned, PIMP provides functionality for creating strategies. These combine derivatives together as legs and can be used, for example, to create butterflies, iron condors, straddles, etc. Strategies are priced efficiently by executing only one Monte-Carlo simulation rather than one for each leg.
```python
Class Strategy(underlying: Stock)
```

It has two methods that create and remove a leg for a given strategy. Short legs can also be added, and their price will be deducted from the overall price of the strategy (since they provide a net credit).
```python
def add_leg(derivative, is_short=False)
def rem_leg(derivative, is_short=False)
```

### Functions

PIMP automatically retrieves price and volatility data for stocks if only a ticker is provided. This function gets that data from Yahoo Finance.
```python
def get_price_and_vol(ticker: str, start = '2005-1-1', end = datetime.date.today().strftime("%Y-%m-%d")):
```

The main functionality of the software is contained within the Monte-Carlo simulation functions. By default, PIMP runs 10^4 iterations, but this setting can be changed. The structure of these functions is fairly straightforward. Strategy pricing is done by a different function because all legs of the strategy are evaluated based on the same MC simulation. This provides the same statistical accuracy as running a separate simulation for each leg, but runs in O(n) as opposed to O(n\*l) (where n is the number of iterations and l the number of legs of the strategy).
```python
def monte_carlo(derivative: Derivative, riskfree: float, n=BASE_ITERATIONS):

def monte_carlo_strategy(strategy: Strategy, riskfree: float, n=BASE_ITERATIONS):
```

For the Monte-Carlo simulation, price paths of the underlying are generated by this helper function.
```python
def make_path(stock: Stock, dte: int, riskfree: float):
```

