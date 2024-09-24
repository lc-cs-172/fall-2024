"""Graph the Aliquot sequence for positive integer n.

Try 6 (a perfect number), 95 (aspiring), 8 (deficient), 24 (abundant), 220
(amicable), and 276.
"""

import matplotlib.pyplot as plt

__author__ = 'Alain Kaegi'

def factors(n : int) -> list[int]:
    """Return a list of all factors (< n) of positive integer n."""
    factor_list = []
    i = 1
    while i < n:
        if n % i == 0:
            factor_list.append(i)
        i = i + 1
    return factor_list

def sum(xs : list[int]) -> int:
    """Return the sum of the list of integers."""
    s = 0
    i = 0
    while i < len(xs):
        s = s + xs[i]
        i = i + 1
    return s

def has_converged(sequence : list[int]) -> bool:
    """Return True when any of the following conditions hold:

    - the last element of the sequence is zero,
    - the sequence has at least 6 elements and the last two elements are the
      same as the previous pair"""
    if sequence[-1] == 0:
        return True
    if len(sequence) > 5 and sequence[-2:] == sequence[-4:-2]:
        return True
    return False

n = int(input("Enter a positive number: "))
max = n

sequence = [n]

plt.ylabel('The Aliquot sequence for ' + str(n))

while True:
    plt.plot(sequence, 'ro-')
    plt.xlim(-1, len(sequence))
    plt.ylim(-1, max + 1)
    plt.show(block = has_converged(sequence))
    plt.pause(0.5)

    if has_converged(sequence):
        break

    n = sum(factors(n))
    sequence.append(n)
    if n > max:
        max = n
