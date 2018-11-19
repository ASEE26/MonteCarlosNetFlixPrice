import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random 
random.seed(1993)
random.random()

def f(x):
    return np.exp(x)+np.cos(x)

def integral_aprox(N=10000000):
    x = np.random.uniform(0, 1, size=(1, N))
    h_n = f(x).sum()/N
    return h_n
integral_aprox()