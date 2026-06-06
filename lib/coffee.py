#!/usr/bin/env python3

class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if value not in ["small", "Medium", "Large"]:
            print("size must be Small, Medium, or large.")
        else:
            self._size = value
            
    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1