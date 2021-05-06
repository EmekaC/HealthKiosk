import re, datetime

# Validation methods for inputs received before placing them in db
genders = ['Male','Female','Other']
statuses = ['Single','Married','Domestic Partnership','Divorced']
relations=['Mother','Father','Parent','Brother','Sister','Son','Daughter','Child','Friend','Spouse','Partner','Family member','Carer','Social worker','Guardian','Other']
communications = ['English','Maltese','Italian','French']


def validateString(value):
    if re.match("^[a-zA-Z ]*$",value):
        return True
    else:
        return False


def validateAddress(value):
    if re.match("^\d+\,\s?[A-z \s\-\']+\,+\s?[A-Z]{3}\s\d{4}$",value):
        return True
    else:
        return False

def validateCity(value):
    if re.match("^[A-z \-\']+\s?$",value):
        return True
    else:
        return False
    
def validateEmail(email):
    if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)",email):
        return True
    else:
        return False


def validateDOB(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
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
    
def validateSiblings(sib):
    if re.match("^[0-1]$",str(sib)):
        return True
    else:
        return False
    
def validateGender(gender):
    if validateString(gender) and (gender in genders):
       return True
    else:
        return False

def validateMartialStatus(status):
    if validateString(status) and (status in statuses):
       return True
    else:
        return False
    
def validateRelationship(relation):
    if validateString(relation) and (relation in relations):
       return True
    else:
        return False
    
def validateCommunication(communication):
    if validateString(relation) and (communication in communications):
        return True
    else:
        return False
    
def validateTemperature(temperature):
    if re.match("^(\d{2}|\d{0,5}\.\d{1,2})$",str(temperature)):
        return True
    else:
        return False 
    
def validateWeight(weight):
    if re.match("^(\d{2,3}|\d{0,5}\.\d{1,2})$",str(weight)):
        return True
    else:
        return False 

def validateHeartPulse(pulse):
    #range 60 - 210
    if re.match("^([6-9][0-9]|1[01]?[0-9][0-9]?|2[01][0])$",str(pulse)):
        return True
    else:
        return False 
    
def validateBloodOx(bloodOx):
    #80- 100
    if re.match("^([8-9][0-9])|(1[01][0])$",str(bloodOx)):
        return True
    else:
        return False
    
def validateDateTimestamp(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False
    
    