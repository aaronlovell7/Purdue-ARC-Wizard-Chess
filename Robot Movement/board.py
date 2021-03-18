'''
figure out implement turning based on input angle
    need a function that accepts angle as input --- radians (pos == clockwise)
    turnRobot(angle)
        return True
    
figure out moving forward while oriented at input angle
    need function that accepts two velocities
    moveForward(distance) -- center to center
        return True
    
flowchart
    robot control: figure out angle and distance to move
    board: turn robot inputted angle
           move robot forward distance meters
           turn robot neg inputted angle
    
'''

import pygame
import time
import numpy as np

global size
global gameDisplay

def printBoard():
            #set color with rgb
            white,black = (255,255,255),(0,0,0)
            
            #set display
            global gameDisplay
            gameDisplay = pygame.display.set_mode((600,600))
            #Size of squares
            global size 
            size = 50
            
            #board length, must be even
            boardLength = 8
            gameDisplay.fill(white)
            
            cnt = 0
            for i in range(1,boardLength+1):
                for z in range(1,boardLength+1):
                    #check if current loop value is even
                    if cnt % 2 == 0:
                        pygame.draw.rect(gameDisplay, white,[size*z,size*i,size,size])
                    else:
                        pygame.draw.rect(gameDisplay, black, [size*z,size*i,size,size])
                    cnt +=1
                #since theres an even number of squares go back one value
                cnt-=1
            #Add a nice boarder
            pygame.draw.rect(gameDisplay,black,[size,size,boardLength*size,boardLength*size],1)
            pygame.display.update()

def printPiece(head, lB, rB):
    red = (255,0,0)
    green = (0,255,0)
    pygame.draw.polygon(gameDisplay, red, (head,lB,rB))
    pygame.draw.circle(gameDisplay, green, head, 5, 0)
    pygame.display.update()

def timeStep():
    start_time = time.time()
    seconds = 0.025

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        if elapsed_time > seconds:
            break

def turnRobot(ang, head, lB, rB, direction):
    #ang == angle to turn in radians; pos -> clockwise
    #head == current pos of head vertex
    #lB == current pos of left base vertex
    #rB == current pos of right base vertex
    if direction > 0:
        if ang > 0:
            #turning clockwise; lB doesnt change
            step = ang / 100
            base = np.sqrt((abs(lB[0] - rB[0]))**2 + (abs(lB[1] - rB[1]))**2)
            side = np.sqrt((abs(lB[0] - head[0]))**2 + (abs(lB[1] - head[1]))**2)
            angH = np.arccos(base/2/side)
            height = side * np.sin(angH)
            angle = step
            for i in range(0,100):
                #only works right now for angles less than 90 degrees
                rx = lB[0] + (base * np.cos(angle))
                ry = lB[1] - (base * np.sin(angle))
                rB = (rx,ry)
                hx = lB[0] + (side * np.cos(angle+angH))
                hy = lB[1] - (side * np.sin(angle+angH))
                head = (hx,hy)
                # cB = (lB[0] + abs(rB[0] - lB[0])/2, lB[1] - abs(rB[1] - lB[1])/2)
                # hx = cB[0] - height * np.sin(angle)
                # hy = cB[1] - height * np.cos(angle)
                head = (hx,hy)
                angle += step
                printBoard()
                printPiece(head,lB,rB)
                timeStep()
        elif ang < 0:
            #turning clockwise; lB doesnt change
            ang = abs(ang)
            step = ang / 100
            base = np.sqrt((abs(lB[0] - rB[0]))**2 + (abs(lB[1] - rB[1]))**2)
            side = np.sqrt((abs(lB[0] - head[0]))**2 + (abs(lB[1] - head[1]))**2)
            angH = np.arccos(base/2/side)
            height = side * np.sin(angH)
            angle = step
            for i in range(0,100):
                #only works right now for angles less than 90 degrees
                lx = rB[0] - (base * np.cos(angle))
                ly = rB[1] - (base * np.sin(angle))
                lB = (lx,ly)
                hx = rB[0] - (side * np.cos(angle+angH))
                hy = rB[1] - (side * np.sin(angle+angH))
                head = (hx,hy)
                # cB = (lB[0] + abs(rB[0] - lB[0])/2, lB[1] - abs(rB[1] - lB[1])/2)
                # hx = cB[0] - height * np.sin(angle)
                # hy = cB[1] - height * np.cos(angle)
                head = (hx,hy)
                angle += step
                printBoard()
                printPiece(head,lB,rB)
                timeStep()
    elif direction < 0:
        if ang > 0:
            #turning clockwise; lB doesnt change
            ang = abs(ang)
            step = ang / 100
            base = np.sqrt((abs(lB[0] - rB[0]))**2 + (abs(lB[1] - rB[1]))**2)
            side = np.sqrt((abs(lB[0] - head[0]))**2 + (abs(lB[1] - head[1]))**2)
            angH = np.arccos(base/2/side)
            height = side * np.sin(angH)
            angle = ang
            # angle = step
            for i in range(0,100):
                #only works right now for angles less than 90 degrees
                lx = rB[0] - (base * np.cos(angle))
                ly = rB[1] - (base * np.sin(angle))
                lB = (lx,ly)
                hx = rB[0] - (side * np.cos(angle+angH))
                hy = rB[1] - (side * np.sin(angle+angH))
                
                head = (hx,hy)
                # cB = (lB[0] + abs(rB[0] - lB[0])/2, lB[1] - abs(rB[1] - lB[1])/2)
                # hx = cB[0] - height * np.sin(angle)
                # hy = cB[1] - height * np.cos(angle)
                head = (hx,hy)
                angle += -1*step
                printBoard()
                printPiece(head,lB,rB)
                timeStep()
        elif ang < 0:
            #turning clockwise; lB doesnt change
            ang = abs(ang)
            step = ang / 100
            base = np.sqrt((abs(lB[0] - rB[0]))**2 + (abs(lB[1] - rB[1]))**2)
            side = np.sqrt((abs(lB[0] - head[0]))**2 + (abs(lB[1] - head[1]))**2)
            angH = np.arccos(base/2/side)
            height = side * np.sin(angH)
            angle = ang
            for i in range(0,100):
                #only works right now for angles less than 90 degrees
                rx = lB[0] + (base * np.cos(angle))
                ry = lB[1] - (base * np.sin(angle))
                rB = (rx,ry)
                hx = lB[0] + (side * np.cos(angle+angH))
                hy = lB[1] - (side * np.sin(angle+angH))
                head = (hx,hy)
                # cB = (lB[0] + abs(rB[0] - lB[0])/2, lB[1] - abs(rB[1] - lB[1])/2)
                # hx = cB[0] - height * np.sin(angle)
                # hy = cB[1] - height * np.cos(angle)
                head = (hx,hy)
                angle += -1*step
                printBoard()
                printPiece(head,lB,rB)
                timeStep()
    return (head,lB,rB)

def moveForward(dist, head, lB, rB, direction, ang):
    if direction > 0:
        #moving forward
        step = dist / 100
        for i in range(0,100):
            lx = lB[0] - np.sin(ang) * step
            ly = lB[1] - np.cos(ang) * step
            rx = rB[0] - np.sin(ang) * step
            ry = rB[1] - np.cos(ang) * step
            hx = head[0] - np.sin(ang) * step
            hy = head[1] - np.cos(ang) * step
            lB = (lx,ly)
            rB = (rx,ry)
            head = (hx,hy)
            printBoard()
            printPiece(head,lB,rB)
            timeStep()
            
            
    elif direction < 0:
        #moving backwards
        step = dist / 100
        for i in range(0,100):
            lx = lB[0] + np.sin(ang) * step
            ly = lB[1] + np.cos(ang) * step
            rx = rB[0] + np.sin(ang) * step
            ry = rB[1] + np.cos(ang) * step
            hx = head[0] + np.sin(ang) * step
            hy = head[1] + np.cos(ang) * step
            lB = (lx,ly)
            rB = (rx,ry)
            head = (hx,hy)
            printBoard()
            printPiece(head,lB,rB)
            timeStep()
            
    return (head, lB, rB)

def moveRobot(head, lB, rB, ang, dist, direction):
    #direction == 1 if moving forward, -1 if moving backward
    printBoard()
    printPiece(head,lB,rB)
    pos = turnRobot(ang,head,lB,rB,1)
    head = pos[0]
    lB = pos[1]
    rB = pos[2]
    pos = moveForward(dist, head, lB, rB, direction, ang)
    head = pos[0]
    lB = pos[1]
    rB = pos[2]
    ang = -1 * ang
    pos = turnRobot(ang,head,lB,rB, -1)
    head = pos[0]
    lB = pos[1]
    rB = pos[2]

def printPieces(pieceLoc):
    pass

def getTriPoints(coord): #coord in form [row,col]
    pass

def chessSim():
    global size
    global gameDisplay
    pygame.init()
    game = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
        
        while game:
            global size
            global gameDisplay
            printBoard()
                            
            #hardcode start triangle on e2 --> [6,4] to [3,1]
            head = (5.5*size, 7.2*size)
            lB = (5.2*size,7.8*size)
            rB = (5.8*size,7.8*size)
            
            moveRobot(head,lB,rB,np.pi/4, 70,1)
            
            game = False
                
            
            
    pygame.quit() 
    




 
#run simulation if this file directly being called by terminal
if __name__ == '__main__' :
    chessSim()