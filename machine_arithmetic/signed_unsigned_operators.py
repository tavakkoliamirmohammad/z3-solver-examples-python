# In Z3 there is no distinction between signed and unsigned bit-vectors as numbers
# In Z3Py, the operators <, <=, >, >=, /, % and >> correspond to the signed versions
# The corresponding unsigned operators are ULT, ULE, UGT, UGE, UDiv, URem and LShR.
from z3 import *

# Create to bit-vectors of size 32
x, y = BitVecs('x y', 32)

solve(x + y == 2, x > 0, y > 0)

# Bit-wise operators
# & bit-wise and
# | bit-wise or
# ~ bit-wise not
solve(x & y == ~y)

solve(x < 0)

# using unsigned version of < 
solve(ULT(x, 0))
The operator >> is the arithmetic shift right, and << is the shift left. The logical shift right is the operator LShR.

# Create to bit-vectors of size 32
x, y = BitVecs('x y', 32)

solve(x >> 2 == 3)

solve(x << 2 == 3)

solve(x << 2 == 24)
