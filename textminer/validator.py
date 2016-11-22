import re


def binary(test):
    return re.findall(r'^[0, 1]+$', test)


def binary_even(test):
    return re.findall(r'^\d+0$', test)


def hex(test):
    return re.findall(r'^[A-Fa-f0-9]+$', test)


def word(test):
    return re.findall(r'^\d?[A-Za-z]$', test)
