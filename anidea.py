# Imports
import matplotlib.pyplot as plt
import numpy as np

# Ask for file input
filename = input('Please enter the name of the file: ')

# Try to open the file and execute the rest of the commands successfully
try:
    with open(filename, "r") as f:
        print("File successfully opened.")
        # Variables
        xList = [] # List of all x-values in coordinates
        yList = [] # List of all y-values in coordinates
        coords = [] # List of coordinates, saved as tuples
        
        # Add coordinates to lists
        for line in f.readlines():
            temp = line.split()
            c = (float(temp[0]), float(temp[1]))
            coords.append(c)
            xList.append(float(temp[0]))
            yList.append(float(temp[1]))
        # If there's an uneven number of x-coordinates and y-coordinates, yield an error
        if (len(xList) != len(yList)):
            raise Exception('Number of x and y values do not match!')
        # If the first and last coordinates do not match, yield and error
        if (xList[0] != xList[-1] or yList[0] != yList[-1]):
            raise Exception('Initial Coordinates do not match Final Coordinates!')
            
        # Plot the result
        plt.plot(xList, yList)
        coords.pop(-1)
        coords.sort()
        
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
        
        print("The total area of the figure is", areaTotal, "units squared.\n")
except IOError: #This error occurs if the file is not found, or failed to open.
    print("File failed to open.")
except Exception as e: #This is a general error caused likely to faulty coordinates.
    print(e)