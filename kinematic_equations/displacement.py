# Ima Hurryin is approaching a stoplight moving with a velocity of 30.0 m/s. 
#The light turns yellow, and Ima applies the brakes and skids to a stop. 
#If Ima's acceleration is -8.00 m/s2, then determine the displacement of the car during the skidding process.
from z3 import *

d, a, t, v_i, v_f = Reals('d a t v__i v__f')

equations = [
   d == v_i * t + (a*t**2)/2,
   v_f == v_i + a*t,
]
print("Kinematic equations:")
print(equations)

# Given v_i, v_f and a, find d
problem = [
    v_i == 30,
    v_f == 0,
    a   == -8
]
print("Problem:")
print(problem)

print("Solution:")
solve(equations + problem)
