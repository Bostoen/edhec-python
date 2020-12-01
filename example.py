from code.functions import *
from scipy import stats
import matplotlib.pyplot as plt
"""
Contains example usage of the software.
"""
np.random.seed(4)

# First, we create an underlying stock. Let's use Apple: we set the price at $120 and volatility at 30%
aapl = Stock(120, 0.3)

# Now let's make a call on Apple expiring in 4 weeks (20 business days), $5 out of the money.
aapl_call = Call(aapl, 125, 20)

# We use monte carlo to price this option, with a riskfree rate of 3% (by default, we run 10^4 Monte Carlo iterations)
call_price = monte_carlo(aapl_call, riskfree=0.03)
print("Call price via MC: " + str(call_price))

# To check our result, we price the same option with the closed form Black-Scholes model
d1 = (np.log(aapl.price/aapl_call.strike) + (0.03 + 0.5*aapl.vol**2)*aapl_call.dte/252)\
     / (aapl.vol*np.sqrt(aapl_call.dte/252))
d2 = d1-aapl.vol*np.sqrt(aapl_call.dte/252)
call_price_bs = aapl.price*stats.norm.cdf(d1, 0.0, 1.0) - aapl_call.strike * np.exp(-0.03*aapl_call.dte/252)\
                *stats.norm.cdf(d2, 0.0, 1.0)
print("Call price via BS: " + str(call_price_bs))
error = abs(call_price-call_price_bs)
error_rel = error/call_price_bs*100
print("Error: " + str(error) + " or " + str(round(error_rel, 2)) + "%")

##############

# We can price some exotic options as well: let's try a binary put on apple, strike at 110 in 4 weeks
# with a payout of $1
aapl_binary = BinaryPut(aapl, 110, 20, notional=1)
binary_price = monte_carlo(aapl_binary, riskfree=0.03)
print("\nBinary put price: " + str(binary_price))

# One step further: let's create a barrier option. We start from our apple call, and turn it
# into an up-and-out option by adding a knockout barrier at $135. Intuition tells us that since
# this barrier severely caps out upside, this new option should be cheaper than our original call.
aapl_barrier = BarrierUpOut(aapl_call, 135)
barrier_price = monte_carlo(aapl_barrier, riskfree=0.03)
print("\nUp-and-out barrier call price: " + str(barrier_price))

##############

# Finally, let's build some strategies. As an example, we create a long call butterfly on Apple.
# This strategy consists of four legs: an ITM long call, two ATM short calls and an OTM long call.
aapl_butterfly = Strategy(aapl)
aapl_butterfly.add_leg(Call(aapl, 110, 20))                 # ITM Long leg
aapl_butterfly.add_leg(Call(aapl, 120, 20), is_short=True)  # ATM Short leg
aapl_butterfly.add_leg(Call(aapl, 120, 20), is_short=True)  # ATM Short leg
aapl_butterfly.add_leg(Call(aapl, 130, 20))                 # OTM Long leg

# Because the long call butterfly is a net debit position, we expect its price to be positive.
butterfly_price = monte_carlo_strategy(aapl_butterfly, riskfree=0.03)
print("\nLong call butterfly price: " + str(butterfly_price))

# This value is reasonably accurate, at time of writing (with apple at $119), this butterfly costs ~$3.8

# One more test: let us check the in-out parity of barrier options. The combination of an in and an out barrier
# option with otherwise identical characteristics should be equal to a vanilla option.
in_out_parity = Strategy(aapl)
in_out_parity.add_leg(BarrierUpIn(aapl_call, 130))
in_out_parity.add_leg(BarrierUpOut(aapl_call, 130))
parity_price = monte_carlo_strategy(in_out_parity, riskfree=0.03)
print("\nIn-out combo price: " + str(parity_price))
print("Difference with vanilla option: " + str(abs(parity_price-call_price)))

# This difference is just the expected monte-carlo error.

##############

# Below is a test for the monte-carlo path generator
# test = [make_path(Stock(120, 0.2), 2000, 0.03) for i in range(100)]
# for i in test:
#     plt.plot(i)
# plt.show()
