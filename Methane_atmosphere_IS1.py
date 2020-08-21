from math import *
import matplotlib.pyplot as plt
E1=8.91*10**5 #float(input("Enter the emissions from CH4: "))
E2=9.05*10**5 #float(input("Enter the emissions from CO: "))
P1=5*10**5 #float(input("Enter the rate of chemical production of OH: "))
#P2=30 #float(input("Enter the rate of chemical production of CO: "))
k1=7.7*10**(-15) #float(input("Enter the rate constant of CH4+OH: "))
k2=2.5*10**(-13) #float(input("Enter the rate constant of CH4+Cl: "))
k3=2*10**(-13) #float(input("Enter the rate constant of CO+OH: "))
cOH=3.635*10**6 #float(input("Enter the initial SS concentration of OH: "))
cCH4=2*10**11 #float(input("Enter the initial SS concentration of CH4: "))
cCl=1.1*10**4 #float(input("Enter the initial SS concentration of Cl: "))
cCO=6.8*10**11 #float(input("Enter the initial SS concentration of CO: "))
T=float(input("Enter the time duration: "))
dt=float(input("Enter the time step: "))

def rCH4(cCH4):
    return E1-k1*cCH4*cOH-k2*cCH4*cCl

def rOH(cOH):
    return P1-k1*cCH4*cOH-k3*cCO*cOH

def rCO(cCO):
    return E2+rCH4(cCH4)-k3*cCO*cOH

def rk4(c,l,h):
    def r(k):
        if l=="CH4":
            return rCH4(k)
        if l=="OH":
            return rOH(k)
        if l=="CO":
            return rCO(k)
    u1=c+h*r(c)/2
    u2=c+h*r(u1)/2
    u3=c+h*r(u2)
    return (c+h/6*(r(c)+2*r(u1)+2*r(u2)+r(u3)))
    
    
t=0
COH=[cOH]
Tc=[0]
CCH4=[cCH4]
CCO=[cCO]

while t<T:
##    rCH4=E1-k1*cCH4*cOH-k2*cCH4*cCl
##    rOH=P1-k1*cCH4*cOH-k3*cCO*cOH
##    rCO=E2+rCH4-k3*cCO*cOH
##
##    cOH=cOH+rOH*dt
##    cCH4=cCH4+rCH4*dt
##    cCO=cCO+rCO*dt
    cCH4=rk4(cCH4,"CH4",dt)
    cOH=rk4(cOH,"OH",dt)
    cCO=rk4(cCO,"CO",dt)
    t+=dt
    Tc.append(t)
    COH.append(cOH)
    CCH4.append(cCH4)
    CCO.append(cCO)


#print(COH)
#print(Tc)
plt.plot(Tc,CCH4)
#plt.plot(Tc,COH)
#plt.plot(Tc,CCO)
plt.show()
