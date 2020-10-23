import numpy
import DyMat
import matplotlib.pyplot as plt


class AR:
    def __init__(self, param):
        self.resultName = param[0]
        self.testID = param[1]
        self.requestName = param[2]
        self.simTime = param[3]
        self.deltaTime = param[4]        
    
    def __del__(self):
        print("")
    
    def loadResult(self):
        res__ = DyMat.DyMatFile(self.resultName)
        res_ = {}
        # get result for dymola mat file
        for i, req in enumerate(self.requestName):
            res_[i] = res__.data(req)

        # make time for interpolation
        time = numpy.zeros(int(self.simTime/self.deltaTime))
        for i in range(1,int(self.simTime/self.deltaTime)):
            time[i] = time[i-1] + self.deltaTime

        # interpolation for equibalant time step
        res = numpy.zeros((len(time),len(res_)))
        for i in range(1,len(res_)):
            res[:,i] = numpy.interp(time,res_[0],res_[i])

        return res

    def RnH_stepSteer(self):
        nPI = 
        # step 01: load resuslt
        res = self.loadResult()

        # step 02 : calcualte PI
        PI = 

        return PI

