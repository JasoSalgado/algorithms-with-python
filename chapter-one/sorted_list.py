"""
A slight variation on this would be to represent the neighbor sets as sorted lists. If you aren’t modifying the lists much, you can keep them sorted and use bisection.

Yet another minor tweak on this idea is to use dicts instead of sets or lists.
"""

a, b, c, d, e, f, g, h = range(8) 
N = [
    {b:2, c:1, d:3, e:9, f:4},
    {c:4, e:3},
    {d:8},
    {e:7},
    {f:5},
    {c:2, g:2, h:2},
    {f:1, h:6},
    {f:9, g:8},
]

print(N)

print(b in N[a])
print(len(N[f]))
print(N[a][b])