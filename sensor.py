class sensor():
    def __init__(self, name, location, record_date):
        self.name = name
        self.location = location
        self.record_date = record_date
        self.data = {}

    def add_data(self, time, data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)} point")
        
    def clear_data(self):
        self.data = {}
        print("data cleared!!")


import numpy as np

sensor1 = sensor(  
name = "sensor1",  
location = "Haldia",
record_date = "2023-01-09" 
) 

print(sensor1.name,sensor1.location,sensor1.record_date)

#generating random data points list of length 10
data=np.random.randint(-10, 10, 10)
#generating random time in seconds corresponding to the data points above
time = np.arange(10)
#adding the generated data points into the sensor object

sensor1.add_data( 
time=time,
data=data
)


#printing the sensor dictionary within the class
print(sensor1.data)
print("######################################")
class Accelerometer(sensor):
    def show_type(self):
        print(f"I am an {self.name}")

acc = Accelerometer(
     "accelerometer",
    "Haldia",
     "2023-01-09"
    )
    
acc.show_type()

acc_data = np.random.randint(-10, 10, 10)
acc_time = np.arange(10)


accel = Accelerometer(
    name="Accelerometer",
    location="Haldia",
    record_date="2023-01-09"
)

accel.add_data(
    data = acc_data,
    time = acc_time
)

accel.show_type()
# print("Accel2erometer Data:", acc.data)
class Gyro(Accelerometer):
    def show_type(self):
        print(f"This is {self.name} and location is at {self.location}")

gyro = Gyro(
    name="Gyroscope",
    location="Kolkata",
    record_date="2023-01-10"
)

gyro_data = np.random.randint(-25, 5, 10)
gyro_time = np.arange(10)
gyro.add_data(
    data=gyro_data,
    time=gyro_time
)
gyro.show_type()









