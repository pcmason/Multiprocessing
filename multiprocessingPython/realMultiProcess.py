#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:28:16 2023

Example using multiprocessing on the cube() method that will be run 1000 times. 

@author: paulmason
"""

import concurrent.futures
import time

def cube(x):
    return x ** 3

if __name__ == "__main__":
    #Create a pool to run 3 processes at a time
    with concurrent.futures.ProcessPoolExecutor(3) as executor:
        start_time = time.perf_counter()
        result = list(executor.map(cube, range(1, 1000)))
        finish_time = time.perf_counter()
    #Output results
    print(f"Program finished in {finish_time - start_time} seconds.")
    print(result)