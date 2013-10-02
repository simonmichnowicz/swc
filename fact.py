import doctest

def factorial(n):
    """
>>> factorial(0)
1
>>> factorial(1)
1
>>> factorial(2)
2
>>> factorial(3)
6

    """
    # ...do something...
    if (n<=1):
        return 1
    else:
        return n*factorial(n-1)
        
        
def fib(n):
    """
>>> fib(3)
3
>>> fib(4)
5
"""
    if (n==1):
        return 1
    if (n==2):
        return 2
    return  fib(n-1) + fib(n-2)
    
def facttest():
    doctest.testmod()
    
if __name__ == "__main__":
    doctest.testmod()
"""
    print "Hello"

    print "Fact 2 is ",factorial(2)
    print "Fact 2 is ",factorial(2)
    print "Fact 3 is ",factorial(3)
    print "Fact 5 is ",factorial(5)
    print "Fact 10 is ",factorial(10)
    print "Fib 4 is ",fib(4)
    """
