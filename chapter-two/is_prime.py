"""
PSEUDOPOLYNOMIALITY
Is is a prime number?
its running time is Θ(n)
"""

def is_prime(n):
    for i in range(2, n):
        if n % i == 0: return False
    return True
