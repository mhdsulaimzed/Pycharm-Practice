from exercise2 import evaluate
 

def test_for_single_operand():
    assert evaluate("5") ==5

def test_for_add():
    assert evaluate("67+") == 13


def test_for_sub():
    assert evaluate("34-") == -1


def test_for_multiplication():
    assert evaluate("57*") == 35

def test_for_div():
    assert evaluate("84/") == 2

def test_for_modulus():
    assert evaluate("42%")== 0

def test_for_zerodiv():
    assert evaluate("30/")== "undefined"

def test_for_zerodiv_in_modulo():
    assert evaluate("40%")== "undefined"

def test_for_charecter():
    assert evaluate("33a") == "undefined"


