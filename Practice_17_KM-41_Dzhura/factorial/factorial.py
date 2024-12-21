def fact(x):
    if x < 0 or not isinstance(x, int):
        raise ValueError('It must be a positive integer')
    else:
        factorial = 1
        for i in range(1, x + 1):
            factorial *= i
        return factorial
