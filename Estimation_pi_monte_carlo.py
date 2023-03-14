# -*- coding: utf-8 -*-
"""
Approximation de la constante d'Archimède, Pi, π'
"""

import random as rd
import matplotlib.pyplot as plt
import numpy as np


def Estimation_Pi(n):
    #Compteur points dans le quart de cercle de rayon 1
    nbr_points_in = 0

    for i in range(0, n):
        x, y = rd.random(), rd.random()        
        norme = pow(x,2) + pow(y,2)
        if(norme <= 1):
            nbr_points_in = nbr_points_in + 1
    
    estimation_pi = (nbr_points_in / n) * 4
    return(estimation_pi)       

if __name__ == "__main__":
    
    
    # #On estime Pi pour différents n = nombre de simulation
    # estimations_pi = []
    # n = []
    # for i in range(1,100000,1000):        
    #     estimations_pi.append(Estimation_Pi(i))
    #     n.append(i)
    
    # plt.figure(figsize=(10,6))
    # plt.plot([1,100000],[3.141592,3.141592],color='b')
    # plt.text(101000,3.141592,"$\pi$",color='b',fontsize=14)
    # plt.plot(n, estimations_pi, linestyle='--', color='red')    
    # plt.xlabel('n', fontsize=20)
    # plt.title('Convergence des estimations', fontsize=20)
    # plt.ylim(3.1,3.2)
    # plt.xlim(1,100000)
    # plt.grid(axis='x')
    
    # plt.show()
    # plt.close()
    

    #Visualisation d'une estimation pour n = 1000
    nbr_points_in = 1000
    points_in_x = []
    points_in_y = []
    points_out_x = []
    points_out_y = []
    
    for i in range(0, nbr_points_in):
        x_i, y_i = rd.random(), rd.random()
        norme = pow(x_i,2) + pow(y_i,2)
        if(norme <= 1):
            points_in_x.append(x_i)
            points_in_y.append(y_i)
        else:
            points_out_x.append(x_i)
            points_out_y.append(y_i)
    
    plt.figure(figsize=(5,5))
    plt.scatter(points_in_x, points_in_y, color = 'r')
    plt.scatter(points_out_x, points_out_y, color = 'b')
    
    
    
            
    

        
    


    