from z3 import *

# Number of write/reads to variable V
steps = 4
# Number of threads
num_threads = 2
# Values for V
V = [ [Int('V_%i_%i' % (i + 1, j+1)) for j in range(num_threads)] for i in range(steps)]

# statement ordering constraint
v_ordering_constraints = [And(V[2 - 1][i] > V[1 - 1][i], # V2 > V1 
                              V[3 - 1][i] > V[1 - 1][i], # V3 > V1
                              V[3 - 1][i] > V[2 - 1][i], # Assume that V2 happens before V3
                              V[4 - 1][i] > V[2 - 1][i], # V4 > V2
                              V[4 - 1][i] > V[3 - 1][i]) # V4 > V3
                              for i in range(num_threads)]

# All values of V must be distinct
v_distinct_constraints = [Distinct([V[i][j] for j in range(num_threads) for i in range(steps)])]

# All values of V must be between 0 and 7
v_value_constraints = [And(0 <= V[i][j], V[i][j] <= 7) for j in range(num_threads) for i in range(steps) ]

# Add all constraints
concurrency_c = v_ordering_constraints + v_distinct_constraints + v_value_constraints

s = Solver()
s.add(concurrency_c)
results = []

while s.check() == sat:
  # Get the current result
  results.append(s.model())
  # Ignore the current result for the next round
  s.add(Or([V[i][j] != s.model()[V[i][j]] for j in range(num_threads) for i in range(steps)])) 

print(results)
print(len(results))
