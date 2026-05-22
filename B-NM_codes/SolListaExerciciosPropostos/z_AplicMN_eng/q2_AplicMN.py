"""
 --------------------------------------------------------
# ENUNCIADO
Considere os dados da questão anterior.
Calcule o polinômio de interpolação $p(x)$ utilizando Lagrange.
Calcule o polinômio de interpolação $p(x)$ utilizando Newton.   
Calcule o polinômio de interpolação $p(x)$ utilizando regressão linear.
Calcule o polinômio de interpolação $p(x)$ utilizando regressão polinomial com graus(2,3,4).
Compare erro e custo computacional para um ponto de teste t=50.
# --------------------------------------------------------

"""
#%%
import numpy as np
import pandas as pd
from metodos_ajuste import RegLinRegPol
