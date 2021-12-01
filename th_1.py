#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 

@author: lars
"""

###########################_Einbindung_import_#################################
###############################################################################
import time
#from can import Message
#import can
# from bitarray import bitarray
import os
import subprocess
import threading

##Einbindung der Module
import GUI_IO
import sRam

###########################_Funktionen_########################################
###############################################################################


################################_THREAD_#######################################

def func_th_1_thread(list,q,string):
    print(string)
    beginn = True

    lesen_RamSec = sRam.RamSec()

    schreiben_CANData = sRam.CAN_Data()
    lesen_CANData = sRam.CAN_Data()

    bus = can.Bus(  interface='socketcan',
                    channel='can0',
                    receive_own_messages=True   )

   
    time.sleep(2)
    ##Endlosschleife (verlassen nur durch Abrechen)
    while beginn == True:

        if lesen_RamSec.start_all[0] == 1:
            print("Thread_1 Daten loggen wird aufgebaut")

            ##Lesen der Busbotschaften die von der Antenne gesendet werden
            for msg in bus:
                #print("Zeitstempel:{} ; Arbit_ID:{} ; Daten:{}".format(msg.timestamp, msg.arbitration_id, msg.data))

                # try:
                if msg.arbitration_id == 10:
                    x_msg = list(msg.data)
                    # schreibenPos.funcXClear()
                    # schreibenPos.funcXmsg(  x_msg[0],
                    #                         x_msg[5],
                    #                         x_msg[6],
                    #                         x_msg[7]    )
                    # print("X-Richtung: " + str(x_msg))

                if lesen_RamSec.start_all[0] == 0:
                    beginn = False
                    break
                #     #sys.exit()

        else:
            ##Start kann nicht durchgeführt werden
            print("Thread_1 Daten loggen nicht hergestellt")
            if lesen_RamSec.beenden[0] == 1:
                beginn = False
                break
                #sys.exit()

    print("Thread_1 Daten loggen wird geschlossen!" + '-' * 60)