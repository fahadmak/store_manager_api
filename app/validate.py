import re


def validate(name, price):
    """A method to Check if name and price are of the correct form"""
    if re.compile('^[a-zA-Z]+').match(str(name)) and re.compile('([1-9][0-9]*)').match(str(price)):
        return True
    return False
