import sys
import ac
import acsys
import platform
import os
from third_party.sim_info import *



appName = ">YOUR APP NAME HERE<"
width, height = 800 , 800

simInfo = SimInfo()

def acMain(ac_version):
    global appWindow

    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, width, height)

    ac.addRenderCallback(appWindow, appGL)

    return appName

def appGL(deltaT):#-------------------------------- OpenGL UPDATE
    pass




def acUpdate(deltaT):#-------------------------------- AC UPDATE
    pass
