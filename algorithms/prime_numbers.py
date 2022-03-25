# Use imperative programming to display all the prime numbers within an interval

def primes_between(lower, upper):
    for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)


if __name__ == "__main__":
    '''Value for testing'''

    print("Primes in range [0,100]", primes_between(0,100))