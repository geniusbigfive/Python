import matplotlib.pyplot as plt
import pyDOE2 as DOE
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline
from scipy.optimize import differential_evolution
from scipy.optimize import NonlinearConstraint, Bounds
import scipy
import numpy as np

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
        doeTable = DOE.bbdesign(nDV)
    else:
        print("Error, You have to check a parameter")
    return doeTable

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

    for i in range(nAR):
        print(i)
    if modelType == 'rbf':
        for i in range(nAR):
            metaModel.append(Rbf(*doeTable, AR[:,i], function='gaussian'))
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
# define object function define
nDV = 6
doeTable = genDoe(nDV, 'bbdesign')
AR= []
metaModel = genMetaModel(doeTable, AR, 'rbf')
objectFlag = []
weight = []

def objectFunction(x):
    objFunc = 0.
    for i in range(len(objectFlag)):
        if objectFlag(i) == 1:
            objFunc = weight(i)*metaModel[i](x) + objFunc
    return  objFunc
#=========================================================================================================================
# Constratins Function Definitinos
#-------------------------------------------------------------------------------------------------------------------------
# x        : new point 
# constraintsFlag : Flag whether to use Constratins function (you have to define same size than AR, 0: dont use, 1: use)
# modelType : Meta model type (Kriging, Regression, RSM, RBF)
#=========================================================================================================================
constraintsFlag = []
def constraintsFunction(x):
    constraintsValue = []
    for i in range(len(constraintsFlag)):
        if constraintsFlag(i) == 1:
            constraintsValue.append(metaModel[i](x))
    return  constraintsValue

#=========================================================================================================================
# NonlinearConstraint Definitinos
#-------------------------------------------------------------------------------------------------------------------------
# constraintsFunction : Constratins Function Definitinos
# lowerLimitValue : lower limit value of constraints
# upperLimitValue : upper limit value of constraints
#=========================================================================================================================
lowerLimitValue = []
upperLimitValue = [] 
nlc = NonlinearConstraint(constraintsFunction, lowerLimitValue, upperLimitValue ) 

#=========================================================================================================================
# Side Constratint Definition
#-------------------------------------------------------------------------------------------------------------------------
#=========================================================================================================================
bounds = [(0., 5.), (0., 5.)]

#=========================================================================================================================
# Find a optimum
#-------------------------------------------------------------------------------------------------------------------------
# constraintsFunction : Constratins Function Definitinos
# lowerLimitValue : lower limit value of constraints
# upperLimitValue : upper limit value of constraints
#=========================================================================================================================
# optimumRes = differential_evolution(objectFunction, bounds, args=( ), constraints=(nlc), strategy = 'randtobest1bin', init = 'latinhypercube', maxiter = 500, tol=1e-6, mutation=0.8, disp = True)



# setup data
x=[]
xx =[]
x2 = np.linspace(0, 10, 9)
x1 = np.linspace(0, 10, 9)
# xx = list([x1, x2])
xx.append(x1) 
xx.append(x2) 

x.append(np.linspace(0,10,9))
# x = np.transpose(x)
print(len(x))
print(len(np.transpose(x)))

y = np.sin(x[0])
xi = np.linspace(0, 10, 101)
print(xi)

rbf=[]

print(len(xx), len(y))

rbf.append( Rbf(*xx, y, epsilon=2, function='gaussian'))
print(xi.shape)

# use fitpack2 method
# ius = InterpolatedUnivariateSpline(x[1], y)
# yi = ius(xi)

# plt.subplot(2, 1, 1)
# plt.plot(x, y, 'bo')
# plt.plot(xi, yi, 'g')
# plt.plot(xi, np.sin(xi), 'r')
# plt.title('Interpolation using univariate spline')

# use RBF method
# rbf=[]
# rbf.append(Rbf(x[1], y, epsilon=2, function='gaussian'))
# rbf[1] = Rbf(x, y, epsilon=2, function='gaussian')
# print(rbf)
fi = rbf[0](1,2)
print(fi)
# plt.subplot(2, 1, 2)
# # plt.plot(x, y, 'bo')
# plt.plot(xi, fi, 'g')
# plt.plot(xi, np.sin(xi), 'r')
# plt.title('Interpolation using RBF - multiquadrics')
# plt.savefig('rbf1d.png')
# plt.show()