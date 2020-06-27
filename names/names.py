import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Initial start of the tree 
bsTree = BSTNode('names') 
duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements


# Whats need?
# use binary tree initialize the tree with string value
# use binary insert to add names to tree
# insert each name in the tree
# if value of name1 contains value of name2 add to duplicates list

# For every name in names_1 put into tree
for n in names_1: 
    bsTree.insert(n)
# For everyname in names_2 put into tree
for n2 in names_2:
    bsTree.insert(n2)
    # if statement here name1 and name2 are the same add it to duplicates list
    if bsTree.contains(n2):
        duplicates.append(n2)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
