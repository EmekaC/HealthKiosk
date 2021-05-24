from be import app, db
from  be.models.heart import Heart, heart_share_schema
from random import randrange
import time


#get results
def getData():
    print("Geting current results")
    hearts = Heart.query.order_by(Heart.id.desc()).first()
    if not hearts:
        return " no data"
    else:
        return heart_share_schema.dump(hearts)
    
    
def startReading():
    print("Starting readings")
    for i in range(20):
        hb = randrange(50,200,1)
        oxy = randrange(70,100,10)
        newResult = Heart(hb,oxy)
        db.session.add(newResult)
        db.session.commit()
        time.sleep(1)
    print("end")
    return heart_share_schema.dump(newResult)
   
def deleteData():
    print("Deleting data")
    Heart.query.delete()
    db.session.commit()
    return "Deleted successfully"
    