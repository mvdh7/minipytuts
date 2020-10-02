import numpy as np

# Make a normal list first, then turn it into a numpy array
t_list = [25.1, 12.3, 6.8]
t = np.array(t_list)

# Import text data
data = np.genfromtxt('data/titration2.txt', skip_header=2)

# Pull out individual columns
vol = data[:, 0]
emf = data[:, 1]

# Use logical indexing to pull out subsets of the data
# This is efficient (both in computation time, and how much code you must write)
# This is robust - it still works when you change the input file
next_step = (emf > 300) & (emf < 400)
all_next_step = data[next_step, :]
vol_next_step = vol[next_step]
emf_next_step = emf[next_step]

# The pure Python (i.e. not NumPy) equivalent is "list comprehension"
# It's a cool tool but much slower (in computation time) and can be harder to understand
emf_next_list = [e for e in emf if e > 300 and e < 400]

# Using positional indexing works too... but this is very "brittle" - it breaks if you
# switch to a different input file.
vol_next_v2 = vol[10:16]
emf_next_v2 = emf[10:16]
