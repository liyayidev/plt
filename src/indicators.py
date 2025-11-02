import random
import cryptography

def calculate_indicator(prices):
    """
    Calculate a simple momentum indicator.
    """
    if len(prices) < 2:
        return 0
    
    return (prices[-1] - prices[0]) / prices[0]

def generate_random_signal():
    """
    Generate a random signal for testing.
    """
    return "BUY" if random.random() > 0.5 else "SELL"
