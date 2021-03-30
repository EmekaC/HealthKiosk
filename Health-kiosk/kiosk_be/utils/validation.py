import re

def validateString(value):
    if re.match("^[a-zA-Z ]*$",value):
        return True
    else:
        return False


def validateEmail(email):
    if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
        return True
    else:
        return False


def validateDOB(date):
    if re.match("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$",date):
        return True
    else:
        return False


def validateMobile(mobile):
    mob = str(mobile)
    if re.match("^[79|99|77]{2}[0-9]{6}$",mob):
        return True
    else:
        return False

def validatePassword(password):
    if re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[^\w\s]).{8,14}$",password):
        return True
    else:
        return False

def validateId(id):
    if re.match("^[0-9]{7}(M|L|G|H){1}$",id):
        return True
    else:
        return False

