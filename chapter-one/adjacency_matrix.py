"""

Adjacency matrix implemented with nested lists.


The other common form of graph representation is the adjacency matrix. The main difference is the following: instead of listing all neighbors for each node, we have one row (an array) with one position for each possible neighbor (that is, one for each node in the graph), and store a value (such as True or False), indicating whether that node is indeed a neighbor. Again, the simplest implementation is achieved using nested lists.
"""

a, b, c, d, e, f, g, h = range(8)

N = [
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

print("Neighborhood membership")
print(N[a][b])

print("*" * 20)
print("Degree")
print(sum(N[a]))

"""
The way we’d use this is slightly different from the adjacency lists/sets. Instead of checking whether b is in N[a], you would check whether the matrix cell N[a][b] is true. Also, you can no longer use len(N[a]) to find the number of neighbors, because all rows are of equal length. Instead, use sum
"""