"""
Why would it be the problematic to create a 10x10 array with the expression [[0]*10]*10?
"""
a = []
for i in range(11):
    a.append(i)
    for j in range(11):
        a.append(j)


print(f'a = {a}')
