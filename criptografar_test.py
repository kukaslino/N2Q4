import pytest
from criptografar import criptografar_string

def test_criptografar_1():
    assert criptografar_string("Hello") == "72olle"

def test_criptografar_2():
    assert criptografar_string("Beleza") == "66aleze"

def test_criptografar_3():
    assert criptografar_string("John") == "74nho"

def test_criptografar_4():
    assert criptografar_string("hello world") == "104olle 119drlo"

def test_criptografar_type():
    assert criptografar_string(1) == "The value cannot be a number"


