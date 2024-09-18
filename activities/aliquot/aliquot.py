"""Graph the Aliquot sequence for positive integer n.

Try 6 (a perfect number), 95 (aspiring), 8 (deficient), 24 (abundant), 220
(amicable), and 276.
"""

__author__ = 'Alain Kaegi'


def factors(n: int) -> list[int]:
    """Return a list of all factors (< n) of positive integer n."""
    return None

n = int(input("Enter a positive number: "))

print(factors(n))
