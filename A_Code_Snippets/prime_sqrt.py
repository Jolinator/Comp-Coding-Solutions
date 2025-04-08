# Computes primes until sqrt(n1) after which any n2 below n1 is very fast,
# To know if n2 is prime, checks only if it is not divisible by primes until sqrt(n1) for any n2<n1
# after computing all primes until sqrt(n1), prime(n2) is O(num_of_primes(sqrt(n1)))



#prime(99999) is slow compared to normal prime checking because it computes all primes until sqrt(99999) = 316
#prime(99997) after prime(99999) very fast compared to normal prime checking O(num_of_primes(316)) 
# with OSPACE(num_of_primes(316))


primes = [2,3]


def next_prime():
    found_prime = False
    itr = primes[-1] + 2
    
    while not found_prime:

    
        for x in primes:
            if x*x > itr:
                found_prime = True
                primes.append(itr)

                break
            if itr % x == 0:
                break
        itr += 2



def prime(n):

    latest = primes[-1]
    while latest * latest <= n:
        next_prime()
        latest = primes[-1]

    for x in primes:
        if x*x > n:
            break
        if n % x == 0:

            return False


    return True

import timeit
print(timeit.timeit("prime(99999999999)", globals=globals(), number=1))
print(timeit.timeit("prime(99999999997)", globals=globals(), number=1))