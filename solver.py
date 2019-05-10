from tspdata import TSPData
from sys import argv
from mip.model import *

inst = TSPData(argv[1])
n = inst.n
d = inst.d
m = Model()

# x[i][j] == 1 if arc (i, j) is selected, 0 otherwise
x = [[m.add_var(var_type=BINARY) for j in range(n)] for i in range(n)]

# objective function: minimize total distance
m += xsum(d[i][j] * x[i][j] for j in range(n) for i in range(n))

# enter each city exactly once
for i in range(n):
    m += xsum(x[j][i] for j in range(n) if j != i) == 1

# leave each city exactly once
for i in range(n):
    m += xsum(x[i][j] for j in range(n) if j != i) == 1

# city label var
y = [m.add_var(lb=0.0, ub=n) for i in range(n)]

# conditional constraints:
# if x[i][] then y[i] >= y[j]+1
for i in range(0, n):
    for j in range(0, n):
        if i == j or i == 0 or j == 0:
            continue
        m += y[i] - (n + 1) * x[i][j] >= y[j] - n

m.optimize()

for i in range(n):
    for j in range(n):
        if x[i][j].x >= 0.99:
            print('arc ({},{})'.format(i, j))
