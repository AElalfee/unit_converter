import pytest

from conversions import convert_length
from models.length import Length


def test_convert_length_meters_to_kilometers():
    result = convert_length(1000, Length.m.name, Length.km.name)
    assert result == 1.0


def test_convert_length_inch_to_cm():
    result = convert_length(1, Length.inch.name, Length.cm.name)
    assert result == pytest.approx(2.54, rel=1e-9)


def test_miles_to_millimeters():
    result = convert_length(1, Length.mile.name, Length.mm.name)
    assert result == pytest.approx(1609344.0, rel=1e-9)