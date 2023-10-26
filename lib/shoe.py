#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "New"
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        """size must be an integer"""
        if type(size) in (int,):
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")