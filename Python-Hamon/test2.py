from exersise1 import palindrome,freq



def test_is_palindrome():
    assert palindrome("nivin")

def test_not_palindrome():
    assert not palindrome("dog")

def test_empty_palindrome():
    assert palindrome("")