# An option strategy pricer
EDHEC Business school - 2020 - Python for finance


## Usage

In this part, we will have a look first on the object, then on the functions.

### Objects

The object are stored in data_structures.py.

This object represents a stock.
```python
Class Stock(price : float, vol : float)
```

This abstract class will define the architecture of the derivatives.
```python
Class Derivatives(underlying: Stock, strike: float, dte: int) 
@abstractmethod
```

This object represents a call.
```python
Class Call(underlying: Stock, strike: float, dte: int)
```


This object represents a put.
```python
Class Put(underlying: Stock, strike: float, dte: int)
```



- `Class BinaryCall(underlying: Stock, strike: float, dte: int, notional=1)`











