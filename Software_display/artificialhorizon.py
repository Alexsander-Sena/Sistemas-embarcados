from tkinter import *
import math

class ArtificialHorizon():
    def __init__(self, w, h, **kwargs):
        self.root = Tk()
        self.root.title('Artificial Horizon')
        self.roll = 0
        self.pitch = 0
        self.yaw = 0
        self.width = w
        self.height = h

        if 'skycolor' in kwargs:
            self.skycolor = kwargs['skycolor']
        else:
            self.skycolor = "blue"

        self.canvas_AH = Canvas(self.root, width=w, heigh=h, bg=self.skycolor)

        
        if 'pitch_dy' in kwargs:
            self.pitch_y = kwargs['pitch_dy']
        else:
            self.pitch_y = self.height/12
        
        if 'pitch_ll' in kwargs:
            self.pitch_line_length = kwargs['pitch_ll']
        else:
            self.pitch_line_length = self.width/5
        
        if 'pitch_lc' in kwargs:
            self.pitch_line_color = kwargs['pitch_lc']
        else:
            self.pitch_line_color = "white"
        
        self.horizon = Horizon(self.canvas_AH, self.pitch_line_length, self.pitch_y, self.pitch_line_color, 3, self.width, self.height)


        if 'planecolor' in kwargs:
            self.planecolor = kwargs['planecolor']
        else:
            self.planecolor = "black"
        
        if 'planescale' in kwargs:
            self.planescale = kwargs['planescale']
        else:
            self.planescale = 1/4

        self.plane = Plane(self.canvas_AH, self.width, self.height, self.planescale, self.planecolor, 4) 


        if 'compasscolor' in kwargs:
            self.compasscolor = kwargs['compasscolor']
        else:
            self.compasscolor = "white"
        
        if 'compassscale' in kwargs:
            self.compassscale = kwargs['compassscale']
        else:
            self.compassscale = self.width/20
        self.compass = Compass(self.canvas_AH, w, h, self.compassscale,self.compasscolor, 4)

        if 'textcolor' in kwargs:
            self.textcolor = kwargs['textcolor']
        else:
            self.textcolor = "black"
        self.speed_text = self.canvas_AH.create_text(w - 75, h/2 - 25, text = "speed: 0", font = ('Calibri', '24'), fill = self.textcolor)
        self.lat_text = self.canvas_AH.create_text(w - 80, h/2, text = "lat: 0", font = ('Calibri', '16'), fill = self.textcolor)
        self.long_text = self.canvas_AH.create_text(w - 75, h/2 + 25, text = "long: 0", font = ('Calibri', '16'), fill = self.textcolor)


    def show(self):
        self.canvas_AH.grid(row = 0,column = 0)
        self.root.mainloop()

    def update_roll(self, roll):
        self.roll = roll
        self.horizon.update(self.roll, self.pitch)
    
    def update_pitch(self, pitch):
        self.pitch = pitch
        self.horizon.update(self.roll, pitch)
    
    def update_yaw(self, yaw):
        self.yaw = yaw
        self.compass.upadte(self.yaw)
    
    def update_speed(self, speed):
        self.canvas_AH.itemconfigure(self.speed_text, text = "speed: " + str(int(speed)))
    
    def update_coords(self, lat, long):
        self.canvas_AH.itemconfigure(self.lat_text, text ="lat: " + str(lat))
        self.canvas_AH.itemconfigure(self.long_text, text ="long: " + str(long))


    
class Plane():
    def __init__(self, canvas, w, h, scale, color, stroke):
        self.canvas = canvas
        self.width = w
        self.height = h
        self.left_wing = self.canvas.create_line( self.width/2 - self.width*scale, self.height/2, self.width/2 - self.width*scale/4, self.height/2, fill = color, width = stroke)
        self.right_wing = self.canvas.create_line( self.width/2 + self.width*scale/4,self.height/2, self.width/2 + self.width*scale, self.height/2, fill = color, width = stroke)
        self.arc = self.canvas.create_arc( self.width/2 -self.width*scale/4, self.height/2 - self.width*scale/4, self.width/2 + self.width*scale/4, self.height/2 + self.width*scale/4, width = stroke, start = 180, extent = 180, style= "arc", outline = color)
        self.point = self.canvas.create_oval( self.width/2 - stroke, self.height/2 - stroke, self.width/2 + stroke, self.height/2 + stroke, fill = color)

class Compass():
    def __init__(self, canvas, w, h, size, color, stroke):
        self.width = w
        self.height = h
        self.size = size
        self.canvas = canvas
        self.lines = []
        self.sublines = []
        self.text = []
        self.compass_rose = ["N", "NNE", "NE", "NEE", "E", "SEE", "SE", "SSE", "S", "SSW", "SW", "SWW", "W", "NWW", "NW", "NNW"]
        self.angle_text = canvas.create_rectangle(0, 0, w,size+ 20, fill = "gray", outline = "gray", width = 3)
        for i in range(0, 16):
            self.lines.append(canvas.create_line(w/2 + i*size*5, 0, w/2 + i*size*5, size, fill = color, width = stroke))
            self.sublines.append(canvas.create_line(w/2 + (i + 0.5)*size*5, 0, w/2 + (i + 0.5)*size*5, size * 3/4, fill = color, width = stroke - 1))
            self.text.append(canvas.create_text(w/2 + i*size*5, size + 10, text = self.compass_rose[i], font = ('Calibri', '14'), fill = color))
        self.angle_text = canvas.create_text(w/2, 15, text = str(0) + "°", font = ('Calibri', '24'), fill = "black")
        self.middle_line = canvas.create_polygon(w/2, size + 20, w/2 + 10, size + 40, w/2 - 10, size + 40, fill = "black" , width = stroke - 2)

    def upadte(self, yaw):
        yaw_d = yaw*180/math.pi
        self.canvas.itemconfigure(self.angle_text, text = str(int(yaw_d)) + "°")

        delta_x = yaw_d * self.size * 80 / 360
        
        for i in range(0, 16):
            #new points for the lines and text
            x = self.width/2 + i*self.size*5 - delta_x
            y0 = 0
            y1 = self.size
            if x <= 0:
                x = x + self.size * 80
            elif x >= self.size * 80:
                x = x - self.size * 80
            self.canvas.coords(self.text[i], x, y1 + 10)
            self.canvas.coords(self.lines[i], x, y0, x, y1)

            #new points for the sublines
            x = self.width/2 + (i + 0.5)*self.size*5 - delta_x
            y0 = 0
            y1 = self.size*3/4
            if x <= 0:
                x = x + self.size * 80
            elif x >= self.size * 80:
                x = x - self.size * 80
            self.canvas.coords(self.sublines[i], x, y0, x, y1)
            

class Horizon():
    def __init__(self, canvas, length, pitch_y, color, stroke, w, h):
        self.horizon = canvas.create_polygon(0, h/2, w , h/2, w, h, 0, h, fill="brown", width = 3, outline = "brown")
        self.canvas = canvas
        self.width = w
        self.height = h
        self.length = length
        self.pitch_y = pitch_y
        self.pitch_factor = 0
        self.lines = []
        self.sublines = []
        self.textl = []
        self.textr = []
        center_x = w/2
        center_y = h/2
        for i in range(-9, 10):
            if i >= 0:
                length = self.length + 20*i
            else: 
                length = self.length - 20*i
            self.lines.append(canvas.create_line(center_x - length/2, center_y + pitch_y * i, center_x + length/2, center_y + pitch_y * i, fill = color, width = stroke))
            self.sublines.append(canvas.create_line(center_x - 3*length/8, center_y + pitch_y * (i + 0.5), center_x + 3*length/8, center_y + pitch_y * (i + 0.5), fill = color, width = stroke - 1))
            self.textl.append(canvas.create_text(center_x - (length/2 + 20), center_y - pitch_y * i, text = str(i*10), font = ('Calibri', '14'), fill = color))
            self.textr.append(canvas.create_text(center_x + (length/2 + 20), center_y - pitch_y * i, text = str(i*10), font = ('Calibri', '14'), fill = color))
    
    def update(self, roll, pitch):
        self.pitch_factor = (self.pitch_y * pitch * 180/ math.pi)/10
        roll_factor = math.tan(roll)* self.width/2
        if roll <= math.pi/4 and roll >= - math.pi/4:
            pitch_factor_y = self.pitch_factor / math.cos(roll)
            x0 = 0
            y0 = self.height/2 + roll_factor + pitch_factor_y
            x1 = self.width
            y1 = self.height/2 - roll_factor + pitch_factor_y
            x2 = self.width
            y2 = self.height
            x3 = 0
            y3 = self.height

        elif roll <= 3*math.pi/4 and roll > 0:
            pitch_factor_x = self.pitch_factor / math.sin(roll)
            x0 = self.width/2 - (self.height/2)/math.tan(roll) + pitch_factor_x
            y0 = self.height
            x1 = self.width/2 + (self.height/2)/math.tan(roll) + pitch_factor_x
            y1 = 0
            x2 = self.width
            y2 = 0
            x3 = self.width
            y3 = self.height
        
        elif roll >= - 3*math.pi/4 and roll < 0:
            pitch_factor_x = self.pitch_factor / math.sin(roll)
            x0 = self.width/2 + (self.height/2)/math.tan(roll) + pitch_factor_x
            y0 = 0
            x1 = self.width/2 - (self.height/2)/math.tan(roll) + pitch_factor_x
            y1 = self.height
            x2 = 0
            y2 = self.height
            x3 = 0
            y3 = 0
        
        else:
            pitch_factor_y = self.pitch_factor / math.cos(roll)
            x0 = self.width
            y0 = self.height/2 - roll_factor + pitch_factor_y
            x1 = 0
            y1 = self.height/2 + roll_factor + pitch_factor_y
            x2 = 0
            y2 = 0
            x3 = self.width
            y3 = 0

        self.canvas.coords(self.horizon, x0, y0, x1, y1, x2, y2, x3, y3)

        #delta y
        delta_x = math.sin(roll) * self.pitch_y
        delta_y = math.cos(roll) * self.pitch_y 

        #delta pitch
        pitch_factor_x  = self.pitch_factor*math.sin(roll)
        pitch_factor_y = self.pitch_factor*math.cos(roll)

        for i in range(-9,10):
            if i >= 0:
                length = self.length + 20*i
            else: 
                length = self.length - 20*i
            #delta for the lines
            lines_delta_x = math.cos(roll) * length/2
            lines_delta_y = math.sin(roll) * length/2 

            #delta for the sublines
            sublines_delta_x = math.cos(roll) * 3*length/8
            sublines_delta_y = math.sin(roll) * 3*length/8

            #delta for the text
            angle = roll*180/math.pi
            text_delta_x = math.cos(roll) * (length/2 + 20)
            text_delta_y = math.sin(roll) * (length/2 + 20)

            self.canvas.coords(self.lines[i+9], self.width/2 - lines_delta_x - delta_x * i + pitch_factor_x,
                                            self.height/2 + lines_delta_y - delta_y * i + pitch_factor_y,
                                            self.width/2 + lines_delta_x - delta_x * i + pitch_factor_x, 
                                            self.height/2 - lines_delta_y - delta_y * i + pitch_factor_y)

            self.canvas.coords(self.sublines[i+9], self.width/2 - sublines_delta_x - delta_x * (i + 0.5) + pitch_factor_x,
                                            self.height/2 + sublines_delta_y - delta_y * (i + 0.5) + pitch_factor_y,
                                            self.width/2 + sublines_delta_x - delta_x * (i + 0.5) + pitch_factor_x, 
                                            self.height/2 - sublines_delta_y - delta_y * (i + 0.5) + pitch_factor_y)
            
            self.canvas.itemconfigure(self.textl[i+9], angle = angle)
            self.canvas.coords(self.textl[i+9], self.width/2 - text_delta_x - delta_x * i + pitch_factor_x,
                                            self.height/2 + text_delta_y - delta_y * i+ pitch_factor_y)
            
            self.canvas.itemconfigure(self.textr[i+9], angle = angle)
            self.canvas.coords(self.textr[i+9], self.width/2 + text_delta_x - delta_x * i + pitch_factor_x, 
                                            self.height/2 - text_delta_y - delta_y * i + pitch_factor_y)
                                            