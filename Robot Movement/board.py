import pygame
import time

global size
global gameDisplay

def printBoard():
            #set color with rgb
            white,black = (255,255,255),(0,0,0)
            
            #set display
            global gameDisplay
            gameDisplay = pygame.display.set_mode((800,600))
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

def timeStep():
    start_time = time.time()
    seconds = 0.1

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
    
        if elapsed_time > seconds:
            break




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
        red = (255,0,0)
        green = (0,255,0)
            
        #put triangle on e2
        head = (5.5*size, 7.2*size)
        lB = (5.2*size,7.8*size)
        rB = (5.8*size,7.8*size)
        pygame.draw.polygon(gameDisplay, red, (head,lB,rB))
        pygame.draw.circle(gameDisplay, green, head,5,0)
        
        pygame.display.update()
        
        #turn triangle to left
        for i in range(0,10,1):
            distx = 0.5 * (rB[0]-lB[0])
            disty = distx
            timeStep()
        #move the triangle forward
        
        for j in range(0, 101, 1):
            printBoard()
            head = (head[0], head[1] - 1)
            lB = (lB[0],lB[1] - 1)
            rB = (rB[0],rB[1] - 1)
            pygame.draw.polygon(gameDisplay, red, (head,lB,rB))
            pygame.draw.circle(gameDisplay, green, head, 5, 0)
            pygame.display.update()
            
            timeStep()
        game = False
        
    
    
pygame.quit()    