import numpy as np
x = np.array([8, 11, 15, 18, 22], dtype=float)
y = np.array([5, 9, 10, 8, 7], dtype=float)
n = len(x)
m = n - 1
# Sistema linear A*c = b
A, b = [], []
# 1. Condicoes de interpolacao
for i in range(m):
	for k in [i, i + 1]:
		linha = np.zeros(3*m)
		linha[3*i:3*i+3] = [x[k]**2, x[k], 1]
		A.append(linha)
		b.append(y[k])
# 2. Continuidade da primeira derivada
for i in range(1, m):
	xi = x[i]
	linha = np.zeros(3*m)
	linha[3*(i-1):3*(i-1)+2] = [2*xi, 1]
	linha[3*i:3*i+2] = [-2*xi, -1]
	A.append(linha)
	b.append(0)