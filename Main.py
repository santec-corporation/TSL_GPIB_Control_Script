# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:07:59 2018

@author: chentir
"""
import sys
from PyQt5 import QtCore, QtWidgets,QtGui
import TSL_Control_Tool_GUI
import pyvisa as visa
import time
import functions

global TSL

################### FUNCTIONS DEFINITIONS #####################################
def LDON():
    TSL.write("POW:STAT 1")

def LDOFF():
    TSL.write("POW:STAT 0")

def PwrAuto():
    TSL.write('POW:ATT:AUT 1')
    
def PwrMan():
    TSL.write('POW:ATT:AUT 0')

def ShutOp():
    TSL.write('POW:SHUT 0')
    time.sleep(0.1)
    GetPwr()
    GetAtt()
    
def ShutClo():
    TSL.write('POW:SHUT 1')
    time.sleep(0.1)
    GetPwr()
    GetAtt()
    
def SetLambda():
    WriteLambda=round(float(ui.lambda_input.text()),4)
    functions.SetWL(WriteLambda)
    time.sleep(0.1)
    GetLambda()
    GetPwr()
    GetAtt()

def GetLambda():
    ui.lambda_disp.setText(functions.GetWL())
    
def SetPwr():
    WritePwr=round(float(ui.Pwr_input.text()),2)
    functions.SetPwr(WritePwr)
    time.sleep(0.1)
    GetPwr()
    GetAtt()
    
def GetPwr():
    ui.Pwr_disp.setText(functions.GetPwr())

def SetAtt():
    WriteAtt=round(float(ui.Att_input.text()),2)
    functions.SetAtt(WriteAtt)
    time.sleep(0.1)
    GetPwr()
    GetAtt()
          
def GetAtt():
    ui.Att_disp.setText(functions.GetAtt())

def Get_Data():
    WLstart=ui.lambdaStart_input.text()
    WLend=ui.lambdaEnd_input.text()
    Swp_mod=ui.Swp_mod_input.currentIndex()
    if Swp_mod==1 or Swp_mod==3:
        Arg1=ui.ScanSpeed_input.text()
        Arg2=ui.TriggStep_input.text()
        if ui.Swp_mod_input.currentIndexChanged:
            ui.frame_5.hide()
            ui.frame_4.show()
    else:
        Arg1=ui.Step_input.text()
        Arg2=ui.Dwell_input.text()
        ui.frame_5.show()
        ui.frame_4.hide()
    Cycle=ui.Repeat_input.text()
    return Swp_mod,WLstart,WLend,Arg1,Arg2,Cycle

def Auto_Start():
    Swp_mod,WLstart,WLend,Arg1,Arg2,Cycle=Get_Data()
    functions.Auto_Start(Swp_mod,WLstart,WLend,Arg1,Arg2,Cycle)

def Trig_Start():
    Swp_mod,WLstart,WLend,Arg1,Arg2,Cycle=Get_Data()
    functions.Trig_Start(Swp_mod,WLstart,WLend,Arg1,Arg2,Cycle)

def Del_change():
    functions.Del_change(ui.GPIB_DEL_input.currentIndex())

def CC_Off():
    TSL.write('COHC 0')

def CC_On():
    TSL.write('COHC 1')

def AM_ON():
    TSL.write('AM:STATE 1')
    
def AM_OFF():
    TSL.write('AM:STATE 0')

def TrigSrc():
    functions.TrigSrc(ui.TrigSrc_input.currentIndex())
    
def TrigMode():
    functions.TrigMode(ui.TrigMode_input.currentIndex())
    
def Stop():    
    TSL.write('WAV:SWE 0')


################### CODE START ################################################
app = QtCore.QCoreApplication.instance()
if app is None:
    app = QtWidgets.QApplication(sys.argv)
TSL_Control_Tool = QtWidgets.QMainWindow()
app.setStyle('Fusion')
ui = TSL_Control_Tool_GUI.Ui_TSL_Control_Tool()
ui.setupUi(TSL_Control_Tool)

icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("santec_logo_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
TSL_Control_Tool.setWindowIcon(icon)

def Connect():
    global TSL
    rm=visa.ResourceManager()
    listing=rm.list_resources()
    tools=[i for i in listing if 'GPIB' in i]
    for i in tools:
        buffer=rm.open_resource(i, read_termination='\r\n')
        if 'TSL' in buffer.query('*IDN?'):
            TSL= buffer
            
    ################### TOOL INFO #################################################
    IDN=TSL.query("*IDN?")
    info=IDN.split(",")
    ui.ProdName_disp.setText(str(info[1]))
    ui.SN_disp.setText(str(info[2]))
    ui.Firmware_disp.setText(str(info[3]))
    # return TSL

################### TOOL INITIALIZATION #######################################
    functions.Ini()
    time.sleep(0.5)
    GetLambda()
    GetPwr()
    GetAtt()

################### GRAPHIC ADDONS ############################################
ui.Att_input.hide()
ui.Att_go.hide()
ui.frame_5.hide()

def Field_select():
        if ui.Swp_mod_input.currentIndex()==1 or ui.Swp_mod_input.currentIndex()==3:
            ui.frame_5.hide()
            ui.frame_4.show()
        else:
            ui.frame_5.show()
            ui.frame_4.hide()

# if '550' in info[1]:
#         ui.TriggStep_input.setToolTip(str(float(TSL.query('WAV:SWE:SPE?'))/1000)+'nm ~ '+str(float(TSL.query('WAV:SWE:STOP?'))-float(TSL.query('WAV:SWE:STAR?')))+'nm')
# elif '710' in info[1]:
#     ui.TriggStep_input.setToolTip(str(float(TSL.query('WAV:SWE:SPE?'))/5000)+'nm ~ '+str(float(TSL.query('WAV:SWE:STOP?'))-float(TSL.query('WAV:SWE:STAR?')))+'nm')

# def Trig_tip():
#     try:
#         if '550' in info[1]:
#             ui.TriggStep_input.setToolTip(str(float(ui.ScanSpeed_input.text())/1000)+'nm ~ '+str(float(ui.lambdaEnd_input.text())-float(ui.lambdaStart_input.text()))+'nm')
#         elif '710' in info[1]:
#             ui.TriggStep_input.setToolTip(str(float(ui.ScanSpeed_input.text())/5000)+'nm ~ '+str(float(ui.lambdaEnd_input.text())-float(ui.lambdaStart_input.text()))+'nm')
#     except ValueError:
#         try:
#             if ui.ScanSpeed_input.text()=='':
#                 if '550' in info[1]:
#                     ui.TriggStep_input.setToolTip(str(float(TSL.query('WAV:SWE:SPE?'))/1000)+'nm ~ '+str(float(ui.lambdaEnd_input.text())-float(ui.lambdaStart_input.text()))+'nm')
#                 elif '710' in info[1]:
#                     ui.TriggStep_input.setToolTip(str(float(TSL.query('WAV:SWE:SPE?'))/5000)+'nm ~ '+str(float(ui.lambdaEnd_input.text())-float(ui.lambdaStart_input.text()))+'nm')
#         except ValueError:
#             try:
#                 if ui.lambdaEnd_input.text()=='':
#                     if '550' in info[1]:
#                         ui.TriggStep_input.setToolTip(str(float(ui.ScanSpeed_input.text())/1000)+'nm ~ '+str(float(TSL.query('WAV:SWE:STOP?'))-float(ui.lambdaStart_input.text()))+'nm')
#                     elif '710' in info[1]:
#                         ui.TriggStep_input.setToolTip(str(float(ui.ScanSpeed_input.text())/5000)+'nm ~ '+str(float(TSL.query('WAV:SWE:STOP?'))-float(ui.lambdaStart_input.text()))+'nm')
#             except ValueError:
#                 try:
#                     if ui.lambdaStart_input.text()=='':
#                         if '550' in info[1]:
#                             ui.TriggStep_input.setToolTip(str(float(ui.ScanSpeed_input.text())/1000)+'nm ~ '+str(float(ui.lambdaEnd_input.text())-float(TSL.query('WAV:SWE:STAR?')))+'nm')
#                         elif '710' in info[1]:
#                             ui.TriggStep_input.setToolTip(str(float(ui.ScanSpeed_input.text())/5000)+'nm ~ '+str(float(ui.lambdaEnd_input.text())-float(TSL.query('WAV:SWE:STAR?')))+'nm')
#                 except ValueError:
#                     if '550' in info[1]:
#                             ui.TriggStep_input.setToolTip(str(float(TSL.query('WAV:SWE:SPE?'))/1000)+'nm ~ '+str(float(TSL.query('WAV:SWE:STOP?'))-float(TSL.query('WAV:SWE:STAR?')))+'nm')
#                     elif '710' in info[1]:
#                         ui.TriggStep_input.setToolTip(str(float(TSL.query('WAV:SWE:SPE?'))/5000)+'nm ~ '+str(float(TSL.query('WAV:SWE:STOP?'))-float(TSL.query('WAV:SWE:STAR?')))+'nm')
                    
################### BUTTONS TO FUNCTION #######################################
ui.Connect.clicked.connect(Connect)
ui.LD_ON.clicked.connect(LDON)                                                  #Switch ON LD
ui.LD_OFF.clicked.connect(LDOFF)                                                #Switch OFF LD
ui.Pwr_auto.clicked.connect(PwrAuto)                                            #Switch to Auto Pwr
ui.Pwr_manual.clicked.connect(PwrMan)                                           #Switch to Manual Pwr
ui.shut_open.clicked.connect(ShutOp)                                            #Open Shutter
ui.shut_close.clicked.connect(ShutClo)                                          #Close Shutter
ui.lambda_go.clicked.connect(SetLambda)                                         #Set Wavelength
ui.lambda_input.editingFinished.connect(SetLambda)                              #Set Wavelength
ui.lambda_get.clicked.connect(GetLambda)                                        #Read Wavelength
ui.Pwr_input.editingFinished.connect(SetPwr)                                    #Set Pwr
ui.Pwr_go.clicked.connect(SetPwr)                                               #Set Pwr
ui.Pwr_get.clicked.connect(GetPwr)                                              #Read Pwr
ui.Att_input.editingFinished.connect(SetAtt)                                    #Set Attenuation
ui.Att_go.clicked.connect(SetAtt)                                               #Set Attenuation
ui.Att_get.clicked.connect(GetAtt)                                              #Read Attenuation
ui.Start.clicked.connect(Auto_Start)                                            #Start scanning
ui.SoftTrig.clicked.connect(Trig_Start)                                         #Start scanning with soft trigger
ui.Swp_mod_input.currentIndexChanged.connect(Field_select)                      #Change selectable fieds depending on sweep mode
ui.Swp_mode_go.clicked.connect(Field_select)                                    #Change selectable fieds depending on sweep mode
ui.Del_go.clicked.connect(Del_change)                                           #Change GPIB delimiter
ui.CC_OFF.clicked.connect(CC_Off)                                               #Switch off Coherence Contorl
ui.CC_ON.clicked.connect(CC_On)                                                 #Switch on Coherence Control
ui.Amp_Mod_ON.clicked.connect(AM_ON)                                            #Switch on Amplitude Modulation
ui.Amp_Mod_OFF.clicked.connect(AM_OFF)                                          #Switch off Amplitude Modulation
ui.TrigSrc_go.clicked.connect(TrigSrc)                                          #Change Trigger Input Source
ui.TrigMode_go.clicked.connect(TrigMode)                                        #Change Trigger Output Mode
ui.Stop.clicked.connect(Stop)                                                   #Stop scan (only works on soft trigger scanning mode)
# ui.ScanSpeed_input.textChanged.connect(Trig_tip)                                #Calculate min and max trigger step
# ui.lambdaStart_input.textChanged.connect(Trig_tip)                              #Calculate min and max trigger step
# ui.lambdaEnd_input.textChanged.connect(Trig_tip)                                #Calculate min and max trigger step
################### TOOL INFO #################################################
TSL_Control_Tool.show()
sys.exit(app.exec_())
