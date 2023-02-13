# The solution is a model for the set of asserted constraints. 
# A model is an interpretation that makes each asserted constraint true. 
# This example show how to inspect models.
from z3 import *

x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
print(s.check())

m = s.model()
print("x = %s" % m[x])

print("traversing model...")
for d in m.decls():
    print("%s = %s" % (d.name(), m[d]))
