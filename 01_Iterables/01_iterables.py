print("sum function works on iterbales: {}".format(sum([1, 2, 3])))

print("sorted function works on iterbales: {}".format(sorted((-6, 8, 2, 0, 1.5))))

# ===============
example_list = [2, None, -10, None, 4, 8]
none_indices = []
iter_cnt = 0
 
# Without using enumeration and thus manually tracking
# iteration-count
for item in example_list:
    if item is None:
        none_indices.append(iter_cnt)
    iter_cnt = iter_cnt + 1

print("Position of None in the list \
    (w/o using enumeration): \
    {:s}".format(", ".join([str(s) for s in none_indices])))
# ===============
 
# ===============
example_list = [2, None, -10, None, 4, 8]
none_indices = []
 
# Using enumeration
for iter_cnt, item in enumerate(example_list):
    if item is None:
        none_indices.append(iter_cnt)
 
print("Position of None in the list \
    (using enumeration): \
    {:s}".format(", ".join([str(s) for s in none_indices])))
# ===============
 
print([idx for idx, item in enumerate(example_list) if item is None])