
class Primes:
# Use imperative programming to display all the prime numbers within an interval
    prime_nums = []

    def primes_between(self, lower, upper):
        for num in range(lower, upper + 1):
        # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    self.prime_nums.append(num)

    def print_prime_nums(self):\
        print("Primes are", self.prime_nums)


if __name__ == "__main__":
    '''Value for testing'''
    p = Primes()
    p.primes_between(1,100)
    p.print_prime_nums()

