from models.length import Length
from models.weight import Weight


def convert_length(value, from_unit, to_unit):
    return value * Length[from_unit].rate / Length[to_unit].rate


def convert_weight(value, from_unit, to_unit):
    return value * Weight[from_unit].rate / Weight[to_unit].rate


def convert_temperature():
    pass
