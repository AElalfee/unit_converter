import pytest

from conversions import convert_weight
from models.weight import Weight


def test_convert_weight_kg_to_g():
    result = convert_weight(1, Weight.kilogram.name, Weight.gram.name)
    assert result == 1000.0


def test_convert_weight_gram_to_milligram():
    result = convert_weight(1, Weight.gram.name, Weight.milligram.name)
    assert result == 1000.0


def test_convert_weight_ounce_to_pound():
    result = convert_weight(16, Weight.ounce.name, Weight.pound.name)
    assert result == 1.0
