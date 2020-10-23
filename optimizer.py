import pyDOE2 as DOE
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
from scipy.optimize import differential_evolution
from scipy.optimize import NonlinearConstraint, Bounds
import scipy
import numpy as np

class optimizer:
    def __init__(self, param):
        self.nDV = param[0]
        self.doeMethod = param[1]
    def __del__(self):
        print("")

#=========================================================================================================================
# doe tabel generator
#-------------------------------------------------------------------------------------------------------------------------
# nDV : number of design variable
# doeMethod : doe method (box - Becken, LHS, PB design)
#=========================================================================================================================
    def genDoe(self):
        if self.doeMethod == 'lhs':
            doeTable = DOE.lhs(self.nDV, samples = self.nDV*10)
        elif self.doeMethod == 'pbdesign':
            doeTable = DOE.pbdesign(self.nDV)
            temp = len(doeTable)-1
            for j in range(self.nDV):
                doeTable[temp, j] = 0
        elif self.doeMethod == 'bbdesign':
            doeTable = DOE.bbdesign(self.nDV, center=1)
        else:
            print("Error, You have to check a parameter")
        return doeTable

#=========================================================================================================================
# doe converte to integer to real
#-------------------------------------------------------------------------------------------------------------------------
# doeTable : doe table
# dvCu : current value of design variable
# dvUb : upper bound value of design variable
# dvLb : lower bound value of design variable
#=========================================================================================================================
    def conDOE(self, doeTable, dvUb, dvLb, dvCu):
        nRun = len(doeTable)
        nDV = len(np.transpose(doeTable))
        rDoeTable = np.zeros((nRun, nDV))
        for i in range(nRun):
            for j in range(nDV):
                if doeTable[i, j] == 1:
                    rDoeTable[i,j] = dvUb[j]
                elif doeTable[i, j] == -1:
                    rDoeTable[i,j] = dvLb[j]
                elif doeTable[i, j] == 0:
                    rDoeTable[i,j] = dvCu[j]
                else:
                    print("Error, You have to check a parameter")
        return rDoeTable

#=========================================================================================================================
# Meta model generator
#-------------------------------------------------------------------------------------------------------------------------
# doeTable : Design of Experiment table
# AR       : analysis response from simulation or test
# modelType : Meta model type (Kriging, Regression, RSM, RBF)
#=========================================================================================================================
    def genMetaModel(self, doeTable, AR, modelType):
        nDV = len(np.transpose(doeTable))
        nAR = len(np.transpose(AR))
        metaModel = []
        
        tempDV = []

        for i in range(nDV):
            tempDV.append(doeTable[:,i])

        for i in range(nAR):
            if modelType == 'rbf':
                for i in range(nAR):
                    metaModel.append(Rbf(*tempDV, AR[:,i],function='gaussian'))
            else:
                print("Error, You have to check a parameter")
        return metaModel

#=========================================================================================================================
# Object Function Definitinos
#-------------------------------------------------------------------------------------------------------------------------
# x        : new point 
# weight   : weight value for multi object function (you have to make same size than AR)
# ObjectFlag : Flag whether to use objective function (you have to define same size than AR, 0: dont use, 1: use)
# modelType : Meta model type (Kriging, Regression, RSM, RBF)
#=========================================================================================================================

    def objectFunction(self,metaModel,objectFlag,weight,x):
        objFunc = 0.
        nDV = 6
        tDV = []
        for i in range(nDV):
            tDV.append(x[i])

        for i in range(len(objectFlag)):
            if objectFlag[i] == 1:
                objFunc = weight[i]*metaModel[i](*tDV) + objFunc
        return  objFunc
#=========================================================================================================================
# Constratins Function Definitinos
#-------------------------------------------------------------------------------------------------------------------------
# x        : new point 
# constraintsFlag : Flag whether to use Constratins function (you have to define same size than AR, 0: dont use, 1: use)
# modelType : Meta model type (Kriging, Regression, RSM, RBF)
#=========================================================================================================================

    def constraintsFunction(self, metaModel,constraintsFlag,x):
        constraintsValue = []
        nDV = len(x)
        tDV = []
        for i in range(nDV):
            tDV.append(x[i])

        for i in range(len(constraintsFlag)):
            if constraintsFlag[i] == 1:
                constraintsValue.append(metaModel[i](*tDV))
        return  constraintsValue

#=========================================================================================================================
# NonlinearConstraint Definitinos
#-------------------------------------------------------------------------------------------------------------------------
# constraintsFunction : Constratins Function Definitinos
# lowerLimitValue : lower limit value of constraints
# upperLimitValue : upper limit value of constraints
#=========================================================================================================================
    def ConstraintFunction(self, constraintsFunction, lowerLimitValue, upperLimitValue):
        nlc = NonlinearConstraint(constraintsFunction, lowerLimitValue, upperLimitValue )
        return nlc

#=========================================================================================================================
# Side Constratint Definition
#-------------------------------------------------------------------------------------------------------------------------
#=========================================================================================================================


#=========================================================================================================================
# Find a optimum
#-------------------------------------------------------------------------------------------------------------------------
# constraintsFunction : Constratins Function Definitinos
# lowerLimitValue : lower limit value of constraints
# upperLimitValue : upper limit value of constraints
#=========================================================================================================================
# optimumRes = differential_evolution(objectFunction, bounds, args=( ), constraints=(nlc), strategy = 'randtobest1bin', init = 'latinhypercube', maxiter = 500, tol=1e-6, mutation=0.8, disp = True)

