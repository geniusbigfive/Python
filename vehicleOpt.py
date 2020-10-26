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


simStartTime = 1
simDeltaTime = 1/409.6
requestListFileName = "dymolaRequest.json"
numberRequest = 30
nameModel = "KIA_CAVALRY.Experiments.Chassis.HTT_Body_Free_20ch_Body_fixed"
namePackage = "C:/Users/ivh/Desktop/MJG/KIA_HTT/V01/KIA_CAVALRY/package.mo"
nameResult = "Res"
nameReqFileName = "HTT_Result"


paramSim = [nameModel,namePackage,nameResult,simStartTime, simDeltaTime, None, None,requestListFileName, numberRequest]
dymolaSim = dymolaAPI(paramSim)
dymolaSim.simulator()

paramAR =["C:/Users/ivh/Desktop/MJG/KIA_HTT/20201023/Res", None,dymolaSim.setRequest() ,simStartTime,simDeltaTime,nameReqFileName]
ar = AR(paramAR)
ar.writeMatFile()



# toKiaList = [
# "CAVALRY.axle1.leftLinkage.upperInnerJoints.toJoint1.frame_a.f[1]",
# "CAVALRY.axle1.leftLinkage.upperInnerJoints.toJoint1.frame_a.f[2]",
# "CAVALRY.axle1.leftLinkage.upperInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle1.leftLinkage.upperInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle1.leftLinkage.upperInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle1.leftLinkage.upperInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle1.leftLinkage.lowerInnerJoints.toJoint1.frame_a.f[1]",	
# "CAVALRY.axle1.leftLinkage.lowerInnerJoints.toJoint1.frame_a.f[2]",	
# "CAVALRY.axle1.leftLinkage.lowerInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle1.leftLinkage.lowerInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle1.leftLinkage.lowerInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle1.leftLinkage.lowerInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle1.leftLinkage.springMount.frame_b.f[1]",	
# "CAVALRY.axle1.leftLinkage.springMount.frame_b.f[2]",	
# "CAVALRY.axle1.leftLinkage.springMount.frame_b.f[3]",	
# "CAVALRY.axle1.leftLinkage.damperMount.frame_b.f[1]",	
# "CAVALRY.axle1.leftLinkage.damperMount.frame_b.f[2]",	
# "CAVALRY.axle1.leftLinkage.damperMount.frame_b.f[3]",	
# "CAVALRY.axle1.stabilizer.stabilizerMount.b1.frame_a.f[1]",	
# "CAVALRY.axle1.stabilizer.stabilizerMount.b1.frame_a.f[2]",	
# "CAVALRY.axle1.stabilizer.stabilizerMount.b1.frame_a.f[3]",	
# "CAVALRY.axle1.stabilizer.stabilizerMount.b2.frame_a.f[1]",	
# "CAVALRY.axle1.stabilizer.stabilizerMount.b2.frame_a.f[2]",	
# "CAVALRY.axle1.stabilizer.stabilizerMount.b2.frame_a.f[3]",	
# "CAVALRY.axle1.steering.rackPinion.rackFrame.f[1]",	
# "CAVALRY.axle1.steering.rackPinion.rackFrame.f[2]",	
# "CAVALRY.axle1.steering.rackPinion.rackFrame.f[3]",	
# "CAVALRY.axle1.steering.rackPinion.supportFrame.f[1]",	
# "CAVALRY.axle1.steering.rackPinion.supportFrame.f[2]",	
# "CAVALRY.axle1.steering.rackPinion.supportFrame.f[3]",
# "CAVALRY.axle1.leftBumpstopper.f",
# "CAVALRY.axle1.rightLinkage.upperInnerJoints.toJoint1.frame_a.f[1]",
# "CAVALRY.axle1.rightLinkage.upperInnerJoints.toJoint1.frame_a.f[2]",
# "CAVALRY.axle1.rightLinkage.upperInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle1.rightLinkage.upperInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle1.rightLinkage.upperInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle1.rightLinkage.upperInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle1.rightLinkage.lowerInnerJoints.toJoint1.frame_a.f[1]",	
# "CAVALRY.axle1.rightLinkage.lowerInnerJoints.toJoint1.frame_a.f[2]",	
# "CAVALRY.axle1.rightLinkage.lowerInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle1.rightLinkage.lowerInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle1.rightLinkage.lowerInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle1.rightLinkage.lowerInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle1.rightLinkage.springMount.frame_b.f[1]",	
# "CAVALRY.axle1.rightLinkage.springMount.frame_b.f[2]",	
# "CAVALRY.axle1.rightLinkage.springMount.frame_b.f[3]",	
# "CAVALRY.axle1.rightLinkage.damperMount.frame_b.f[1]",	
# "CAVALRY.axle1.rightLinkage.damperMount.frame_b.f[2]",	
# "CAVALRY.axle1.rightLinkage.damperMount.frame_b.f[3]",
# "CAVALRY.axle1.rightBumpstopper.f",	
# "CAVALRY.axle2.leftLinkage.upperInnerJoints.toJoint1.frame_a.f[1]",
# "CAVALRY.axle2.leftLinkage.upperInnerJoints.toJoint1.frame_a.f[2]",
# "CAVALRY.axle2.leftLinkage.upperInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle2.leftLinkage.upperInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle2.leftLinkage.upperInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle2.leftLinkage.upperInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle2.leftLinkage.lowerInnerJoints.toJoint1.frame_a.f[1]",	
# "CAVALRY.axle2.leftLinkage.lowerInnerJoints.toJoint1.frame_a.f[2]",	
# "CAVALRY.axle2.leftLinkage.lowerInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle2.leftLinkage.lowerInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle2.leftLinkage.lowerInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle2.leftLinkage.lowerInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle2.leftLinkage.springMount.frame_b.f[1]",	
# "CAVALRY.axle2.leftLinkage.springMount.frame_b.f[2]",	
# "CAVALRY.axle2.leftLinkage.springMount.frame_b.f[3]",	
# "CAVALRY.axle2.leftLinkage.damperMount.frame_b.f[1]",	
# "CAVALRY.axle2.leftLinkage.damperMount.frame_b.f[2]",	
# "CAVALRY.axle2.leftLinkage.damperMount.frame_b.f[3]",	
# "CAVALRY.axle2.stabilizer.stabilizerMount.b1.frame_a.f[1]",	
# "CAVALRY.axle2.stabilizer.stabilizerMount.b1.frame_a.f[2]",	
# "CAVALRY.axle2.stabilizer.stabilizerMount.b1.frame_a.f[3]",	
# "CAVALRY.axle2.stabilizer.stabilizerMount.b2.frame_a.f[1]",	
# "CAVALRY.axle2.stabilizer.stabilizerMount.b2.frame_a.f[2]",	
# "CAVALRY.axle2.stabilizer.stabilizerMount.b2.frame_a.f[3]",	
# "CAVALRY.axle2.leftLinkage.steerLink.toJoint1.frame_a.f[1]",	
# "CAVALRY.axle2.leftLinkage.steerLink.toJoint1.frame_a.f[2]",	
# "CAVALRY.axle2.leftLinkage.steerLink.toJoint1.frame_a.f[3]",
# "CAVALRY.axle2.leftBumpstopper.f",
# "CAVALRY.axle2.rightLinkage.upperInnerJoints.toJoint1.frame_a.f[1]",
# "CAVALRY.axle2.rightLinkage.upperInnerJoints.toJoint1.frame_a.f[2]",
# "CAVALRY.axle2.rightLinkage.upperInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle2.rightLinkage.upperInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle2.rightLinkage.upperInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle2.rightLinkage.upperInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle2.rightLinkage.lowerInnerJoints.toJoint1.frame_a.f[1]",	
# "CAVALRY.axle2.rightLinkage.lowerInnerJoints.toJoint1.frame_a.f[2]",	
# "CAVALRY.axle2.rightLinkage.lowerInnerJoints.toJoint1.frame_a.f[3]",	
# "CAVALRY.axle2.rightLinkage.lowerInnerJoints.toJoint2.frame_a.f[1]",	
# "CAVALRY.axle2.rightLinkage.lowerInnerJoints.toJoint2.frame_a.f[2]",	
# "CAVALRY.axle2.rightLinkage.lowerInnerJoints.toJoint2.frame_a.f[3]",	
# "CAVALRY.axle2.rightLinkage.springMount.frame_b.f[1]",	
# "CAVALRY.axle2.rightLinkage.springMount.frame_b.f[2]",	
# "CAVALRY.axle2.rightLinkage.springMount.frame_b.f[3]",	
# "CAVALRY.axle2.rightLinkage.damperMount.frame_b.f[1]",	
# "CAVALRY.axle2.rightLinkage.damperMount.frame_b.f[2]",	
# "CAVALRY.axle2.rightLinkage.damperMount.frame_b.f[3]",	
# "CAVALRY.axle2.rightLinkage.steerLink.toJoint1.frame_a.f[1]",	
# "CAVALRY.axle2.rightLinkage.steerLink.toJoint1.frame_a.f[2]",	
# "CAVALRY.axle2.rightLinkage.steerLink.toJoint1.frame_a.f[3]",
# "CAVALRY.axle2.rightBumpstopper.f"
# ]