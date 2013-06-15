'''
Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The product
of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4

Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n,
starting with n = 0.
'''

def getPrimeSieve(limit):
    sieve = [True] * limit
    for n in xrange(3, int(limit**.5) + 1, 2):
        if sieve[n]:
            sieve[n*n::n*2] = [False] * ((limit-n*n-1) / (n * 2) + 1)
    sieve[4::2] = [False] * ((limit - 5) / 2 + 1)
    return sieve


def eq(n, a, b):
    return pow(n, 2) + a * n + b


def checkPrime(n):
    if n % 2 == 0:
        return False
    elif n < 0:
        return False
    elif n >= sieveLength:
        return False
    else:
        return sieve[n]


def countConsecutive(a, b):
    n = 0
    while checkPrime(eq(n, a, b)):
        n += 1
    return n


sieve = getPrimeSieve(10**4)
sieveLength = len(sieve)

maxConsec = 0
maxProduct = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        consec = countConsecutive(a, b)
        if consec > maxConsec:
            maxConsec = consec
            maxProduct = a * b
print maxProduct
