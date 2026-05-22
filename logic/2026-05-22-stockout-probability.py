import math

def poisson_stockout_probability(lambda_demand, stock_level):
    """Calculates the probability of a stock-out using Poisson distribution for demand."""
    # lambda_demand: average demand per period
    # stock_level: current units available
    prob_sufficient = 0
    for i in range(stock_level + 1):
        prob_sufficient += (math.exp(-lambda_demand) * (lambda_demand**i)) / math.factorial(i)
    
    return round(1 - prob_sufficient, 4)