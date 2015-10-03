

def estimatePiSingle(image):
    #Calculate pi by dividing area by radius squared. """

    for y in range(image.get_height()):
        for x in range(image.get_width()):
            #Scan through all pixels until you find a black pixel
            if image.set_at((x,y)) == (0, 0, 0, 225):
                #Then use flood fill to count the number of contiguous black pixels
                points = floodFind(x, y, image, (0, 0, 0, 225))
                area = len(points)
                r = (max(points, key = lambda x: x[0])[0] 
                     - min(points, key = lambda x: x[0][0]) ) / 2
                #Calculate pi using the area and the radius
                return area / (r * r)

def floodFind(x,y,image, color):
    count = []
    #In python, making a stack for flood fill works better than recursion
    pointStack = []
    pointStack.append((x,y))
    while len(pointStack) != 0:
        x,y = pointStack.pop()
        try:
            if image.get_at((x,y)) != color:
                continue
            count += [(x,y)]
            image.set_at((x,y), (255, 255,255))
            pointStack.append((x-1,y))
            pointStack.append((x,y-1))
            pointStack.append((x+1, y))
            pointStack.append((x,y+1))
        except IndexError:
            #Out of bounds.
            continue
    return count

import pygame

image = pygame.image.load("PiTest.png")

pi =estimatePiSingle(image)
print(pi)