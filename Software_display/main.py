from tkinter import *
from artificialhorizon import ArtificialHorizon
import math
import serial
import serial.tools.list_ports
import time
from repeatingtimer import RepeatingTimer

ser = serial.Serial(timeout = None)
ser.baudrate = 9600
ser.port = 'COM2'

def read_serial():
    fila = ser.in_waiting;
    if fila > 10:
        msg = ser.readline()
        msg_deco = msg.decode("utf-8")
        valor = msg_deco.split(";")
        for i in range(len(valor)):
            valor[i] = int(valor[i])

        #roll;pitch;yaw;lat1;lat2;long1;long2;speed;
        if len(valor) == 8:
            roll = valor[0]
            pitch = valor[1]
            yaw = valor[2]
            lat1 = valor[3]
            lat2 = valor[4]
            long1 = valor[5]
            long2 = valor[6]
            speed = valor[7]
            lat = lat1*10000 + lat2
            long = long1*10000 + long2
            ah.update_roll(roll)
            ah.update_yaw(yaw)
            ah.update_pitch(pitch)
            ah.update_speed(speed)
            ah.update_coords(lat, long)        

t = RepeatingTimer(0.05, read_serial)

def slider(val):
    ah.update_roll(int(val)/100)

def slidep(val):
    ah.update_pitch(int(val)/100)

def slidey(val):
    ah.update_yaw(int(val)/100)
    
def refresh():
    COMports_dropbox['menu'].delete(0, 'end')
    COMports = []
    for i in serial.tools.list_ports.comports(include_links=False):
        COMports.append(i)
    for COMport in COMports:
        COMports_dropbox['menu'].add_command(label=COMport, command=lambda new_com = COMport: COMselected.set(new_com))
def baud_select(option):
    ser.baudrate = int(option)

def com_select(option):
    ser.port = option[0]

def open_serial():
    try:
        ser.open()
        time.sleep(1)
        button_open.config(state = DISABLED)
        button_close.config(state = NORMAL)
        t.start()
    except:
        print("erro ao abrir a porta COM")

def close_serial():
    try:
        t.cancel()
        ser.close()
        time.sleep(1)
        button_close.config(state = DISABLED)
        button_open.config(state = NORMAL)
        

    except:
        print("erro ao fechar a porta COM")

ah = ArtificialHorizon(800, 800)


COMports = []
for i in serial.tools.list_ports.comports(include_links=False):
    COMports.append(i)
COMselected = StringVar()
if not COMports:
    COMports.append("Nenhuma COM detectada")
COMselected.set(COMports[0])
COMports_dropbox = OptionMenu(ah.root, COMselected, *COMports, command = com_select)
baudrate = [
    "1200",
    "2400",
    "4800",
    "9600",
    "19200",
    "38400",
    "57600",
    "115200"
]
baudselected = StringVar()
baudselected.set(baudrate[3])
Baud_dropbox = OptionMenu(ah.root, baudselected, *baudrate, command = baud_select)
button_refresh = Button(ah.root,text = "Refresh COMports", command = refresh)
button_open = Button(ah.root,text = "Open", command = open_serial)
button_close = Button(ah.root,text = "Close", command = close_serial, state = DISABLED)

COMport_window = ah.canvas_AH.create_window(0.01*ah.width , 0.95*ah.height, anchor=NW, window=COMports_dropbox)
Baud_window = ah.canvas_AH.create_window(0.01*ah.width , 0.85*ah.height, anchor=NW, window=Baud_dropbox)
refresh_window = ah.canvas_AH.create_window(0.15*ah.width, 0.90*ah.height, anchor=NW, window=button_refresh)
open_window = ah.canvas_AH.create_window(0.01*ah.width, 0.90*ah.height, anchor=NW, window=button_open)
close_window = ah.canvas_AH.create_window(0.08*ah.width, 0.90*ah.height, anchor=NW, window=button_close)
 
roll = Scale(ah.root,  from_ = -math.pi*100, to = math.pi*100, orient = HORIZONTAL, command = slider)
pitch = Scale(ah.root,  from_ = -math.pi*100, to = math.pi*100, command = slidep)
yaw = Scale(ah.root,  from_ = 0, to = 2*math.pi*100,  orient = HORIZONTAL, command = slidey)
roll.grid(row = 0, column = 1)
yaw.grid(row = 0, column = 2)
pitch.grid(row = 0, column = 3)

ah.show()

