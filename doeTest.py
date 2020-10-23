import numpy as np
from scipy.interpolate import Rbf, InterpolatedUnivariateSpline

# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyDOE2 as DOE

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

kk = genDoe(3,'bbdesign')
print(len(kk))
# ub = [1,2,3]
# lb = [5,6,7]
# cu = [0,0,0]

# dd = conDOE(kk,cu,ub,lb)

# print(dd)

