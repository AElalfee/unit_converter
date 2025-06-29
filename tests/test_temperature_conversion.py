import pytest

from conversions import convert_temperature
from models.temperature import Temperature


def test_convert_temperature_celsius_to_fahrenheit():
    result = convert_temperature(
        0, Temperature.celsius.name, Temperature.fahrenheit.name
    )
    assert result == 32.0


def test_convert_temperature_fahrenheit_to_celsius():
    result = convert_temperature(
        32, Temperature.fahrenheit.name, Temperature.celsius.name
    )
    assert result == 0.0


def test_convert_temperature_kelvin_to_celsius():
    result = convert_temperature(
        273.15, Temperature.kelvin.name, Temperature.celsius.name
    )
    assert result == 0.0


def test_convert_temperature_celsius_to_kelvin():
    result = convert_temperature(0, Temperature.celsius.name, Temperature.kelvin.name)
    assert result == 273.15
