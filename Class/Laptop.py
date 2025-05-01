class Laptop():
    def __init__(self, price, processor, RAM, OS):
        self.price=price
        self.processor=processor
        self.RAM=RAM
        self.OS=OS
    def boot(self):
        print(f"Booting Up {self.OS}")
        print("Please Wait...")
    def shutdown(self):
        print(f"Shutting Down {self.OS}")
    def restart(self):
        print(f"Restarting {self.OS}")
    def bios(self):
        print("Welcome to the BIOS")
    def get_info(self):
        return self.__dict__
    def set_info(self, price, processor, RAM, OS):
        self.price=price
        self.processor=processor
        self.RAM=RAM
        self.OS=OS
Windows = Laptop(63000, "AMD", "16GB", "Windows")
Windows.shutdown()
Windows.boot()
Windows.bios()
