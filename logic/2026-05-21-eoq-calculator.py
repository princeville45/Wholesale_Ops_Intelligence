import numpy as np

def calculate_eoq(annual_demand, ordering_cost, holding_cost_per_unit):
    """Calculates Economic Order Quantity (EOQ) to minimize total inventory costs."""
    if holding_cost_per_unit <= 0: return 0
    eoq = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost_per_unit)
    return round(eoq, 2)