#run this in notebook 
from scipy.integrate import odeint
import numpy as np 
import seaborn as sns 
from matplotlib import pyplot as plt
#
from sympy.interactive import printing 
printing.init_printing(use_latex=True)
from sympy import * 
import sympy as sp 

#general solution 

x = sp.Symbol('x')
f = sp.Function('f')(x)

diffeq = Eq(f.diff(x,x)-5*f,0)
display(diffeq)
dsolve(diffeq,f)

"""
NOTES 
ODE 
dy/dt = -ky(t)
>> y(t)
"""
#coeff
k = 3
#span 
t = np.linspace(0,20)
#initial condiiton 
y0 = 1
def model(y,t):
    dydt = -k * y
    return dydt 

#solve 
y = odeint(model, y0, t)
plt.plot(t,y)
plt.show()