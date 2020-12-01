# An option strategy pricer
EDHEC Business school - 2020 - Python for finance


## Usage

In this part, we will have a look first on the object, then on the functions. Please have a look on the example notebook to see those class in a simple use case.

### Objects

The object are stored in data_structures.py.

This object represents a stock.
```python
Class Stock(price : float, vol : float)
```

This abstract class will define the architecture of the derivatives. Each derivative has a particular payoff method that returns a float.
```python
Class Derivatives(underlying: Stock, strike: float, dte: int) 
@abstractmethod
def payoff(self, path) -> float:
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







