#https://www.codewars.com/kata/product-of-consecutive-fib-numbers/train/python

def fib_products(prod):
    '''
    Given a number, 'prod', find two fibonacci numbers such that f(n) * f(n+1) = prod.

    inputs:
    prod - int

    outputs:
    lst - list of form [f1, f2, found] where:
        f1 - int, lower of the two fibonacci factors
        f2 - int, higher of the two fibonacci factors
        found - bool, whether or not the input is a fibonacci product
    If no factors can be found then f1 and f2 will be the smallest two fibonacci numbers such that f1*f2 > prod

    fibonacci sample:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
    '''

    #initialize first fibonacci numbers
    f1 = 0
    f2 = 1

    #initialize first product
    p = f1 * f2

    #run until product passes input
    while p <= prod:
        #if product matches input ...
        if p == prod:
            # ... return current fibonacci numbers and True
            return [f1, f2, True]
        # otherwise, increment to the next fibonacci numbers and check their product
        f1, f2 = f2, (f1 + f2)
        p = f1 * f2
    #return the fibonacci numbers and False if prod is not a fibonacci product
    return [f1, f2, False]
