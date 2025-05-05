class Bus():
    def __init__(self):
        self.__private=9876543210
    def get_info(self):
        return self.__private
Bus1 = Bus()
print(Bus1.get_info()) # Correct
# print(Bus1.__private) # Wrong
