from enum import Enum


class Temperature(Enum):
    celsius = "celsius"
    fahrenheit = "fahrenheit"
    kelvin = "kelvin"

    def __init__(self, label):
        self.label = label
