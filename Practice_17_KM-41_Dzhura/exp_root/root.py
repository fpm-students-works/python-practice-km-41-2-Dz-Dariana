import math
def root2(i):
    if i < 0:
        raise ValueError('Число має бути додатнім')
    return math.sqrt(i)
def root3(i):
    return i ** (1/3)