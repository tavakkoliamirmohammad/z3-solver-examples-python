# An example show how to use Z3 for proving Demorgan's law
from z3 import *

def prove(f):
    s = Solver()
    s.add(Not(f))
    if s.check() == unsat:
        print("proved")
    else:
        print("failed to prove")

p, q = Bools('p q')
demorgan = And(p, q) == Not(Or(Not(p), Not(q)))
print(demorgan)

print("Proving demorgan...")
prove(demorgan)