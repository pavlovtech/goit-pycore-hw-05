import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    This function takes a string as input and returns a generator that yields all valid numbers
    in the text. Numbers are assumed to be clearly separated by spaces.
    """
    # Regular expression to find all numbers in the text
    pattern = re.compile(r'\b\d+\.\d+\b|\b\d+\b')
    
    # Find all matches in the text
    matches = pattern.findall(text)
    
    # Yield each match as a float
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    This function takes a text and a generator function as arguments and returns the sum
    of all numbers found by the generator function in the text.
    """
    # Use the generator function to get numbers and sum them up
    return sum(func(text))

# Example usage:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
