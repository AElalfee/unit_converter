from enum import Enum

class Length(Enum):
    mm = ('mm', 0.001)
    cm = ('cm', 0.01)
    m = ('m', 1.0)
    km = ('km', 1000)
    inch = ("inch", 0.0254)
    foot = ("foot", 0.3048)
    yard = ("yard", 0.9144)
    mile = ("mile", 1609.344)
    
    
    def __init__(self, label, rate):
        self.label = label
        self.rate = rate