from math import *
from math import sin, cos, tan



#Integral approximation using the midpoint Riemann Sum with 'n' subintervals
#Higher n yields more accurate result

def integrate(func: str, lowerBound, upperBound, n):
    summation = 0
    finalSum = 0
    f = lambda x: eval(func)
    for i in range (1, n+1):
        k = (upperBound - lowerBound)/n #sub-intervals

        summation += f((lowerBound + ((i - (1/2)) * k) )) #height of rectangles

        finalSum = k * summation #Area of rectangles
    return finalSum

 
    




#print(midSum('x**2', 0, 10, 10000))


