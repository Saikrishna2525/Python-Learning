# F = C * 9/5 + 32
from TempaturesCelcius import temperatures
print(list(map((lambda num : num * (9/5) + 32), temperatures)))
