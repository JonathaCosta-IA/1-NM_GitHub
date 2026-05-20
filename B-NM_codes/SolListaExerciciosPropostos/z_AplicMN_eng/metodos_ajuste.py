
#%%
import numpy as np
import matplotlib.pyplot as plt

class RegLinRegPol():
    def __init__(self,x,y,grau=1):
        self.x = x
        self.y = y

    def GerarModelo(self,grau,exibir=0):
        modelo = np.poly1d(np.polyfit(self.x,self.y,grau))
        if exibir == 1 :print(f"O modelo estimado é \n{modelo}\n")
        return modelo
    
    def EstimarValor(self,modelo,x0):
        y0 = modelo(x0)
        print(f"O estimado de y para x = {x0:.6f} é: {y0:.6f}\n")
        return y0
    
    def CalcErros(self,modelo):
        y_real = self.y
        y_pred = modelo(self.x)

        ErroModelo = np.sum((y_real - y_pred)**2)
        ErroMedio = np.sum((y_real - np.mean(y_real))**2)
        r2 = 1 - ErroModelo/ErroMedio
        print(f"\nErro quadrático total = {ErroModelo:.6f}")
        print(f"R² = {r2:.6f}")

        return ErroModelo,ErroMedio

    def ExibirGraf(self,modelo):
        y_estimado = modelo(self.x)
        plt.title(f"Gráfico do modelo")
        plt.plot(self.x,self.y,'o',label = 'Dados de ensaio')
        plt.plot(self.x,y_estimado,'--',label = 'Modelo')
        plt.legend()
        plt.grid()
        plt.show()


# -------------------------------------------------------
# Simular
# x=[0,1,2,3,4]
# y=[1.1,2,2.9,4.2,4.8]
# a=RegLinRegPol(x,y)
# for i in range(5):
#     modelo = a.GerarModelo(i)
#     a.CalcErros(modelo)
# modelo = a.GerarModelo(exibir=1,grau=2)
# a.CalcErros(modelo)
# a.EstimarValor(modelo,2.5356)
# a.ExibirGraf(modelo)