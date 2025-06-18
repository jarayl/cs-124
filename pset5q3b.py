from decimal import Decimal, getcontext
from math import factorial

def binomial_coefficient(n, i):
    # Compute the binomial coefficient using Decimal for high precision without factorials
    # This is a more efficient approach especially for large n and x
    coeff = Decimal(1)
    for x in range(i):
        coeff *= Decimal(n - x) / Decimal(x + 1)
    return coeff

def probability(n, m, k):
    probability_sum = Decimal(0)
    for i in range(16):
        probability_sum += binomial_coefficient((n*k), i) * (Decimal(1)/Decimal(m))**i * (Decimal(1)-(Decimal(1))/Decimal(m))**((n*k)-i)

    # Subtract the cumulative probability from 1 to get the probability of exceeding k
    return Decimal(1) - probability_sum

# Example usage with large values of n
n = 100000 # Replace with actual number of trials
m = 8*n     # Replace with actual number of success states
k = 5    
p = probability(n, m, k)
print(p)
print(m*p)
