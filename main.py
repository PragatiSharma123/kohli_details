from sensorModule import sensor
from my_sensor import Accelerometer, Gyro, GPS
import numpy as np

#define a accelerometer object
acc = Accelerometer(
    name="Accelerometer_v1",
    location="Haldia",
    record_date="2023-01-10"
)

gyro=Gyro(
     name="Accelerometer_v1",
    location="Haldia",
    record_date="2023-01-10"

)
gps = GPS(
    name="GPS_v1",
    location="Haldia",
    record_date="2023-01-10",
    brand="espressif"
)

#get data
time = np.arange
acc_data = np.random.randint(-20, 20, 10)
gyro_data= np.random.randint(-20, 20, 10)
gps_data=  np.random.randint(-20, 20, 10)

#add data to sensor
acc.add_data(data=acc_data, time=time)
gyro.add_data(data=gyro_data,time=time)
gps.add_data(data=gps_data, time=time)

#print data points
print("Accelerometer Data:", acc.data)
print("Gyroscope Data:", gyro.data)
print("GPS Data:",gps.data)
