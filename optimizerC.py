import pyDOE2 as DOE
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
from scipy.optimize import differential_evolution
from scipy.optimize import NonlinearConstraint, Bounds
import scipy
import numpy as np

class optimizer:
    def __init__(self):
        print("enterd optimizer")
    def 

#=========================================================================================================================
# doe tabel generator
#-------------------------------------------------------------------------------------------------------------------------
# nDV : number of design variable
# doeMethod : doe method (box - Becken, LHS, PB design)
#=========================================================================================================================
    def genDoe(nDV, doeMethod):
        if doeMethod == 'lhs':
            doeTable = DOE.lhs(nDV, samples = nDV*10)
        elif doeMethod == 'pbdesign':
            doeTable = DOE.pbdesign(nDV)
        elif doeMethod == 'bbdesign':
            doeTable = DOE.bbdesign(nDV, center=1)
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
    def conDOE(doeTable, dvUb, dvLb, dvCu):
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
    def genMetaModel(doeTable, AR, modelType):
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

    def objectFunction(metaModel,objectFlag,weight,x):
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

    def constraintsFunction(metaModel,constraintsFlag,x):
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
    def ConstraintFunction(constraintsFunction, lowerLimitValue, upperLimitValue):
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

dv_low = [8955.0, 48510.0, 3048.0, 8550.0, 51156.0, 1981.0]
dv_up = [10945.0, 59290.0, 3726.0, 10450.0, 62524.0, 2422.0]

x0 = [9950.0, 53900.0, 3387.761, 9500.0, 56840.0, 2202.2108122]

AR = np.array([[0.24917664, 5.04250217, 1.35341606],
       [0.23161277, 4.6834628 , 2.15557269],
       [0.24374156, 4.92964399, 1.71229204],
       [0.22759482, 4.60054697, 2.79965422],
       [0.28735857, 5.80867634, 0.05726655],
       [0.25843202, 5.22681173, 0.6879538 ],
       [0.32234092, 6.54398179, 0.        ],
       [0.2634901 , 5.32808162, 0.62277943]])

nDV = 6
doeTable = genDoe(nDV, 'pbdesign')

cDoeTable = conDOE(doeTable,dv_up,dv_low ,x0)
metaModel = genMetaModel(cDoeTable, AR, 'rbf')    

newDV = []

for i in range(6):
    newDV.append(cDoeTable[6,i])

newAR = metaModel[1](*newDV)
print(newAR)

objectFlag = [1,1,0]
weight = [1,1,0]
constraintsFlag = [1,1,1]

lowerLimitValue = [0.28735857,4.6834628]
upperLimitValue = [0.32234092,6.54398179] 

B=objectFunction(metaModel,objectFlag,weight,newDV)
print(B)
A=constraintsFunction(metaModel,constraintsFlag,newDV)
print(A)

# nlc =NonlinearConstraint(A, lowerLimitValue, upperLimitValue)

bounds = [(8955.0,10945.0), (48510.0,59290.0),(3048.0,3726.0),(8550.0,10450.0),(51156.0,62524.0),(1981.0,2422.0)]

