def caching_fibonacci():
    # Create an empty dictionary for caching
    cache = {}
    
    def fibonacci(n):
        # Base cases
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Check if the value is already in the cache
        if n in cache:
            return cache[n]
        
        # Calculate the Fibonacci number and store it in the cache
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Return the result
        return cache[n]
    
    # Return the inner function fibonacci
    return fibonacci

# Get the fibonacci function
fib = caching_fibonacci()

# Use the fibonacci function to calculate Fibonacci numbers
print(fib(10))  # Outputs 55
print(fib(15))  # Outputs 610