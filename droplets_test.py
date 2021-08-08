# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:14:56 2021

@author: Fulmenius User
"""

#stdlib imports

import numpy as np
import random

#custom imports 

import generators as gen
import kawasaki_sample as kwss

N = 10
T = 2.1
k= 0.25

L, plm, p, m = gen.droplet_gen(N, N, k)
kwss.numpy_metropolis_kawasaki(L, T, plm, p, num_it=1000)
gen.drawLattice(L)
