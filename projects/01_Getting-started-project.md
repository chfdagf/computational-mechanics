---
jupytext:
  formats: notebooks//ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
```

# Computational Mechanics Project #01 - Heat Transfer in Forensic Science

We can use our current skillset for a macabre application. We can predict the time of death based upon the current temperature and change in temperature of a corpse. 

Forensic scientists use Newton's law of cooling to determine the time elapsed since the loss of life, 

$\frac{dT}{dt} = -K(T-T_a)$,

where $T$ is the current temperature, $T_a$ is the ambient temperature, $t$ is the elapsed time in hours, and $K$ is an empirical constant. 

Suppose the temperature of the corpse is 85$^o$F at 11:00 am. Then, 2 hours later the temperature is 74$^{o}$F. 

Assume ambient temperature is a constant 65$^{o}$F.

1. Use Python to calculate $K$ using a finite difference approximation, $\frac{dT}{dt} \approx \frac{T(t+\Delta t)-T(t)}{\Delta t}$.

```{code-cell} ipython3
T_a, T_0, T_1=65,85,74
time0,time1= 0,2
deltaT=time1-time0 #delta t=2 hours
T_sumT=T_1 #t+delta t = 2 --> temp@2 hours T(2)=74F
T_t=T_0 #T(0)= 85
dTdt=(T_sumT-T_t)/deltaT #finite difference approx
K= -dTdt/(T_0-T_a)
print(K)
```

2. Change your work from problem 1 to create a function that accepts the temperature at two times, ambient temperature, and the time elapsed to return $K$.

```{code-cell} ipython3
def LifeApprox(Temp1,Temp2,TempAmb,DeltaTime):
    """`LifeApprox` is a function that accepts the temperature at two times, ambient temperature, and the time elapsed to return  𝐾
    Arguments:
    ----------
    Temp1:First temperature
    Temp2:Second temperature
    TempAmb: Ambient temperature
    DeltaTime: time elapsed between temperatures
    
    Outputs:
    -------- 
    K: empirical constant
    """
    dTdt=(Temp2-Temp1)/deltaT #finite difference approx
    K= -dTdt/(Temp1-TempAmb)
    return K
T_a, T_0, T_1=65,85,74
time=2
print(LifeApprox(T_0,T_1,T_a,time))
```

```{code-cell} ipython3
def LifeApproxT(time):
    """`LifeApproxT` is a function that returns the corpse temperature of a given time
    Arguments:
    ----------
    Time: time elapsed between initial temperature
    
    Outputs:
    -------- 
    Temperature: Corpse temperature
    """  
    K=0.275
    T_0=85
    T_a=65
    T_t=-K*(T_0-T_a)*time+T_0
    return T_t
print(LifeApproxT(2))
```

3. A first-order thermal system has the following analytical solution, 

    $T(t) =T_a+(T(0)-T_a)e^{-Kt}$

    where $T(0)$ is the temperature of the corpse at t=0 hours i.e. at the time of discovery and $T_a$ is a constant ambient temperature. 

    a. Show that an Euler integration converges to the analytical solution as the time step is decreased. Use the constant $K$ derived above and the initial temperature, T(0) = 85$^o$F. 

    b. What is the final temperature as t$\rightarrow\infty$?
    
    c. At what time was the corpse 98.6$^{o}$F? i.e. what was the time of death?

```{code-cell} ipython3
T_a=65
T_0=85
K=0.275
def LifeAnalytical(time, T_Ambient=65, T_0=85, K=0.275):
    '''`LifeAnalytical` is a function that returns the Temperature of a given time and optional Ambient temperature, Temperature at time of discovery and constant K
    Arguments:
    ----------
    time: time in hours elapsed from time of discovery
    T_Ambient:Ambient Temperature
    T_0: Temperature of corpse at time of discovery
    K: empirical constant
    
    Outputs:
    --------
    T_t: temperature of corpse at given time in Farenheit
    '''
    T_t=T_Ambient +(T_0-T_Ambient)*np.exp(-K*time)
    return T_t
#a
t=np.linspace(0,2,num=50)#num = time step
n= len(t)
v_numerical=[]
for i in range(len(t)):v_numerical.append(LifeApproxT(t[i]))
v_analytical=[] 
for i in range(len(t)):v_analytical.append(LifeAnalytical(t[i]))
#for i in reversed(range(0,3)):
#    print(f"time elapsed: {i}, Temperature of corpse: {LifeAnalytical(i)}{chr(176)}F")#shows as elapsed time(hours) go to 0 it reaches
plt.figure()
plt.plot(t,v_numerical,'o',label=str(n)+' Euler steps')
plt.plot(t,v_analytical,label='analytical')
plt.title('First 2 hours of corpse temperature')
plt.xlabel('time (hours)')
plt.ylabel(f'Temperature ({chr(176)}F)')
plt.ylim(70,90)
plt.legend()
print("From the graph it can be observed that the earlier in time(0.0-0.5) the values overlap which is the earlier time step which means the Euler integration converges to the analytical solution as the time step is decreased.")
```

```{code-cell} ipython3
#b
print(f"b) final temp as t->inf using Analytical: {LifeAnalytical(np.inf)}{chr(176)}F") # Logical as it should reach the same as Ambient temperature
#c
#rearranging Analytical function to solve for time
T_t=85
T_0=98.6
T_a=65
K=0.275
timeAnalytical=np.log((T_t-T_a)/(T_0-T_a))/-K
print(f"c) Time of corpse at 98.6{chr(176)}F from analytical function: {timeAnalytical:5.2f} hours ({timeAnalytical:5.2f} hours earlier than 11 am)") #exact value = 1.8865228851460631 hours
```

```{code-cell} ipython3

```
