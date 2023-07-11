#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 17:09:06 2023

Basic example showing the use of the multiprocessing library.
Combines the task() method 10 times and is completed in < 1 second using the multiprocessing library.

@author: paulmason
"""

import multiprocessing
import time

#Create a function that sleeps for 0.5s and prints a statement before and after the sleep
def task():
    print('Sleeping for 0.5 seconds.')
    time.sleep(0.5)
    print('Finished sleeping.')
    
#Multiprocessing must be done within the main conditional statement
if __name__ == '__main__':
    start_time = time.perf_counter()
    processes = []
    
    #Create 10 processes and start them
    for i in range(10):
        p = multiprocessing.Process(target = task)
        p.start()
        processes.append(p)
    
    #Join all the processes
    for p in processes:
        p.join()
    
    finish_time = time.perf_counter()
    
    #Output the speed of the program
    print(f"Program finished in {finish_time - start_time} seconds.")