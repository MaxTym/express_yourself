import re

#
# def words(rinput):
#     l = []
#     l = re.findall(r'[a-z0-9]*\-*[a-z]+', rinput)
#     if l == []:
#         print("None")
#         return None
#     else:
#         print(l)
#         return l

#words(rinput)
#rinput = "919.555.1212"
#{"area_code": "919", "number": "555-1212"})
#
#
# def phone_number(rinput):
#     x = (re.findall(r'(\d{3})\D*(\d{3})\D*(\d{4})$', rinput))
#     try:
#         area_code = x[0][0]
#         number = "{}-{}".format(x[0][1], x[0][2])
#     except:
#         print("None")
#         return None
#     print({"area_code": area_code, "number": number})

#
# @params("input,expected", [
#     ("$4", {"currency": "$", "amount": 4.0}),
#     ("$19", {"currency": "$", "amount": 19.0}),
#     ("$19.00", {"currency": "$", "amount": 19.0}),
#     ("$3.58", {"currency": "$", "amount": 3.58}),
#     ("$1000", {"currency": "$", "amount": 1000.0}),
#     ("$1000.00", {"currency": "$", "amount": 1000.0}),
#     ("$1,000", {"currency": "$", "amount": 1000.0}),
#     ("$1,000.00", {"currency": "$", "amount": 1000.0}),
#     ("$5,555,555", {"currency": "$", "amount": 5555555.0}),
#     ("$5,555,555.55", {"currency": "$", "amount": 5555555.55}),
#     ("$45,555,555.55", {"currency": "$", "amount": 45555555.55}),
#     ("$456,555,555.55", {"currency": "$", "amount": 456555555.55}),
#     ("$1234567.89", {"currency": "$", "amount": 1234567.89}),
#     ("$12,34", None),
#     ("$1234.9", None),
#     ("$1234.999", None),
#     ("$", None),
#     ("31", None),
#     ("$$31", None),
# ])
#
#^\$\d+((\,\d{3})?)*(\.\d{2})?$
rinput = "$456,555,555.55"
a = 123
#print(format(amount, '.2f'))

def money(rinput):
    x = re.findall(r'^\$\d+(\,\d{3})*?\.?\d{2}?', rinput)
    print(x)
    try:
        amount = x[0][1:]
    except:
        return None
    print({"currency": "$", "amount": amount})


money(rinput)
#

# @params("input,expected", [
#     ("63936", {"zip": "63936", "plus4": None}),
#     ("50583", {"zip": "50583", "plus4": None}),
#     ("06399", {"zip": "06399", "plus4": None}),
#     ("26433-3235", {"zip": "26433", "plus4": "3235"}),
#     ("64100-6308", {"zip": "64100", "plus4": "6308"}),
#     ("7952", None),
#     ("115761", None),
#     ("60377-331", None),
#     ("8029-3924", None),
# ])
# def test_zip(input, expected):
#     assert s.zipcode(input) == expected
# rinput = "06399"
#
# def zipcode(rinput):
#     x =  re.findall(r'^\d{5}$|^\d{5}-\d{4}$', rinput)
#     try:
#         zip_code = x[0][:5]
#     except:
#         print("None")
#         return None
#     if x[0][6:]:
#         print(len(x[0]))
#         print({"zip": zip_code, "plus4": x[0][6:]})
#     else:
#         print({"zip": zip_code, "plus4": None})
#
#
# zipcode(rinput)
#
# ("9/4/1976", {"month": 9, "day": 4, "year": 1976}),
# ("1976-09-04", {"month": 9, "day": 4, "year": 1976}),
# ("2015-01-01", {"month": 1, "day": 1, "year": 2015}),
# ("02/15/2004", {"month": 2, "day": 15, "year": 2004}),
# ("9/4", None),
# ("2015", None),

# rinput = "9/4"
# #
# date_regex = [r"(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4}|\d{2})",
#                   r"(?P<year>\d{4})-?(?P<month>\d{2})-?(?P<day>\d{2})",
#                   r"(?P<day>\d{1,2})\s*(?P<month>[A-Za-z]{3})\s*(?P<year>\d{4})",
#                   r"(?P<month>[A-Za-z]{3})\s*(?P<day>\d{1,2})\s*,?\s*(?P<year>\d{4})"]
#
# for regex in date_regex:
#     match = re.match(regex, rinput)
#     if match:
#         return match
#
# for date in dates:
#     match = extract_date(date)
#     if match:
#         ddict = match.groupdict()
#         ddict = clean_date(**ddict)
#         ddict['orig'] = date
#
#         print("{orig}\t{month:02d}/{day:02d}/{year:d}".format(**ddict))
# @params("input,expected", [
#     ("""368 Agness Harbor
#      Port Mariah, MS 63293""",
#      {"address": "368 Agness Harbor", "city": "Port Mariah", "state": "MS",
#       "zip": "63293", "plus4": None}),
#     ("8264 Schamberger Spring, Jordanside, MT 98833-0997",
#      {"address": "8264 Schamberger Spring", "city": "Jordanside",
#       "state": "MT", "zip": "98833", "plus4": "0997"}),
#     ("Lake Joellville, NH", None),
# ])
# def test_address(input, expected):
#     assert s.address(input) == expected
# rinput = "368 Agness Harbor Port Mariah, MS 63293"
#
# def address(rinput):
#     print(rinput)
#     match = re.search(r"^(\d+[\w\s]+[\w\s]+) ([\w\s]+[\w\s]+), ([A-Z]{2}) (\d{5})$", rinput)
#     print(match)
#     if match:
#         address, city, state, zip_code = match.groups()
#         print("Address:", address, "City:", city, "State:", state, "Zip:", zip_code)
#
#
# address(rinput)
