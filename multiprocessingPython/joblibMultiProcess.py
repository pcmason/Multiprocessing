#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:41:17 2023

Example using multiprocessing from the joblib libarary on the cube() method that will be run 1000 times. 

@author: paulmason
"""
import time
from joblib import Parallel, delayed

def cube(x):
    return x**3

start_time = time.perf_counter()
#delayed() is a wraper to another function to create a delayed version of the function call
#Call the delayed function multiple times with different sets of arguments 
#Parallel() creates the engine instance and here there will be 3 processes running in parallel
result = Parallel(n_jobs = 3)(delayed(cube)(i) for i in range(1, 1000))
finish_time = time.perf_counter()
print(f"Program finished in {finish_time - start_time} seconds.")
print(result)