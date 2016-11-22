import re


def phone_numbers(text):
    return re.findall(r'\([0-9]{3}\) [0-9]{3}-[0-9]{4}', text)


def emails(text):
    return re.findall(r'\w+\.?\w+@\w+\.\w{2,3}', text)
