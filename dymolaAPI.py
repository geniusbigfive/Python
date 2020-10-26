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
import json

class dymolaAPI:
    def __init__(self,param):
        self.modelName = param[0]
        self.packageName = param[1]
        self.resultName = param[2]
        self.simTime = param[3]
        self.deltaTime = param[4]
        self.handleModelParamName = param[5]
        self.handleModelParamVal = param[6]
        self.fileRequest = param[7]
        self.numRequest = param[8]

    def __dell__(self):
        print("")

    def translate(self):
        try:
            dymola = None
            dymola = DymolaInterface("C:/Program Files/Dymola 2019 FD01/bin64/Dymola.exe")

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
            dymola = DymolaInterface("C:/Program Files/Dymola 2019 FD01/bin64/Dymola.exe")
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

    def setRequest(self):
        requestName= []
        for i in range(self.numRequest):
            requestName.append(i)

        with open(self.fileRequest) as json_file:
            json_data = json.load(json_file)

        requestName[0] = json_data["_time"]
        
        requestName[1] = json_data["frontSuspension"]["Left"]["spring"]["deflection"]
        requestName[2] = json_data["frontSuspension"]["Left"]["damper"]["rodAxialForce"]
        requestName[3] = json_data["frontSuspension"]["Left"]["upperArm"]["ballJoint"]["fx"]
        requestName[4] = json_data["frontSuspension"]["Left"]["upperArm"]["ballJoint"]["fy"]
        requestName[5] = json_data["frontSuspension"]["Left"]["lowerArm"]["ballJoint"]["fx"]
        requestName[6] = json_data["frontSuspension"]["Left"]["lowerArm"]["ballJoint"]["fy"]
        requestName[7] = json_data["frontSuspension"]["Left"]["tieRod"]["axialForce"]

        requestName[8] = json_data["frontSuspension"]["Right"]["spring"]["deflection"]
        requestName[9] = json_data["frontSuspension"]["Right"]["damper"]["rodAxialForce"]
        requestName[10] = json_data["frontSuspension"]["Right"]["upperArm"]["ballJoint"]["fx"]
        requestName[11] = json_data["frontSuspension"]["Right"]["upperArm"]["ballJoint"]["fy"]
        requestName[12] = json_data["frontSuspension"]["Right"]["lowerArm"]["ballJoint"]["fx"]
        requestName[13] = json_data["frontSuspension"]["Right"]["lowerArm"]["ballJoint"]["fy"]
        requestName[14] = json_data["frontSuspension"]["Right"]["tieRod"]["axialForce"]

        requestName[15] = json_data["rearSuspension"]["Left"]["spring"]["deflection"]
        requestName[16] = json_data["rearSuspension"]["Left"]["damper"]["rodAxialForce"]
        requestName[17] = json_data["rearSuspension"]["Left"]["upperArm"]["ballJoint"]["fx"]
        requestName[18] = json_data["rearSuspension"]["Left"]["upperArm"]["ballJoint"]["fy"]
        requestName[19] = json_data["rearSuspension"]["Left"]["lowerArm"]["ballJoint"]["fx"]
        requestName[20] = json_data["rearSuspension"]["Left"]["lowerArm"]["ballJoint"]["fy"]

        requestName[21] = json_data["rearSuspension"]["Right"]["spring"]["deflection"]
        requestName[22] = json_data["rearSuspension"]["Right"]["damper"]["rodAxialForce"]
        requestName[23] = json_data["rearSuspension"]["Right"]["upperArm"]["ballJoint"]["fx"]
        requestName[24] = json_data["rearSuspension"]["Right"]["upperArm"]["ballJoint"]["fy"]
        requestName[25] = json_data["rearSuspension"]["Right"]["lowerArm"]["ballJoint"]["fx"]
        requestName[26] = json_data["rearSuspension"]["Right"]["lowerArm"]["ballJoint"]["fy"]

        return requestName