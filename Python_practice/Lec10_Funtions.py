# a function is block of code which only runs when it is called
# you can pass data, known as parameters, into a function.
# A function can return data as a result.
#in Python a function is defined using the def keyword

# def greet_user(name):
#     """Display a greeting message."""
#     print(f"Hello, {name}!")
    
# # Calling the function with a parameter
# greet_user("Alice")

def square(number):
    """Return the square of a number."""
    return number ** 2

# Calling the function and storing the result
result = square(5)

# squre using lambda function
square_lambda = lambda x: x ** 2
# Calling the lambda function
result_lambda = square_lambda(5)


def factorial(n):
    """Return the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the factorial function
result_factorial = factorial(5)

print(f"Square of 5: {result}")
print(f"Square of 5 using lambda: {result_lambda}") 
print(f"Factorial of 5: {result_factorial}")
# Function with default parameter
def greet(name="Guest"):
    """Display a greeting message with a default name."""
    print(f"Hello, {name}!")
    
    
x = lambda a, b: a + b
# Calling the function with a default parameter
print(x(5, 3))  # Output: 8