import numpy as np
from optimizer import optimizer
from dymolaAPI import dymolaAPI
from analysisResponse import AR

# define dymola sim env
import platform
import DyMat
import time
import json
import sys
import matplotlib.pyplot as plt
import pandas as pd
import os
import pyDOE2 as DOE


paramOpt = [2,'pbdesign', 3,3]
paramSim = ["VSDL.JTurn","/home/bigfive/Bigfive/Research/python/optimizer/VSDL/package.mo",'Res',10, 0.01, None, None]
requestList = ["_time.y","vehicle.controlBus.chassisBus.yawRate","vehicle.controlBus.chassisBus.lateralAcceleration"]
paramAR =["VSDL/Res", None,requestList ,10,0.01]

# opt = optimizer(paramOpt)
# table = opt.genDoe()

dymolaSim = dymolaAPI(paramSim)
# dymolaSim.translate()
# dymolaSim.simulator()

ar = AR(paramAR)
ar.loadResult()




