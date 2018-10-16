import re


def validate(name, price):
    """A method to Check if name and price are of the correct form"""
    if re.compile('([a-zA-z]*)').match(str(name)):
        return False
    if re.compile('([1-9][0-9]*)').match(price):
        return False
    return True
