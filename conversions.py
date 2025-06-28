from models.length import Length


def convert_length(value, from_unit, to_unit):
    return value * Length[from_unit].rate / Length[to_unit].rate


def convert_weight():
    pass


def convert_temperature():
    pass
