import random

#Line 1
print(random.randint(5, 20))
# The smallest number is 5, and the largest is 20 (inclusive).

# Line 2
print(random.randrange(3, 10, 2))
# The smallest number is 3, and the largest is 9.
# The possible numbers are 3, 5, 7, and 9.
# No, line 2 could not have produced a 4 because the step is 2, starting from 3.

# Line 3
print(random.uniform(2.5, 5.5))
# The smallest number is 2.5, and the largest is just below 5.5
# (it can be any float in the range [2.5, 5.5) ).

# Code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
