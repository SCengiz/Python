#!/usr/bin/python3
import numpy as np

def get_number():
		print(' -- Submodule_1 -- ')
		return 1

class Circle(object):
    
    pi = np.pi
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return Circle.pi * self.radius * self.radius
    

