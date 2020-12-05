import math
#import numpy as np
def solve(n):
    a, a_squared = 1,1
    while a <= n:
        if is_square(a_squared+n):
            return a_squared
        a +=1
        a_squared = pow(a,2)
    return -1

def is_square(integer):
    return math.sqrt(integer).is_integer()
