from PIL import Image
from sys import argv

def isPrime(num):
    for x in range(2, int(num/2)+1):
        if num % x == 0: return False
    return True
sizeOfSpiral = 0
for x in argv:
    if x.isnumeric():
        sizeOfSpiral = int(x)
        break
if sizeOfSpiral < 2:
    print("Wrong size. Must be a whole number bigger than 1.\nUse the program like\npython3 ulam.py [size of spiral in one dimension]")
    exit()
step = 1
lastStep = 0
direction = 0 # 0 - left, 1 - up, 2 - right, 3 - down
currentX = round(sizeOfSpiral/2)
currentY = round(sizeOfSpiral/2)
im = Image.new(mode="RGB", size=(sizeOfSpiral, sizeOfSpiral))
pixels = im.load()
for num in range(1, (sizeOfSpiral**2)+1):
    # step one: determine where should we go next
    if direction == 0:
        currentX -= 1
    elif direction == 1:
        currentY += 1
    elif direction == 2:
        currentX += 1
    elif direction == 3:
        currentY -= 1
    else:
        print("error - undefined direction")
        exit()
    # step two: determine if we should turn or not
    lastStep += 1
    if lastStep == step:
        lastStep = 0
        direction += 1
        if direction == 4: direction = 0
        # step three: do we make bigger steps after the next? with this clockwise movement 
        # having started with going left we increase the steps when we go right or left
        if direction == 0 or direction == 2: step += 1
    # step four: we apply a pixel to the image
    if isPrime(num) and num != 1: pixels[currentX-1, currentY-1] = (0, 0, 0)
    else: pixels[currentX-1, currentY-1] = (255, 255, 255)
im.save("umalspiralprimes_" + str(sizeOfSpiral) + ".png")