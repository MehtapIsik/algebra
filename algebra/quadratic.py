def poly_old(*args):
    """
    f(x) = a * x + b * x**2
	
    *args = (x, a, b)
    """

    # Unpack arguments
    x = args[0]
    a = args[1]
    b = args[2]
	
    print(args)
	
    fx = a*x + b*(x**2)
	
    return fx


def poly(*args):
    """
    f(x) = a * x + b * x**2 + c * x**3 + ...

    *args = (x, a, b, ...)
    """

    # Add a warning for something potentially incorrect
    if len(args) == 1:
        raise Exception("You have only entered a value for x, and no coefficients.") 
	
    # Unpack arguments
    x = args[0] # The x value 
    coef = args[1:] # everything after the first argument
	
    # Calculate using a loop
    result = 0
    for power,c in enumerate(coef):
        result += c * (x ** (power+1))

    print(args)
	
    return result
