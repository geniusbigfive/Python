import numpy
import pandas

gatTest = pandas.read_csv("gatTest.txt")


print(gatTest)
print(gatTest.info)


slipAmp = 3 #angle
speed = 5 #km/h
effectAngle = slipAmp *.5
slipSpeed = speed * numpy.sin(effectAngle/57.3)
print(slipSpeed)
