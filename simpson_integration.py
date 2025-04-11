import numpy as np


def simpson_int(f,b,a,n):
    ''' Let f(x) be a function well defined in the closed range [a,b] and 
    we integrate the function in the interval a to b, with n(even) grids'''

    interval = (b-a)/n
    int_sum = 0
    factor = interval/3

    for i in range(2,n+1):

        x = a + (i-1)*interval
        if i % 2 == 0: # to check if the term is x_(odd)
            int_sum = int_sum+4*f(x)
        else:
            int_sum = int_sum + 2*f(x)

    return factor*(int_sum + f(a) + f(b))  # adding f(x0) and f(xn)

f = lambda x: np.exp(-x**2)

integration_f = simpson_int(f,1,0,10)

print(f"The result of integration is : {integration_f}")