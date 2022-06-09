import numpy as np

def CometRadius(c,n):
    #c - average comet size
    #n - array lenght 
    u=np.random.random(n)
    g=3.6
    R= c * u**g
    return R

def Hill_radius(ap,m,M): 
    return ap* (m/(3*M))**(1/3)

def Roche_limit(rho_p,rho_s, R):
               return 2.44*R*(rho_p/rho_s)**(1/3)