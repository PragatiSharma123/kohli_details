from sensorModule import sensor

class Accelerometer(sensor):
    def show_type(self):
        print(f"I am an {self.name}")

class Gyro(Accelerometer):
    def show_type(self):
        print(f"This is {self.name} and location is at {self.location}")


class GPS(sensor):
     def __init__(self, name, location, record_date, brand):
         super().__init__(name, location, record_date)
         self.brand = brand