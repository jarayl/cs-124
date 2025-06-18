import math

def witness(p):
    for a in range(2,p):
        if pow(a,p-1,p) != 1 and math.gcd(a,p) == 1:
            return a
    return p
print(witness(12403180369))
print(pow(2,12403180368, 12403180369))