from enum import Enum


class Weight(Enum):
    milligram = ("milligram", 0.001)
    gram = ("gram", 1.0)
    kilogram = ("kilogram", 1000)
    ounce = ("ounce", 28.3495)
    pound = ("pound", 453.592)

    def __init__(self, label, rate):
        self.label = label
        self.rate = rate
