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



# """This must be a full address with street number, street, city, state,
# and ZIP code. Again, US-only."""
# assert v.address("""368 Agness Harbor
# Port Mariah, MS 63293""")
# assert v.address("""96762 Juluis Road Suite 392
# Lake Imogenemouth, AK 20211""")
# assert v.address("""671 Tawnya Island Apt. 526
# Clementeburgh, AK 82652""")
# assert v.address("""568 Eunice Shoals
# Parishaven, AK 09922-2288""")
# assert v.address("8264 Schamberger Spring, Jordanside, MT 98833-0997")
#
# assert not v.address("")
# assert not v.address("99132 Kaylah Union Suite 301")
# assert not v.address("Lake Joellville, NH")
# assert not v.address("35981")
