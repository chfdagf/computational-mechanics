import numpy as np

def linInterp(x,p1,p2):
    '''linear interplation function
    return y(x) given the two endpoints 
    p1=np.array([x1,y1])
    and
    p2=np.array([x2,y2])'''
    slope = (p2[1]-p1[1])/(p2[0]-p1[0])
    
    return p1[1]+slope*(x - p1[0])