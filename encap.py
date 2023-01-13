class sensor():
    def __init__(self, name, location, record_date, version):
        self.name = name
        self.location = location
        self.record_date = "2023-01-10"
        self.__version = "0.001"
        self.data = {}


        def get_record_date(self):
            print(f"The record date for {self.name} is {self.__record_date}")

        def get_version(self):
            print(f"The version for {self.name} is {self.__version}")

            def set_version(self,version):
                self.__version = version
            print(f"The version for {self.name} is {self.__version}")

    def add_data(self, time, data):
        self.data["data"] = data
        self.data["time"] = time
        print(f"Received {len(data)} point")
        
    def clear_data(self):
        self.data = {}
        print("data cleared!!")

        sensor1 = sensor(
            name="sensor 1",
            location="kolkata"
        )
        print(sensor1.name)
        print(sensor1.location)
        #print(sensor1.__record_date)
        # print(sensor1.__version)
        sensor1.get_record_date()
        sensor1.get_version()
        sensor1.set_version("0.009")
        sensor1.get_version()