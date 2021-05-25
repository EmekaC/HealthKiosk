from random import randrange
import time
from be import app, db
from  be.models.temp import Temp, temp_share_schema

#get live results
def getTestData():
    print("Geting current results")
    temps = Temp.query.order_by(Temp.id.desc()).first()
    if not temps:
        return " no data"
    else:
        return temp_share_schema.dump(temps)
    
#Start sensor    
def startTestTempreture():
    print("Starting readings")
    for i in range(20):
        bodyTemp = randrange(31,40,1)
        newResult = Temp(bodyTemp)
        db.session.add(newResult)
        db.session.commit()
        time.sleep(1)
    print("end")
    return temp_share_schema.dump(newResult)

# Delete temporaly sensor data
def deleteTestData():
    print("Deleting data")
    Temp.query.delete()
    db.session.commit()
    return "Deleted successfully"


