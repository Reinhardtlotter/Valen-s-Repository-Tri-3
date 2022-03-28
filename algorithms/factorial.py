
# Python code to demonstrate naive method
# to compute factorial

class Factor:

    def factorial(n):
        fact = 1
        
        for i in range(1,n+1):
            fact = fact * i
            
        print ("The factorial of " , n, " is : ",end="")
        print (fact)

    # Test Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 20
    for i in range(n):
        print("Factor (",i,") = ", Factor.factorial(i))