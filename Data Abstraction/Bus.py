# from abc import ABC, abstractmethod
# class Bus(ABC):
#     def __init__(self, var):
#         self.var=var
#     @abstractmethod
#     def move(self):
#         print("Wroom!")
#     def get_info(self):
#         return self.var
# Bus1 = Bus(123)
# # Bus1.get_info() # Wrong
# class BusInherited(Bus):
#     def __init__(self, var):
#         super().__init__(var)
#     def move(self):
#         print("Wroom!")
# Bus2 = BusInherited(123) # WRONG
