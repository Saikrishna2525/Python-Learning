class Bus():
    def __init__(self):
        self._private=9876543210
    def get_info(self):
        return self._private
Bus1 = Bus()
print(Bus1.get_info()) # Correct
# print(Bus1._private) # Correct but should not use
