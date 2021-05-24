import time
from be import app, db
from  be.models.heart import Heart, heart_share_schema
from be.utils.max30100 import *
from be.utils.hrcalc import *


#get live results
def getData():
    print("Geting current results")
    hearts = Heart.query.order_by(Heart.id.desc()).first()
    if not hearts:
        return " no data"
    else:
        return heart_share_schema.dump(hearts)
    

def startReadingHeartBeat():
    mx30 = max30100.MAX30100()
    mx30.set_mode(max30100.MODE_SPO2)
    heatBeats = []
    sat = []

    timeout = time.time() + 30 # 30sec duration

    print("Starting readings: ")

    while not (time.time() > timeout):
        red,ir = mx30.read_sequential()
        hb,vB,o2,bO = hrcalc.calc_hr_and_spo2(ir,red)
        if((hb != -999) and (o2 != -999)):
            heatBeats.append(hb)
            sat.append(o2)
            newResult = Heart(hb,round(o2))
            db.session.add(newResult)
            db.session.commit()
            print("Heart beat: ",hb)
            print("O2: ",round(o2))


    avgHb = round(sum(heatBeats)/len(heatBeats))
    avgSat = round(sum(sat)/len(sat))
    print("Average heart beat is: ",avgHb)
    print("Average oxygen sat is: ",avgSat)
    mx30.reset()
    print("End --- Reset sensor")
    finalResult = Heart(avgHb,avgSat)
    return heart_share_schema.dump(finalResult)


def deleteData():
    print("Deleting data")
    Heart.query.delete()
    db.session.commit()
    return "Deleted successfully"
    
