# (20 points) Factoring of integers. Write a program that asks the user for 
# an integer and then prints out all its factors. 
# For example, when the user enters 150, the program should print 2 3 5 5

def factor(n):
    """
    Input an integer and the factor function will print 
    out the given number's factors.
    """
    i = 2
    while n > 0:            # while will be infinite without redefining n = n/i
        if n % i == 0:      # if n / i provides no remaider
            print(i)
            n = n / i       # redefine n to continue loop to find other factors
        else:
            i += 1

print(factor(150))