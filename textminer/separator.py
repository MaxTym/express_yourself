import re


def words(input):
    l = []
    l = re.findall(r'[a-z0-9]*\-*[a-z]+', input)
    if l == []:
        return None
    else:
        return l


def phone_number(input):
    x = (re.findall(r'(\d{3})\D*(\d{3})\D*(\d{4})$', input))
    try:
        area_code = x[0][0]
        number = "{}-{}".format(x[0][1], x[0][2])
    except:
        return None
    return {"area_code": area_code, "number": number}


def money(input):
    x = re.findall(r'^\$\d+\.+\d{2}$', input)
    try:
        amount = x[0][1:]
    except:
        return None
    return {"currency": "$", "amount": amount}


def zipcode(input):
    x =  re.findall(r'^\d{5}$|^\d{5}-\d{4}$', input)
    try:
        zip_code = x[0][:5]
    except:
        return None
    if x[0][6:]:
        return {"zip": zip_code, "plus4": x[0][6:]}
    else:
        return({"zip": zip_code, "plus4": None})


def test_date(input):
    return re.findall('^\d{1,4}[-/]\d{2}[-/]\d{1,4}$', input)
