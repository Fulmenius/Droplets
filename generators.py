# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:09:48 2020

@author: Fulmenius User

Lattice generators
"""

import numpy as np
import matplotlib.pyplot as plt


def drawLattice(L):  #Нарисовать решетку
        plt.pcolor(L)
        plt.xlabel('This is X')
        plt.ylabel('This is Y')
        plt.show()


def uniformGen(M, N): #Массив единиц
    return np.ones(size = (M, N))

def randGen(M, N):    #Случайное заполнение
    return np.random.choice([-1, 1], size = (M, N))
    
    
def fixedGen(M, N):     #M - ось Y, первая. N - ось Х, вторая. Граничные условия
    L = np.random.choice([-1, 1], size = (M, N))
    
    L[0, :] = -1
    L[M-1, :] = -1
    L[:, N-1] = 1
    L[:, 0] = 1
    L[0,N-1] = 1    
    
    return L

#Generate a 1D array containing k -1's and N*M-k 1's\
                            #with -1's on the border
                            #and shuffle the cerntral part, then reshape to 2D

def droplet_gen(M, N, k): #M, N = shape, k = proportion of 1's
    
    assert (k >= 0 and k <= 1), "k must lie between 0 and 1"
        
    m = int(np.floor((N-2)*(M-2)*k))
    L = (-1)*(np.ones((M, N)))
    L[1:M-1, 1:N-1] =\
        np.random.permutation(np.array([1]*m + [-1]*(((N-2)*(M-2)) - m)))\
                                                        .reshape(M-2, N-2)
                                                        
    pluses = np.where(L == 1)
    minuses = np.where(L[1:(N-1), 1:(M-1)] == -1)
    p = len(pluses[0])
    m = len(minuses[0])
    
    return L, np.hstack((np.array(pluses), np.array(minuses) + 1)), p, m



def six_points_gen(M, N, P):
    if P < 0 or P > 1:
        print("Wrong value: P must be between 0 and 1")
        return 0 
    
    L = np.random.choice([-1, 1], size = (M, N))
    L[0:int(np.floor(P*M)), 0] = -1
    L[int(np.floor(P*M)):, 0] = 1
    L[0:int(np.floor(P*M)), N-1] = -1
    L[int(np.floor(P*M)):, N-1] = 1
    L[M-1, 1:N-1] = -1
    L[0, 1:N-1] = 1
    
    return L


def conf_5(M, N, P):
    L = np.ones(shape=(M, N))
    L[0:int(np.floor(P*M)), 0] = -1
    L[int(np.floor(P*M)):, 0] = 1
    L[0:int(np.floor(P*M)), N-1] = -1
    L[int(np.floor(P*M)):, N-1] = 1
    L[M-1, 1:N-1] = -1
    L[0, 1:N-1] = 1
    
    return L


    


#kek = six_points_gen(40, 40, 0.5)
#drawLattice(kek)

#heh = conf_5(40, 40, 0.5)
#drawLattice(heh)


