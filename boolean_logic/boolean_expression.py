# Example showing the use of boolean values in simplify function and boolean operators
from z3 import *

p = Bool('p')
q = Bool('q')
print(And(p, q, True))
print(simplify(And(p, q, True)))
print(simplify(And(p, False)))