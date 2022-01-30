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

coords.clear()
xCoords.clear()
yCoords.clear()
coords.append((0.0,0.0))
xCoords.append(0.0)
yCoords.append(0.0)

seed(sd)
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
    print(coords[len(coords)-1])
    iters = iters-1

lastx = (0.0, yCoords[-1])
coords.append(lastx)
xCoords.append(0.0)
yCoords.append(yCoords[-1])
coords.append((0.0, 0.0))
xCoords.append(0.0)
yCoords.append(0.0)

# Check if intersect TODO

plt.plot(xCoords, yCoords)
plt.rcParams.update({'font.size': 8})
length = len(xCoords)
print("REAL COORDINATES")
for i in range(length):
    print(" (" , xCoords[i] , ", " , yCoords[i] , ") ")

for i, j in zip(xCoords, yCoords):
   plt.text(i, j+0.5, '({}, {})'.format(i, j))
   
xVert = []
yVert = []

xHor = []
yHor = []

for i in range(length-1):
    x1 = xCoords[i]
    x2 = yCoords[i+1]
    y1 = yCoords[i]
    y2 = yCoords[i+1]
    if( x1 == x2):
        xHor.append(xCoords[i])
        xHor.append(xCoords[i+1])
        yHor.append(yCoords[i])
        yHor.append(yCoords[i+1])
    elif ( y1 == y2):
        xVert.append(xCoords[i])
        xVert.append(xCoords[i+1])
        yVert.append(yCoords[i])
        yVert.append(yCoords[i+1])

print("Hor coordinates")
horLength = len(xHor)    
for i in range(horLength):
    print(" (" , xHor[i] , ", " , yHor[i] , ") ")

print("Ver coordinates")
verLength = len(xVert)
for i in range(verLength):
    print(" (" , xVert[i] , ", " , yVert[i] , ") ")


plt.show()