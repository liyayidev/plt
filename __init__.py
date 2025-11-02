from .src.indicators import calculate_indicator, generate_random_signal
from .src.risk_management import validate_order, calculate_position_size

def run_strategy(market_data):
    """
    Main strategy function that uses custom modules.
    """
    prices = market_data.get("prices", [])
    indicator_value = calculate_indicator(prices)
    
    signal = generate_random_signal()
    
    return {
        "action": signal,
        "indicator_value": indicator_value,
        "timestamp": __import__("datetime").datetime.now().isoformat()
    }

def execute_trade(order_data):
    """
    Execute a trade with validation.
    """
    is_valid, message = validate_order(order_data)
    
    if not is_valid:
        return {"status": "ERROR", "message": message}
    
    # Simulate trade execution
    return {
        "status": "SUCCESS",
        "order_id": __import__("random").randint(100000, 999999),
        "executed_at": __import__("datetime").datetime.now().isoformat()
    }
