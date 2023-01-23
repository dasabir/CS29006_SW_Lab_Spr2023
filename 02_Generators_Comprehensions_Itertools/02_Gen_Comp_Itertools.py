# ===============
# Use of 'range' function
# start: 1 (included)
# stop: 10 (excluded)
# step: 2
for i in range(1, 10, 2):
    print(i)
# prints: 1.. 3.. 5.. 7.. 9

# Use of 'range' function
# start: 0 (excluded, default)
# stop: 5 (included)
# step: 1 (default)
for i in range(5):
    print(i)
# prints: 0.. 1.. 2.. 3.. 4
# ===============

# ===============
# when iterated over, 'even_gen' will generate 0.. 2.. 4.. ... 98
even_gen = (i for i in range(100) if i%2 == 0)

for item in even_gen:
    print(item)
# prints: 0.. 2.. 4.. ... 98
# ===============

# ===============
# Generators are not stored
even_gen = (i for i in range(100) if i%2 == 0)
print(even_gen)
# Example output: <generator object <genexpr> at 0x7fda3c2329e0>
# ===============

# =============== UNCOMMENT THE PRINT STATEMENT TO RUN
# query the length of a generator
# print(len(even_gen))
# Output: TypeError: object of type 'generator' has no len()
# ===============

# ===============
gen = (i**2 for i in range(100))
# computes the sum 0 + 1 + 4 + 9 + 25 + ... + 9801
print(sum(gen))
# prints 328350
# ===============

# ===============
print(sum(gen))
# prints 0
# ===============

# =============== UNCOMMENT THE LAST PRINT STATEMENT TO RUN
# Iterating over generators using next
short_gen = (i**2 for i in range(3))
print(next(short_gen)) # prints 0
print(next(short_gen)) # prints 1
print(next(short_gen)) # prints 4
# print(next(short_gen)) # gives StopIteration exception
# ===============

# ===============
# a simple list comprehension
print([i**2 for i in range(10)])
# prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# ===============

# ===============
# Finding indices of None in a list in one line
example_list = [2, None, -10, None, 4, 8]
print([idx for idx, item in enumerate(example_list) if item is None])
# prints [1, 3]
# ===============

# ===============
# zip function
names = ["Angie", "Brian", "Cassie", "David"]
exam_1_scores = [90, 82, 79, 87]
exam_2_scores = [95, 84, 72, 91]
print(list(zip(names, exam_1_scores, exam_2_scores)))
# prints [('Angie', 90, 95), ('Brian', 82, 84), ('Cassie', 79, 72), ('David', 87, 91)]
# ===============

# ===============
from itertools import combinations
print(list(combinations([0, 1, 2, 3], 3)))
# prints [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
# ===============