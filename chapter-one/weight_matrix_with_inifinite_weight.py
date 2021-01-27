"""
Weight matrices make it easy to access edge weights, of course, but membership checking and finding the degree of a node, for example, or even iterating over neighbors must be done a bit differently now. You need to take the infinity value into account–for example, like this (using inf = float('inf') for more readable code)
"""
a, b, c, d, e, f, g, h = range(8)
_ = float('inf')

W = [
    [0, 2, 1, 3, 9, 4, _, _],
    [_, 0, 4, _, 3, _, _, _],
    [_, _, 0, 8, _, _, _, _],
    [_, _, _, 0, 7, _, _, _],
    [_, _, _, _, 0, 5, _, _],
    [_, _, 2, _, _, 0, 2, 2],
    [_, _, _, _, _, 1, 0, 6],
    [_, _, _, _, _, 9, 8, 0]
]

print(W)
print('*' * 20)
print(W[a][b])
print('*' * 20)
print(W[c][e])
print('*' * 20)
