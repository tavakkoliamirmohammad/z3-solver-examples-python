#Ben Rushin is waiting at a stoplight. 
#When it finally turns green, Ben accelerated from rest at a rate of a 6.00 m/s2 for a time of 4.10 seconds. 
#Determine the displacement of Ben's car during this time period.

from z3 import *

d, a, t, v_i, v_f = Reals('d a t v__i v__f')

equations = [
   d == v_i * t + (a*t**2)/2,
   v_f == v_i + a*t,
]

# Given v_i, t and a, find d
problem = [
    v_i == 0,
    t   == 4.10,
    a   == 6
]

solve(equations + problem)

# Display rationals in decimal notation
set_option(rational_to_decimal=True)

solve(equations + problem)