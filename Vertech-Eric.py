# Imports
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from tkinter import *
from tkinter.ttk import *

bg_color = 'palegreen'

class vertech(tk.Tk):
 
    def __init__(self, *args, **kwargs):
        
        '''This function, __init__, within the object, KeyClick, sets the main 
        parameters for the entire program and allows a way to switch between frames'''
        
        tk.Tk.__init__(self, *args, **kwargs)
        main_frame = tk.Frame(self)
        
        main_frame.pack(side="top", fill="both", expand = True)
        
        self.frames = {}
        
        for page in (Main_menu, Learn, Free):
            frame = page(main_frame, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(Main_menu)
        self.after(1000, lambda: self.show_frame(Main_menu))
    
    def show_frame(self, cont):
        
        '''This function, show_frame, within the object, KeyClick, will display 
        the frame of whatever frame is used as it's parameter. This also allows
        displays the saved counter in the event that the user clicks resume'''
        
        frame = self.frames[cont]
        frame.tkraise()


class Main_menu(tk.Frame):
  
  def __init__(self, parent, controller):    
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg=bg_color)
        
        menu_title = tk.Label(self, text="Vertech", bg=bg_color, fg="black",
                             font=("LARGE_FONT", 18,"bold"))
        menu_title.pack(padx=210, pady=25)
        
        menu_play = tk.Button(self, text="Begin Learning!", font = "LARGE_FONT",
                              bg="mediumslateblue", fg="white",
                              command=combine_funcs(lambda: controller.show_frame(Learn)))
        menu_play.pack(padx=25, pady=25)
        
        menu_free = tk.Button(self, text="Sandbox", font = "LARGE_FONT",
                              bg="mediumslateblue", fg="white",
                              command=combine_funcs(lambda: controller.show_frame(Free)))
        menu_free.pack(padx=25, pady=25)
        
        menu_quit = tk.Button(self, text="Quit", bg="PaleVioletRed", fg="white",
                              command=controller.destroy)
        menu_quit.pack(padx=25, pady=25)
        
        def show_frame(self, cont):
        
            '''This function, show_frame, within the object, KeyClick, will display 
            the frame of whatever frame is used as it's parameter. This also allows
            displays the saved counter in the event that the user clicks resume'''
            
            frame = self.frames[cont]
            frame.tkraise()

class Learn(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg=bg_color)
       
        Learn.class_and_grade_lbl = tk.Label(self, text = "", bg=bg_color)
        Learn.class_and_grade_lbl.pack(padx=5, pady=5)
        
        Learn_display_graph_btn = tk.Button(self, text="Display shape", bg="mediumslateblue", fg="white",
                              command=plot)
        Learn_display_graph_btn.pack(padx=5, pady=5)
   
        Learn_promptAnswer = tk.Label(self, text="Your Answer: ", bg=bg_color, fg="black",
                             font=("LARGE_FONT", 15,"bold"))
        Learn_promptAnswer.pack(padx=5, pady=15) 
   
        Learn.my_text = tk.Text(self, width=10, height=1)
        Learn.my_text.pack(pady=25) 
        
        Learn_submit_btn = tk.Button(self, text = 'Enter', bg="mediumslateblue",
                                    fg="white",
                                    command=combine_funcs(combine_funcs(calculate, click), lambda: controller.show_frame(Learn)))
        Learn_submit_btn.pack(padx=5, pady=20)
        
        Learn.promptAnswer_lbl = tk.Label(self, text="", bg=bg_color, fg="black",
                             font=("LARGE_FONT", 15,"bold"))
        Learn.promptAnswer_lbl.pack(padx=5, pady=15)
        
        
        Learn_home_btn = tk.Button(self, text="Home", bg="mediumslateblue",
                                    fg="white",
                                    command=lambda: controller.show_frame(Main_menu))
        Learn_home_btn.pack(padx=5, pady=5)   

class Free(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self, bg=bg_color)
        
        Free.class_and_grade_lbl = tk.Label(self, text = "", bg=bg_color)
        Free.class_and_grade_lbl.pack(padx=5, pady=5)
        
        Free_upload_btn = tk.Button(self, text="Upload that thing!", font = "LARGE_FONT",
                                    bg="mediumslateblue", fg="white",
                                    command=combine_funcs(UploadAction, plotCalc))
        Free_upload_btn.pack(padx=5, pady=20)
        
        Free.ans = tk.Label(self, text="", bg=bg_color, fg="black",
                             font=("LARGE_FONT", 15,"bold"))
        Free.ans.pack(padx=5, pady=15)
        
        Free_home_btn = tk.Button(self, text="Home", bg="mediumslateblue",
                                    fg="white",
                                    command=lambda: controller.show_frame(Main_menu))
        Free_home_btn.pack(padx=5, pady=5)

def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

def plotCalc():
    plot()
    calculate()
    print(areaTotal)
    Free.ans.config(text="AREA: " + str(areaTotal) + " units^2", font = 'LARGEFONT')
    

def click():
    answer = Learn.my_text.get('1.0', tk.END)
    #answer="1288.0"
    Learn.my_text.delete('1.0', tk.END)
    #calculate()
    #print("area in click is: " + str(areaTotal))
    #print("areaTotal is: " + str(areaTotal))
    #print("answer is: " + str(answer))
    if (areaTotal == int(answer)):
        Learn.promptAnswer_lbl.config(text="Correct!", font = 'LARGEFONT')
    else:
        Learn.promptAnswer_lbl.config(text="Wrong!", font = 'LARGEFONT')
        Learn.my_text.delete('1.0', tk.END)
        
def plot():
    global coords
    with open("box_hard_1.txt", "r") as f:
        newWindow = Toplevel(vertech)
        xList = [] # List of all x-values in coordinates
        yList = [] # List of all y-values in coordinates
        #coords = []
        coords.clear()
             
             # Add coordinates to lists
        for line in f.readlines():
             temp = line.split()
             c = (float(temp[0]), float(temp[1]))
             coords.append(c)
             xList.append(float(temp[0]))
             yList.append(float(temp[1]))
        #for x in xList:
        #    print(x)
        fig = Figure(figsize = (5, 5),
                    dpi = 100)
        
        # adding the subplot
        plot1 = fig.add_subplot(111)
        
        plot1.plot(xList, yList)
        #plot1.rcParams.update({'font.size': 7})
    
        #for i, j in zip(xCoords, yCoords):
        #       plot1.text(i, j+0.5, '({}, {})'.format(i, j))
        
        
        canvas = FigureCanvasTkAgg(fig, master = newWindow)  
        canvas.draw()
        canvas.get_tk_widget().pack()

          
def calculate():           
    global coords
    global areaTotal
    #print(len(coords))
    if (len(coords) != 0):
        coords.pop(-1)
    while coords:
        coords.sort()
        #print(coords)
        #print(len(coords))
        c1 = coords[0]
        c2 = coords[1]
        c3 = None
        c4 = None
        coords.pop(0)
        coords.pop(0)
        index = 0
        for co in coords:
            if(co[1] == c1[1] and c3 == None):
                c3 = co
            elif(co[1] == c2[1] and c4 == None):
                c4 = co
            
            index+=1
            if(c3 != None or c4 != None):
                index-=1
                if (c3 != None and c4 != None):
                    break
    
        # Find the length between selected coordinates
        length = None
        if (c3!= None and c4 != None and c3[0] > c4[0]):
            length = abs(c4[0]-c1[0])
        else:
            length = abs(c3[0]-c1[0])
        
        # Find width between selected coordinates
        width = abs(c2[1]-c1[1])
        # Find area of figure
        areaCurrent = length * width
        areaTotal += areaCurrent
        
        #print(length, width, areaCurrent, areaTotal)
        
        # Determine which of the two coordinates extends out further (x-value).
        # Eliminate the coordinate that comes up short.
        if (c3!= None and c4 != None and c3[0] > c4[0]):
            newCoord = (c4[0], c3[1])
            coords.insert(index, newCoord)
            coords.pop(index+1)
            if (coords[0][1] > coords[1][1]):
                temp = coords[0]
                coords.pop(0)
                coords.insert(1, temp)
        elif (c3!= None and c4 != None and c3[0] < c4[0]):
            newCoord = (c3[0], c4[1])
            coords.insert(index, newCoord)
            coords.pop(index+1)
            if (coords[0][1] > coords[1][1]):
                temp = coords[0]
                coords.pop(0)
                coords.insert(1, temp)
        elif (c3!= None and c4 != None):
            coords.remove(c3)
            coords.remove(c4)      
    #print("area in function is: " + str(areaTotal))

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
########################################################################################################
vertech = vertech()
#vertech.protocol('WM_DELETE_WINDOW', overrideWindowX)
vertech.title("Vertech")
vertech.geometry("513x360")
coords = []  # List of coordinates, saved as tuples
areaTotal = 0
vertech.resizable(width=False, height=False)
vertech.mainloop()