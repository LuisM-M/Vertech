# THIS IS 

#from random import seed
from random import *
import matplotlib.pyplot as plt

xCoords = []
yCoords = []
coords = []

# difficulty --> tutorial 0, easy 1, normal 2, hard 3
difficulty = 2
# iters (iterations) --> default is 10
# tutorial (4-8), easy (4-8), medium (8-16), hard (16+)
iters = 10

sd = 0

with open("s.txt", "r") as f:
    sd = int(f.read())

fail = False
sd = 1

for i in range(1, 11):
        #print("SEED: ", sd)
    fail = True
    coords.clear()
    xCoords.clear()
    yCoords.clear()
    coords.append((0.0,0.0))
    xCoords.append(0.0)
    yCoords.append(0.0)
    
    iters = 10
    seed(i)
    while (iters != 0):
        mult = 1
        # rand
        r = random()
        if (r < 0.5):
            mult = -1
        val = randint(10, 25) * mult
        #print(val)
        # Move LR
        if (iters % 2 == 0):
            c = (xCoords[len(xCoords)-1]+float(val), float(yCoords[len(yCoords)-1]))
            coords.append(c)
            xCoords.append(xCoords[len(xCoords)-1]+float(val))
            yCoords.append(float(yCoords[len(yCoords)-1]))
        # Move UD
        else:
            c = (float(xCoords[len(xCoords)-1]), yCoords[len(yCoords)-1]+float(val))
            coords.append(c)
            xCoords.append(float(xCoords[len(xCoords)-1]))
            yCoords.append(yCoords[len(yCoords)-1]+float(val))
        #print(coords[len(coords)-1])
        iters = iters-1
    
    lastx = (0.0, yCoords[-1])
    coords.append(lastx)
    xCoords.append(0.0)
    yCoords.append(yCoords[-1])
    coords.append((0.0, 0.0))
    xCoords.append(0.0)
    yCoords.append(0.0)
    
    # Check if intersect TODO
    
    length = len(xCoords)
    #print("REAL COORDINATES")
    #for i in range(length):
        #print(" (" , xCoords[i] , ", " , yCoords[i] , ") ")
    
       
    xVert = []
    yVert = []
    
    xHor = []
    yHor = []
    
    for i in range(length-1):
        x1 = xCoords[i]
        x2 = xCoords[i+1]
        y1 = yCoords[i]
        y2 = yCoords[i+1]
        if(y1 == y2):
            xHor.append(x1)
            xHor.append(x2)
            yHor.append(y1)
            yHor.append(y2)
        elif (x1 == x2):
            xVert.append(x1)
            xVert.append(x2)
            yVert.append(y1)
            yVert.append(y2)
    
    #print(xHor)
    #print("\n", yHor)
    
    # =============================================================================
    # print("HORIZONTAL LINES")
    horLength = len(xHor)
    # print("Number of horizontal lines: ", horLength)
    # i = 0
    # while i < horLength-1:
    #     print( "(", xHor[i], "," , yHor[i] , ") to (", xHor[i+1], ",", yHor[i+1], ")" )
    #     i+=2
    # print("VERTICLE lINES")
    verLength = len(xVert) 
    # print("Number of verticle lines: ", verLength)   
    # i = 0
    # while i < verLength-1:
    #     print( "(", xVert[i], "," , yVert[i] , ") to (", xVert[i+1], ",", yVert[i+1], ")" )
    #     i+=2
    # =============================================================================
# This is originally Akhilios Code
# we are iterating through it slighty wrong I believe
# I think we are essentially tracing the entire shape bc the horizontal line list doesnt skip the verticle lines

# =============================================================================
#     i = 0;
#     j = 0;
#     while i < horLength-1:
#         while j < verLength-1:
#             # print( xHor[i], xHor[i+1])
#             if(xVert[j] < xHor[i] and xVert[j] > xHor[i+1]): # horizontal is moving left
#                 if(yVert[j] > yHor[i] and yVert[j+1] < yHor[i]):
#                     fail = False
#                     #print("fail here1")
#                     #print("( " , xHor[i] , " , " , yHor[i] , ")")
#                     #print("( " , xHor[i+1] , " , " , yHor[i+1] , ")")
#             elif (xVert[j] > xHor[i] and xVert[j] < xHor[i+1]): # horizontal is moving right
#                 if(yVert[j] > yHor[i] and yVert[j+1] < yHor[i]):
#                     fail = False
#                     #print("fail here2")
#                     #print("( " , xHor[i] , " , " , yHor[i] , ")")
#                     #print("( " , xHor[i+1] , " , " , yHor[i+1] , ")"
#             j += 2
#         i += 2
# =============================================================================


# This is Luis's version of the code
# What I am trying to do, is to correctly iterate through the entire line segments
# I noticed some funky behavior with the for loops in akhils code originally and decided to rework it
# to try to get rid of the weird behavior
# The issue is, I didn't work on Akhil's code which included the logic behind the intersecting lines
# I am not too sure as to what to do, as it is getting late
# Hopefully this works becuase we are almost done.
    i = 0;
    j = 0;
    while i < horLength-1: # currently not trying to change the fail boolean, just trying to print out the line segments
        print("(", xHor[i],", ",  yHor[i+1], ")")
        j = 0
        while j < verLength-1:
            print( "(", )
            j += 2
        i += 2
    if (not fail):
        print("FAILED WHEN SD:", sd)
    else:
        print("PASSED WHEN SD:", sd)
    
    #if (not fail):
    #    sd += 1
    
    plt.plot(xCoords, yCoords)
    go = "SD: " + str(sd)
    plt.title(go)
    plt.rcParams.update({'font.size': 7})
    
    for i, j in zip(xCoords, yCoords):
           plt.text(i, j+0.5, '({}, {})'.format(i, j))
    
    plt.show()
    
    sd += 1

#print("SD:", sd)
#plt.plot(xCoords, yCoords)
#plt.rcParams.update({'font.size': 7})

#for i, j in zip(xCoords, yCoords):
#       plt.text(i, j+0.5, '({}, {})'.format(i, j))

#plt.show()

f = open("s.txt", "w")
sd += 1
f.write(str(sd))
f.close()