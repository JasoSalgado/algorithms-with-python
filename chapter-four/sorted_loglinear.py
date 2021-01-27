"""
Sorted loglinear
"""

seq.sort()
dd = float('inf')
for i in range(len(seq) -1):
    x, y = seq[i], seq[i+1]
    if x == y: continue
    d = abs(x-y)
    if d < dd:
        xx, yy, dd = x, y, d

print(xx, yy)
