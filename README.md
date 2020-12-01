# An option strategy pricer
EDHEC Business school - 2020 - Python for finance


## Usage

In this part, we will have a look first on the object, then on the functions. Please have a look on the example notebook to see those class in a simple use case.

### Financial objects

This object represents a stock.
```python
Class Stock(price : float, vol : float)
```

This abstract class will define the architecture of the derivatives. Each derivative has a particular payoff method that returns a float.
```python
Class Derivatives(underlying: Stock, strike: float, dte: int) 
@abstractmethod
def payoff(path) -> float:
```

This object represents a call.
```python
Class Call(underlying: Stock, strike: float, dte: int)
```

This object represents a put.
```python
Class Put(underlying: Stock, strike: float, dte: int)
```

This object represents a binary call. The notional is set to 1 by default.
```python
Class BinaryCall(underlying: Stock, strike: float, dte: int, notional=1)
```

This object represents a binary put. The notional is set to 1 by default.
```python
Class BinaryPut(underlying: Stock, strike: float, dte: int, notional=1)
```


This object represents an asian call. The notional is set to 1 by default.
```python
Class AsianCall(underlying: Stock, strike: float, dte: int)
```

This object represents an asian call.
```python
Class AsianCall(underlying: Stock, strike: float, dte: int)
```


This object represents an asian put.
```python
Class AsianPut(underlying: Stock, strike: float, dte: int)
```


This object represents a barrier up out.
```python
Class BarrierUpOut(option: Derivative, barrier: float)
```

This object represents a barrier down out.
```python
Class BarrierDownOut(option: Derivative, barrier: float)
```

This object represents a barrier up in.
```python
Class BarrierUpIn(option: Derivative, barrier: float)
```

This object represents a barrier down in.
```python
Class BarrierDownIn(option: Derivative, barrier: float)
```

### Strategy object

This object represents the strategy. 
```python
Class Strategy(underlying: Stock)
```
It has two methods that create and remove a leg for a given strategy. To short, `is_short` has to be set `True` when the leg is added.
```python
def add_leg(derivative, is_short=False)
def rem_leg(derivative, is_short=False)
```

### Functions

This function returns the price and the volatility for a given ticker using yahoo's daily database. By default, `start = '2005-1-1'` and `end = '2020-12-1'` as it stands for yesterday. 
Those dates must be strings and follow the format `yyyy-mm-dd`.
```python
def get_price_and_vol(ticker: str, start = '2005-1-1', end = datetime.date.today().strftime("%Y-%m-%d")):
```

This function returns the present value of a given derivative. `n=10000` by default but it can be modified by the user on the menu.
```python
def monte_carlo(derivative: Derivative, riskfree: float, n=BASE_ITERATIONS):
```

The following function returns the present value of a strategy. As on the prior function, `n=10000` by default but it can be modified by the user.
```python
def monte_carlo_strategy(strategy: Strategy, riskfree: float, n=BASE_ITERATIONS):
```

The following function computes the Monte Carlo path for a given underlying. It is used by the previous functions to compute the present value.
```python
def make_path(stock: Stock, dte: int, riskfree: float):
```

