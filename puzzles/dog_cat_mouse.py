#Spend d exactly 100 dollars and buy exactly 100 animals. 
#Dogs cost 15 dollars, cats cost 1 dollar, and mice cost 25 cents each. 
#You have to buy at least one of each. How many of each should you buy?
from z3 import *

# Create 3 integer variables
dog, cat, mouse = Ints('dog cat mouse')
solve(dog >= 1,   # at least one dog
      cat >= 1,   # at least one cat
      mouse >= 1, # at least one mouse
      # we want to buy 100 animals
      dog + cat + mouse == 100,
      # We have 100 dollars (10000 cents):
      #   dogs cost 15 dollars (1500 cents), 
      #   cats cost 1 dollar (100 cents), and 
      #   mice cost 25 cents 
      1500 * dog + 100 * cat + 25 * mouse == 10000)