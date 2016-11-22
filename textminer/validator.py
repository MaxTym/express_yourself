import re


def binary(test):
    return re.findall(r'^[0, 1]+$', test)


def binary_even(test):
    return re.findall(r'^\d+0$', test)


def hex(test):
    return re.findall(r'^[A-Fa-f0-9]+$', test)


def word(test):
    return re.findall(r'^[a-z0-9\-]+[a-z]+$', test)


def words(example, count=None):
    x = re.findall(r'[a-z0-9]*\-*[a-z]+', example)
    if count is None:
        return len(x) == len(example.split(' '))
    else:
        return len(x) == count


def phone_number(test):
    return re.findall(r'(?:\(?(\d{3})\)?[-.]?\s*)?(\d{3})[\-\.]?(\d{4})', test)


def money(test):
    return re.findall(r'^\$\d+((\,\d{3})?)*(\.\d{2})?$', test)


def zipcode(test):
    return re.findall(r'^\d{5}(\-\d{4})?$', test)


def date(test):
    return re.findall(r'\d+[/-]?\d+[/-]\d+', test)


def email(test):
    return re.findall(r'^\w+(\.)?\w+@\w+\.\w+$', test)


def address(test):
    return re.search(r"^\d+([\w\s]+) [\.\,]? [\w\s]? (\d+)?, ([A-Z]{2}) (\d{5})(\-\d{4})?$", test)
