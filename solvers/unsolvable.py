# An example showing th Z3 cannot solve non-polynomial equations
from z3 import *

x = Real('x')
s = Solver()
s.add(2**x == 3)
print(s.check())
