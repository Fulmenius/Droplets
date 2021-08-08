# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:19:02 2021

@author: Fulmenius User
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:10:15 2020

@author: Fulmenius User
"""

from Constants import e, kB, J
import numpy as np
import random
from generators import drawLattice
import colorama as col

col.init()

def U_np(L):
    return -J*np.sum(L*(np.roll(L, 1, axis=0) + np.roll(L, 1, axis=1)))


#def flip(i, j, L):
#        M = L.copy()
#        M[i][j] = -M[i][j]
#        return M
     

def numpy_metropolis_kawasaki(L, T, plm, p, num_it=400):
      
    print(plm.shape)
    pluses = plm.T[0:p]
    minuses = plm.T[p:]
    
    #print(f"len(pluses) = {len(pluses[0, :])}, len(minuses)={len(minuses[0, :])}")
    print(pluses, minuses)
 
    #print("PLUSES")
    #print(list(map(lambda x: L[tuple(x)], [x for x in pluses.T])))    
    
    #print("MINUSES")
    #print(list(map(lambda x: L[tuple(x)], [x for x in minuses.T])))
    
    def get_pms():
        print("PLUSES \n", print(list(map(lambda x: L[tuple(x)], [x for x in pluses]))) )
        print("MINUSES \n", print(list(map(lambda x: L[tuple(x)], [x for x in minuses]))) )
        
    for i in range(num_it):
        
        cp = np.random.randint(len(pluses))
        chosen_plus = pluses[cp]
        #print(f"chosen_plus = {chosen_plus}")
        #print(f"value = {L[tuple(chosen_plus)]}")
        cm = np.random.randint(len(minuses))
        chosen_minus = minuses[cm]
        #print(f"chosen_minus = {chosen_minus}")  
        #print(f"value = {L[tuple(chosen_minus)]}")
        
        #dU = -J*(sum([L[R1y][R1x]*L[R1y-i][R1x-j] for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) \
         #    -sum([-L[R1y][R1x]*L[R1y-i][R1x-j] for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) )\
          #  -J*(sum([L[R2y][R2x]*L[R2y-i][R2x-j] for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) \
           #  -sum([-L[R2y][R2x]*L[R2y-i][R2x-j] for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) )\
            #    -4*J*((abs(R1x-R1y) + abs(R2x-R2y)) == 1)
        
        #calculate dU for the positive spin, then for the negative, then the interaction term
        
        dU = -J*(sum([L[tuple(chosen_plus)]*L[tuple(chosen_plus - np.array((i, j)))] \
                      for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) \
                                                                       \
             -sum([-L[tuple(chosen_plus)]*L[tuple(chosen_plus - np.array((i, j)))] \
                   for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) )\
                                                                     \
                                                                     \
            -J*(sum([L[tuple(chosen_minus)]*L[tuple(chosen_minus - np.array((i, j)))] \
                     for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) \
                                                                      \
             -sum([-L[tuple(chosen_minus)]*L[tuple(chosen_minus - np.array((i, j)))] \
                   for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]]) )\
                                                                     \
                -4*J*((abs(chosen_plus[0]-chosen_minus[0]) +\
                       abs(chosen_plus[1]-chosen_minus[1])) == 1)
        
        #get_pms()
            
        if  dU < 0:
            if (np.random.uniform(0, 1) < e**(dU/(kB*T))):
                L[tuple(chosen_plus)] = -L[tuple(chosen_plus)]
                L[tuple(chosen_minus)] = -L[tuple(chosen_minus)]
                plm.T[[cp, p+cm]]\
                    = plm.T[[p+cm, cp]]
          #      print("BOOOOOM! [ , ]")
                
                
        else:
            L[tuple(chosen_plus)] = -L[tuple(chosen_plus)]
            L[tuple(chosen_minus)] = -L[tuple(chosen_minus)]
            #print(plm.T.shape)
            #print(f"chosen_plus = {chosen_plus}")
            #print(chosen_minus)
            plm.T[[cp, p+cm]]\
                    = plm.T[[p+cm, cp]]
         #  print("BABAAAAH!, [ ][ ]")
         #   print("pluses", pluses[:, chosen_plus])
         #  print(L)
            
        i+=1
        if i % 100 == 0: drawLattice(L)
        print(dict(zip(*np.unique(L, return_counts=True))))
        
        