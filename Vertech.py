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
        
        for page in (Main_menu, Learn):
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
        menu_title.pack(padx=5, pady=25)
        
        menu_play = tk.Button(self, text="Begin Learning!", font = "LARGE_FONT",
                              bg="mediumslateblue", fg="white",
                              command=combine_funcs(lambda: controller.show_frame(Learn)))
        menu_play.pack(padx=5, pady=5)
        
        menu_quit = tk.Button(self, text="Quit", bg="PaleVioletRed", fg="white",
                              command=controller.destroy)
        menu_quit.pack(padx=5, pady=5)
        
        
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
        Learn.class_and_grade_lbl.pack(padx=5, pady=10)
        
        Learn_display_graph_btn = tk.Button(self, text="Display shape", bg="mediumslateblue", fg="white",
                              command=plot(createWindow()))
        Learn_display_graph_btn.pack(padx=5, pady=5)
   
        Learn_home_btn = tk.Button(self, text="Home", bg="mediumslateblue",
                                    fg="white",
                                    command=lambda: controller.show_frame(Main_menu))

        Learn_home_btn.pack(padx=5, pady=10)   

def createWindow():
    master = Tk()
    newWindow = Toplevel(master)
    return newWindow
        
def plot(parent):
    with open("box_hard_1.txt", "r") as f:
        
        xList = [] # List of all x-values in coordinates
        yList = [] # List of all y-values in coordinates
        coords = []
             
             # Add coordinates to lists
        for line in f.readlines():
             temp = line.split()
             c = (float(temp[0]), float(temp[1]))
             coords.append(c)
             xList.append(float(temp[0]))
             yList.append(float(temp[1]))
        fig = Figure(figsize = (5, 5),
                    dpi = 100)
      
        # list of squares
        #y = [i**2 for i in range(101)]
        
        # adding the subplot
        plot1 = fig.add_subplot(111)
      
        # plotting the graph
        #plot1 = fig.add_axes(xList)
        plot1.plot(yList)
        
        
        canvas = FigureCanvasTkAgg(fig, master = parent)  
        canvas.draw()
        canvas.get_tk_widget().pack()
      
        # creating the Matplotlib toolbar
       # toolbar = NavigationToolbar2Tk(canvas, createWindow)
        #toolbar.update()
      
        # placing the toolbar on the Tkinter window
        #canvas.get_tk_widget().pack()
        # Ask for file input
# =============================================================================
#     filename = input('Please enter the name of the file: ')
#     
#     # Try to open the file and execute the rest of the commands successfully
#     #try:
#         with open(filename, "r") as f:
#             print("File successfully opened.")
#             # Variables
#             xList = [] # List of all x-values in coordinates
#             yList = [] # List of all y-values in coordinates
#             
#             
#             # Add coordinates to lists
#             for line in f.readlines():
#                 temp = line.split()
#                 c = (float(temp[0]), float(temp[1]))
#                 coords.append(c)
#                 xList.append(float(temp[0]))
#                 yList.append(float(temp[1]))
#             # If there's an uneven number of x-coordinates and y-coordinates, yield an error
#             if (len(xList) != len(yList)):
#                 raise Exception('Number of x and y values do not match!')
#             # If the first and last coordinates do not match, yield and error
#             if (xList[0] != xList[-1] or yList[0] != yList[-1]):
#                 raise Exception('Initial Coordinates do not match Final Coordinates!')
#             fig = Figure(figsize = (5, 5), dpi = 100)    
#             plt.plot(xList, yList)
#             canvas = FigureCanvasTkAgg(fig, master = vertech)  
#             canvas.draw()
#     except IOError: #This error occurs if the file is not found, or failed to open.
#         print("File failed to open.")
#     except Exception as e: #This is a general error caused likely to faulty coordinates.
#         print(e)    
# =============================================================================
            
            
def calculate():           
    # Take first two elements in current list
    areaTotal = 0
    while coords:
        coords.sort()
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
        if (c3[0] > c4[0]):
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
        if (c3[0] > c4[0]):
            newCoord = (c4[0], c3[1])
            coords.insert(index, newCoord)
            coords.pop(index+1)
            if (coords[0][1] > coords[1][1]):
                temp = coords[0]
                coords.pop(0)
                coords.insert(1, temp)
        elif (c3[0] < c4[0]):
            newCoord = (c3[0], c4[1])
            coords.insert(index, newCoord)
            coords.pop(index+1)
            if (coords[0][1] > coords[1][1]):
                temp = coords[0]
                coords.pop(0)
                coords.insert(1, temp)
        else:
            coords.remove(c3)
            coords.remove(c4)
            

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
########################################################################################################
vertech = vertech()
#vertech.protocol('WM_DELETE_WINDOW', overrideWindowX)
vertech.title("Vertech")
#vertech.geometry('+%d+%d' % (400, 200))
coords = [] # List of coordinates, saved as tuples
vertech.resizable(width=False, height=False)
vertech.mainloop()