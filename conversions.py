from models.length import Length
from models.weight import Weight
from models.temperature import Temperature


def convert_length(value, from_unit, to_unit):
    return value * Length[from_unit].rate / Length[to_unit].rate


def convert_weight(value, from_unit, to_unit):
    return value * Weight[from_unit].rate / Weight[to_unit].rate


def convert_temperature(value, from_unit, to_unit):
    from_enum = Temperature[from_unit]
    to_enum = Temperature[to_unit]

    if from_enum == Temperature.celsius:
        celsius = value
    elif from_enum == Temperature.fahrenheit:
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if to_enum == Temperature.celsius:
        return celsius
    elif to_enum == Temperature.fahrenheit:
        return celsius * 9 / 5 + 32
    else:
        return celsius + 273.15
