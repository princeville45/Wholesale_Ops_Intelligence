def calculate_inventory_turnover(cost_of_goods_sold, beginning_inventory, ending_inventory):
    """Calculates the Inventory Turnover Ratio and Days Sales in Inventory (DSI)."""
    average_inventory = (beginning_inventory + ending_inventory) / 2
    if average_inventory == 0: return 0, 0
    turnover_ratio = cost_of_goods_sold / average_inventory
    dsi = 365 / turnover_ratio if turnover_ratio != 0 else 0
    return round(turnover_ratio, 2), round(dsi, 2)