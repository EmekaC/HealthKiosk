from be.utils.validation import genders,relations,statuses,communications
from collections import defaultdict

d = defaultdict(lambda: len(d))

def getGenders():
    gender_id = [d[x] for x in genders]
    gender_dict = dict(zip(gender_id, genders))
    return gender_dict

def getRelations():
    relation_id = [d[x] for x in relations]
    relation_dict = dict(zip(relation_id, relations))
    return relation_dict
    

def getStatuses():
    status_id = [d[x] for x in statuses]
    status_dict = dict(zip(status_id, statuses))
    return status_dict

def getCommunications():
    communication_id = [d[x] for x in communications]
    communication_dict = dict(zip(communication_id, communications))
    return communication_dict
   