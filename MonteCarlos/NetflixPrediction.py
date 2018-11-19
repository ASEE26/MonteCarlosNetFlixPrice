import matplotlib
import matplotlib.pyplot as plt

import numpy as np
from scipy.stats import norm
from pandas_datareader import data
from timeit import default_timer as timer
import random 
import math

Netflix = data.DataReader('NFLX', 'yahoo',start='1/1/2003')
#Netflix

Netflix_2017 = Netflix[:3776] #3776 los dias hasta el año 2017
#Netflix_2017

#calcular la tasa de crecimiento anual compuesta (CAGR) que
#nos dará nuestra entrada de retorno promedio (mu)
days = (Netflix_2017.index[-1] - Netflix_2017.index[0]).days
cagr = ((((Netflix_2017['Adj Close'][-1]) / Netflix_2017['Adj Close'][1])) ** (365.0/days)) - 1 #promedio de ganancias
print ('CAGR =',str(round(cagr,4)*100)+"%")
mu = cagr
 
#Crea una serie de rendimientos porcentuales y calcula.
#La volatilidad anual de los rendimientos.
Netflix_2017['Returns'] = Netflix_2017['Adj Close'].pct_change()
vol = Netflix_2017['Returns'].std()*math.sqrt(252)
print ("Annual Volatility =",str(round(vol,4)*100)+"%")

result = []
result2 = []
S = Netflix_2017['Adj Close'][-1]
T = 252 #dias del año bursatil

def simulacion(N=1000):
    for i in range(N):
        daily_returns=np.random.normal(mu/T,vol/math.sqrt(T),T)+1
        
        price_list = [S]
        for x in daily_returns:
            price_list.append(price_list[-1]*x)
    
        plt.plot(price_list)
        
        result.append(price_list[-1])
        result2.append(price_list[0])
        #result2.append(sum(price_list))
    plt.show()
    plt.hist(result,bins=50)
    plt.show()

start = timer()
simulacion(1000)
end = timer()
print("Time :", end - start)
print("Valor esperado para el primer dia del año 2018 es ", round(np.mean(result2),2))
print("Valor esperado para el ultimo dia del año 2018 es ", round(np.mean(result),2))
print("Comprobacion del precio en el primer dia de enero: \n")
Netflix[3776:3777]