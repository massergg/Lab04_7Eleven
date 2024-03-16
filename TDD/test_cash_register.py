# test_cash_register.py
import pytest
import sys
sys.path.append('/path/to/LAB04_7ELEVEN')
from main.cash_register import CashRegister


@pytest.fixture
def cash_register():
    return CashRegister()

def test_add_item(cash_register):
    cash_register.add_item("apple", 1.0)
    assert cash_register.items == {"apple": 1}
    assert cash_register.prices == {"apple": 1.0}

def test_add_multiple_items(cash_register):
    cash_register.add_item("apple", 1.0)
    cash_register.add_item("banana", 0.5)
    assert cash_register.items == {"apple": 1, "banana": 1}
    assert cash_register.prices == {"apple": 1.0, "banana": 0.5}

def test_calculate_total(cash_register):
    cash_register.add_item("apple", 1.0)
    cash_register.add_item("banana", 0.5)
    assert cash_register.calculate_total() == 1.5

def test_apply_discount(cash_register):
    cash_register.add_item("apple", 1.0)
    cash_register.apply_discount("apple", 0.5)
    assert cash_register.prices["apple"] == 0.5

def test_apply_discount_invalid_item(cash_register):
    with pytest.raises(ValueError):
        cash_register.apply_discount("orange", 0.5)
