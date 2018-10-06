# (20 points) Factoring of integers. Write a program that asks the user for an integer and 
# then prints out all its factors. 
# For example, when the user enters 150, the program should print 2 3 5 5

def factor(n):
    """
    Input an integer and the factor function will print out the given number's factors.
    """
    i = 0
    for i in range(n):
        i += 1
        result = n / i
        if result % i == 0:
            print(i)
        else:
            result = n / (i+1)
            if result % i == 0:
                print(i)

print(factor(150))



