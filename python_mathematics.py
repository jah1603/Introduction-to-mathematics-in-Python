# ***Types of numbers***

print(type(3))

print(type(4/3))

print(type(3.5))

print((type(1.0+3.5j)))

5 + 3.5

2**3

# ***All computer algebra typically respects the PEMDAS rule***

#Parentheses then exponentiation then multiplication then division then additioin then subtraction
5*5+5

5*(5+5)

2**2*2 + 2**(2*2)

2/(4/2)

***Fractions***

from fractions import Fraction

f3_2 = Fraction(3,2)

f6_4 = Fraction(6,4)

f12_15 = Fraction(12,15)

f3_2 == f6_4

f3_2 * f6_4

1/f3_2

3*f3_2

f3_2 + f6_4

float(f3_2 +f6_4)

Fraction('0.12213')

Fraction(0.12213)

Fraction(0.1)

import math
pi_fraction = Fraction(math.pi)
print(pi_fraction)

# ***Arbitrary Integer Precision***

# Python has fantastic integer arithmetic. It can represent integers to arbitrary

a_int = 3**100
type(a_int)

b_int = 3**100 + 1
type(b_int)

print(b_int - a_int)

type(b_int - a_int)

***And now floats :-(***

a_float = 3.0**100.0

b_float = 3.0**100.0 + 1.0

print(b_float - a_float)

a = 3.0
# Take the 1000th root
root = a ** (1/1000)
print(root)



root**1000

root**1000 == 3.0

def are_floats_equal(a, b, delta):
    if a == 0 or b == 0:
        #delta is an absolute error
        return max( abs(a), abs(b) ) <= delta
    else:
        #delta is a fractional error
        return  abs( (a-b) / max( abs(a), abs(b) ) ) <= delta

x = 0.0
y = 1E-12
print(are_floats_equal(x,y,1E-10))

x = 9.1
y = 10.4
print(are_floats_equal(x,y,1E-10))

# **Arithmetic operations in 'perfect' maths are 'associative'***

# e.g. ( a + b ) + c = a + (b + c)

x = (0.1 + 0.2) + 0.3
y = (0.1) + (0.2 +0.3)
x == y

# In this case the associative rule does not hold as it would in 'real' mathematics.

print('%.20f' %x)

print('%.20f' %y)

x = (0.5 + 0.25) + 0.125
y = (0.5) + (0.25 + 0.125)
x == y

# When we use numbers which can be represented in binary then the associative rule does hold.

# ***Are numbers commutative?***
# e.g. a x b x c = b x a x c

x = 0.1 * 0.2 * 0.3
y = 0.3 * 0.2 * 0.1
x == y

x = 0.125 * 0.5 * 0.25
y = 0.25 * 0.5 * 0.125
x == y

import bitstring
f0p3 = bitstring.BitArray(float = 0.3, length = 32)
print(f0p3.bin)

import math
def simple_factorise(x):
    factors = []
    for number in range( x, 0, -1 ):
        if x % number == 0:
            factors.append(number)
    return factors

print(simple_factorise(27))

%time simple_factorise(100001)

%time simple_factorise(125)

def slightly_better_factorise(x):
    factors = []
    low_limit = math.floor( math.sqrt(x) ) - 1
    for number in range( x, low_limit, -1 ):
        if x % number == 0:
            factors.append(number)
            cofactor = int( x / number )
            if cofactor != number:
                factors.append(cofactor)
        return factors

%time slightly_better_factorise(100001)

def even_better_factorise(x):
    factors = []
    high_limit = math.ceil( math.sqrt ( x ) ) + 1
    for number in range( 1, high_limit, 1 ):
        if x % number == 0:
            factors.append(number)
            cofactor = int( x / number )
            if cofactor != number:
                factors.append(cofactor)
        return factors

%time even_better_factorise(100001)

def prime_factors(x):
    x = int(x)
    factors = []
    high_limit = math.ceil( math.sqrt(x) ) + 1
    # Try two's first
    while x % 2 == 0:
        x = int( x / 2 )
        factors.append(2)
    #At this point there are no remaining even factors. Let's start at 3, trying only odd factors
    for trial_factor in range( 3, high_limit, 2 ):
        while x  % trial_factor == 0:
            x = int( x/ trial_factor )
            factors.append(trial_factor)
        if x == 1:
            break
    if x > 2:
        factors.append(x)
    return factors

prime_factors(64)

prime_factors(117)

prime_factors(119)

prime_factors(7)
