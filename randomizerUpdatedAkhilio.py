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

#for i in range(1, 11):
    #print("SEED: ", sd)
fail = True
coords.clear()
xCoords.clear()
yCoords.clear()
coords.append((0.0,0.0))
xCoords.append(0.0)
yCoords.append(0.0)

iters = 10
seed(5)
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

horLength = len(xHor)    
verLength = len(xVert)
for i in range(horLength-1):   
    for j in range(verLength-1):
        #print(xVert[j], xHor[i], xHor[i+1])
        if(xVert[j] < xHor[i] and xVert[j] > xHor[i+1]): # horizontal is moving left
            if(yVert[j] > yHor[i] and yVert[j+1] < yHor[i]):
                fail = False
                #print("fail here1")
                #print("( " , xHor[i] , " , " , yHor[i] , ")")
                #print("( " , xHor[i+1] , " , " , yHor[i+1] , ")")
        elif (xVert[j] >= xHor[i] and xVert[j] <= xHor[i+1]):
            if(yVert[j] > yHor[i] and yVert[j+1] < yHor[i]):
                fail = False
                #print("fail here2")
                #print("( " , xHor[i] , " , " , yHor[i] , ")")
                #print("( " , xHor[i+1] , " , " , yHor[i+1] , ")"
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
