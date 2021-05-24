import board
import busio as io
import adafruit_mlx90614
import time
from be import app, db
from  be.models.temp import Temp, temp_share_schema

#get live results
def getData():
    print("Geting current results")
    temps = Temp.query.order_by(Temp.id.desc()).first()
    if not temps:
        return " no data"
    else:
        return temp_share_schema.dump(temps)
    
#Start sensor    
def startTempreture():
    timeout = time.time() + 40 #40 secs
    i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
    mlx = adafruit_mlx90614.MLX90614(i2c)

    print("Starting reading")
    while not (time.time() > timeout)::
        roomTemp = "{:.2f}".format(mlx.ambient_temperature)
        bodyTemp = "{:.2f}".format(mlx.object_temperature)
        newResult = Temp(bodyTemp)
        db.session.add(newResult)
        db.session.commit()
        time.sleep(1)

    print("End reading")
    finalResult = Temp(bodyTemp)
    print("Room Temperature is: ",roomTemp,"°C")
    print("Body Temperature is: ",bodyTemp,"°C")
    return temp_share_schema.dump(finalResult)

# Delete temporaly sensor data
def deleteData():
    print("Deleting data")
    Temp.query.delete()
    db.session.commit()
    return "Deleted successfully"


