import numpy as np
from optimizer import optimizer
import platform
import DyMat
import time
import json
import sys
import matplotlib.pyplot as plt
import pandas as pd
import os
from dymola.dymola_interface import DymolaInterface
from dymola.dymola_exception import DymolaException

class dymolaAPI:
    def __init__(self,param):
        self.modelName = param[0]
        self.packageName = param[1]
        self.resultName = param[2]
        self.simTime = param[3]
        self.deltaTime = param[4]
        self.handleModelParamName = param[5]
        self.handleModelParamVal = param[6]

    def __dell__(self):
        print("")

    def translate(self):
        try:
            dymola = None
            dymola = DymolaInterface("/opt/dymola-2021-x86_64/bin64/dymola.sh")

            openResult = dymola.openModel(self.packageName)
            print("                    openModel : ", openResult )

            if not openResult:
                print("Model open failed. Below is the translation log.")
                log = dymola.getLastErrorLog()
                print(log)
                exit(1)
            
            transResult = dymola.translateModelExport(self.modelName)
            print("                    translateModel : ", transResult)
          
        except DymolaException as ex:
            print(("Error: " + str(ex)))
        finally:
            if dymola is not None:
                dymola.close()
                dymola = None
        return 0 

    def simulator(self):
        try:
            dymola = None
            dymola = DymolaInterface("/opt/dymola-2021-x86_64/bin64/dymola.sh")
            openResult = dymola.openModel(self.packageName)
            print("                    openModel : ", openResult )   
            if not openResult:
                print("openModel is failed. Below is the translation log.")
                log = dymola.getLastErrorLog()
                print(log)
                exit(1)
            dymola.experimentSetupOutput(events=False)
            result = dymola.simulateExtendedModel(self.modelName,0.0, self.simTime, 0, self.deltaTime, "Radau", 0.00001, self.deltaTime, self.resultName, initialNames=self.handleModelParamName, initialValues=self.handleModelParamVal)
            
            print("                    simulateExtendedModel : ", result[0])
            if not result[0]:
                print("Simulation is failed. Below is the translation log.")
                log = dymola.getLastErrorLog()
                print(log)
                exit(1)
            
        except DymolaException as ex:
            print(("Error: " + str(ex)))
        finally:
            if dymola is not None:
                dymola.close()
                dymola = None
        return 0 