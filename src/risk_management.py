def validate_order(order_data):
    """
    Validate an order before execution.
    """
    required_fields = ["symbol", "quantity", "side"]
    
    for field in required_fields:
        if field not in order_data:
            return False, f"Missing required field: {field}"
    
    if order_data["quantity"] <= 0:
        return False, "Quantity must be positive"
    
    return True, "Valid order"

def calculate_position_size(account_balance, risk_percentage, stop_loss):
    """
    Calculate position size based on risk parameters.
    """
    if stop_loss <= 0:
        return 0
    
    risk_amount = account_balance * risk_percentage
    return risk_amount / stop_loss
