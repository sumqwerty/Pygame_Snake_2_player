import pygame
import time
import random

pygame.init()

reddish_pink = (255,128,128)
lemon_yellow = (255,255,128)
paste_green = (128,255,128)
dpaste_green = (0,255,128)
paste_blue = (128,255,255)
dpaste_blue = (0,128,255)
dreddish_pink = (255,128,192)
dpink = (255,128,255)
parrot_green = (0,255,64)
pale_orange = (255,128,64)
dark_blue = (0,0,64)
paint_green = (0,64,64)
army_green = (0,128,0)
pale_ugly = (128,128,64)
dark_purple = (64,64,64)

white = (255, 255, 255)
black = (0, 0, 0)

red = (200, 0 ,0)
light_red = (255,0,0)
orange = (255,140,26)

green = (34, 177, 76)
light_green = (0,255,0)
greenx = (128,225,0)

yellow = (200,200,0)
light_yellow = (251,251,0)

brown = (139, 69, 69)
grey = (128,128,128)

blue = (0, 0, 255)

display_width = 800
display_height = 600

m = 0
time = 4
timeo = 4
loopd = 1

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('SNAKE')

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

snake_icon = pygame.image.load('icon2.png')

img = pygame.image.load('snakeHead.png')
img2 = pygame.image.load('icon.png')

smallfont = pygame.font.SysFont("comicsansms", 20)
medfont = pygame.font.SysFont("comicsansms", 25)

clock = pygame.time.Clock()

scorep1 = 0
scorep2 = 0

block_size = 20
FPS = 24

direction = "right"
direction2 = "right"

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 80)

def pause():

    paused = True
    message_to_screen("Paused",
                      green,
                      -100,
                      size = "large")
    message_to_screen("Press C to continue or Q to quit.",
                      green,
                      25)

    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        #gameDisplay.fill(white)
        clock.tick(5)

def randAppleGen():
    randAppleX = round(random.randrange(((display_width/2)+block_size), display_width-block_size)/20.0)*20.0
    randAppleY = round(random.randrange(0, display_height-block_size)/20.0)*20.0

    return randAppleX, randAppleY

def randAppleGen2():
    randAppleX2 = round(random.randrange(0, ((display_width/2)-block_size))/20.0)*20.0
    randAppleY2 = round(random.randrange(0, display_height-block_size)/20.0)*20.0

    return randAppleX2, randAppleY2


def options():
    global m, timeo

    opt = True

    while opt:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)

        message_to_screen("TIME",
                          green,
                          -200,
                          "large")

        button("Endless", 350,140,115,50, green, light_green, action = "endless")
        button("03:00 min", 350,200,115,50, green, light_green, action = "time1")
        button("05:00 min", 350,260,115,50, green, light_green, action = "time2")
        button("07:00 min", 350,320,115,50, green, light_green, action = "time3")
        button("10:00 min", 350,380,115,50, green, light_green, action = "time4")

        button("Play", 357,520,100,50, green, light_green, action = "play")
        button("Back", 357,450,100,50, yellow, light_yellow, action = "main")
        #button("Quit", 550,450,100,50, red, light_red, action = "quit")

        pygame.display.update()
        clock.tick(15)

def game_controls():


    gcont = True

    while gcont:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(black)
        message_to_screen("CONTROLS",
                          green,
                          -100,
                          "large")
        message_to_screen("UP: Up Arrow",
                          white,
                          -30)
        message_to_screen("DOWN: Down arrows",
                          white,
                          10)
        message_to_screen("LEFT and RIGHT: Left and Right arrows",
                          white,
                          50)

        message_to_screen("Pause: P",
                         white,
                        90)


        button("Play", 350,500,100,50, green, light_green, action = "play")
        button("Back", 350,430,100,50, yellow, light_yellow, action = "main")
        #button("Quit", 550,500,100,50, red, light_red, action = "quit")

        pygame.display.update()
        clock.tick(15)


def button(text, x, y, width, height, inactive_color, active_color, action = None):
    global timeo, time, loopd
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "play" and loopd == 2:
                gameLoope()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

            if action == "options":
                options()

            if action == "endless":
                gameLoope()
                loopd = 2

            if action == "time1":
                timeo = 2
                time = 2
                loopd = 1
                gameLoop()
            if action == "time2":
                timeo = 4
                time = 4
                loopd = 1
                gameLoop()
            if action == "time3":
                timeo = 6
                time = 6
                loopd = 1
                gameLoop()
            if action == "time4":
                timeo = 9
                time = 9
                loopd = 1
                gameLoop()

    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))


    text_to_button(text,black,x,y,width,height)




def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()



        gameDisplay.fill(black)
        message_to_screen("Welcome to Snake",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective is to eate red apples",
                          white,
                          -30)
        message_to_screen("The more apples you eat the longer you get",
                          white,
                          10)
        message_to_screen("If you run into yourself, or the edges, you die!!",
                          white,
                          50)

##        message_to_screen("Press C to play, P to pause or Q to quit.",
##                          black,
##                          180)

        button("Play", 150,430,100,50, green, light_green, action = "play")
        button("Controls", 150,500,100,50, yellow, light_yellow, action = "controls")
        button("Quit", 550,430,100,50, red, light_red, action = "quit")
        button("Time", 550,500,100,50, dpaste_blue, paste_blue, action = "options")

        gameDisplay.blit(snake_icon,(345,430))

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
        pygame.draw.rect(gameDisplay, red, [XnY[0]+(block_size/4),XnY[1]+(block_size/4),block_size / 2,block_size / 2])

def snake2(block_size, snakelist2):


    if direction2 == "right":
        head2 = pygame.transform.rotate(img, 270)
    if direction2 == "left":
        head2 = pygame.transform.rotate(img, 90)
    if direction2 == "up":
        head2 = img
    if direction2 == "down":
        head2 = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head2, (snakelist2[-1][0], snakelist2[-1][1]))

    for XnY in snakelist2[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])
        pygame.draw.rect(gameDisplay, blue, [XnY[0]+(block_size/4),XnY[1]+(block_size/4),block_size / 2,block_size / 2])



def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)


    return textSurface, textSurface.get_rect()


def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2), (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

def score_d(msg2, color2,x=0,y=0):
    screen_text_2 = smallfont.render(msg2, True ,color2)
    gameDisplay.blit(screen_text_2, [x,y])

def game_over():
    global score, time, timeo
    game_over = True

    while game_over:

        gameDisplay.fill(black)
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        message_to_screen("Game Over",
                          green,
                          -100,
                          "large")
        message_to_screen("The scores are equal",
                          black,
                          -30)


        button("Play Again", 150,430,150,50, green, light_green, action = "play")
        button("Controls", 350,430,100,50, yellow, light_yellow, action = "controls")
        button("Quit", 550,430,100,50, red, light_red, action = "quit")
        score = 0
        timeo = time
        pygame.display.update()
        clock.tick(15)

def player_1_won():
    global scorep1, timeo,time
    win1 = True

    while win1:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        gameDisplay.fill(black)
        message_to_screen("Player 1 Won!",
                          green,
                          -100,
                          "large")
        message_to_screen("SCORE: " + str(scorep1),
                          green,
                          50,
                          "medium")


        button("Play Again", 150,430,150,50, green, light_green, action = "play")
        button("Controls", 350,430,100,50, yellow, light_yellow, action = "controls")
        button("Quit", 550,430,100,50, red, light_red, action = "quit")
        button("Time", 350,500,100,50, dpaste_blue, paste_blue, action = "options")
        pygame.display.update()
        timeo = time
        clock.tick(15)

def player_2_won():
    global scorep2,timeo, time
    win2 = True

    while win2:

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



        gameDisplay.fill(black)
        message_to_screen("Player 2 Won!",
                          green,
                          -100,
                          "large")
        message_to_screen("SCORE: " + str(scorep2),
                          green,
                          50,
                          "medium")


        button("Play Again", 150,430,150,50, green, light_green, action = "play")
        button("Controls", 350,430,100,50, yellow, light_yellow, action = "controls")
        button("Quit", 550,430,100,50, red, light_red, action = "quit")
        button("Time", 350,500,100,50, dpaste_blue, paste_blue, action = "options")
        timeo = time
        pygame.display.update()
        clock.tick(15)

def gameLoope():
    global direction,direction2,timeo,m, scorep1,scorep2, time, loopd
    loopd = 2

    gameExit = False
    gameOver = False
    i = 1
    j = 60
    g = 1
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x2 = display_width/2
    lead_y2 = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    lead_x_change2 = 0
    lead_y_change2 = 0

    scorep1 = 0
    snakeList = []
    snakeLength = 1

    scorep2 = 0
    snakeList2 = []
    snakeLength2 = 1

    m = 0

    randAppleX,randAppleY = randAppleGen()
    randAppleX2,randAppleY2 = randAppleGen2()

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('SNAKE')

    while not gameExit:

        if gameOver == True:
            game_over()
##            message_to_screen("Game over",
##                              red,
##                              -50 ,
##                              size = "large")
##            message_to_screen("Press C to play the again or Q to quit",
##                              black,
##                              50,
##                              size = "medium")
##            pygame.display.update()


        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_a:
                    direction2 = "left"
                    lead_x_change2 = -block_size
                    lead_y_change2 = 0

                elif event.key == pygame.K_d:
                    direction2 = "right"
                    lead_x_change2 = block_size
                    lead_y_change2 = 0

                elif event.key == pygame.K_w:
                    direction2 = "up"
                    lead_y_change2 = -block_size
                    lead_x_change2 = 0

                elif event.key == pygame.K_s:
                    direction2 = "down"
                    lead_y_change2 = block_size
                    lead_x_change2 = 0


                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= 800:
            lead_x = display_width/2

        if lead_x < display_width/2:
            lead_x = 800

        if lead_y >= 600:
            lead_y = 0

        if lead_y <0:
            lead_y = 600


        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x2 >= display_width/2:
            lead_x2 = 0

        if lead_x2 < 0:
            lead_x2 = display_width/2

        if lead_y2 >= 600:
            lead_y2 = 0

        if lead_y2 <0:
            lead_y2 = 600


        lead_x2 += lead_x_change2
        lead_y2 += lead_y_change2

        gameDisplay.fill(black)

        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        gameDisplay.blit(img2, (randAppleX, randAppleY))
        gameDisplay.blit(img2, (randAppleX2, randAppleY2))





        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        snakeHead2 = []
        snakeHead2.append(lead_x2)
        snakeHead2.append(lead_y2)
        snakeList2.append(snakeHead2)


        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                player_2_won()

        if len(snakeList2) > snakeLength2:
            del snakeList2[0]
        for eachSegment in snakeList2[:-1]:
            if eachSegment == snakeHead2:
                gameOver = True
                player_1_won()

        snake(block_size, snakeList)
        snake2(block_size, snakeList2)
        score_d("player 1 score: " + str(scorep1), light_yellow,(display_width/2)+5)
        score_d("player 2 score: " + str(scorep2), blue)
        pygame.draw.line(gameDisplay,red,(display_width/2,0),(display_width/2,display_height),5)





        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX,randAppleY = randAppleGen()
            snakeLength += 1
            scorep1 += 10

        if lead_x2 == randAppleX2 and lead_y2 == randAppleY2:
            randAppleX2,randAppleY2 = randAppleGen2()
            snakeLength2 += 1
            scorep2 += 10

##        if (i%24 == 0):
##            j -= 1
##
##        if (j%60 == 0):
##            j = 60
##            if(g%24 == 0 and timeo > 0):
##                timeo -= 1
##
##        if (timeo == m and j == 1):
##            if(scorep1 == scorep2):
##                gameOver = True
##            elif(scorep1 > scorep2):
##                player_1_won()
##            elif(scorep2 > scorep1):
##                player_2_won()


##        text = smallfont.render(str(timeo)+":"+str(j) , True, white)
##        gameDisplay.blit(text, [2,display_height-40])
        pygame.display.update()
        clock.tick(FPS)
##        i += 1
##        g += 1

    pygame.quit()
    quit()




def gameLoop():
    global direction,direction2,timeo,m, scorep1,scorep2, time

    gameExit = False
    gameOver = False
    i = 1
    j = 60
    g = 1
    lead_x = display_width/2
    lead_y = display_height/2

    lead_x2 = display_width/2
    lead_y2 = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    lead_x_change2 = 0
    lead_y_change2 = 0

    scorep1 = 0
    snakeList = []
    snakeLength = 1

    scorep2 = 0
    snakeList2 = []
    snakeLength2 = 1

    m = 0

    randAppleX,randAppleY = randAppleGen()
    randAppleX2,randAppleY2 = randAppleGen2()

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('SNAKE')

    while not gameExit:

        if gameOver == True:
            game_over()
##            message_to_screen("Game over",
##                              red,
##                              -50 ,
##                              size = "large")
##            message_to_screen("Press C to play the again or Q to quit",
##                              black,
##                              50,
##                              size = "medium")
##            pygame.display.update()


        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'right':
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP and direction != 'down':
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN and direction != 'up':
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0

                elif event.key == pygame.K_a and direction2 != 'right':
                    direction2 = "left"
                    lead_x_change2 = -block_size
                    lead_y_change2 = 0

                elif event.key == pygame.K_d and direction2 != 'left':
                    direction2 = "right"
                    lead_x_change2 = block_size
                    lead_y_change2 = 0

                elif event.key == pygame.K_w and direction2 != 'down':
                    direction2 = "up"
                    lead_y_change2 = -block_size
                    lead_x_change2 = 0

                elif event.key == pygame.K_s and direction2 != 'up':
                    direction2 = "down"
                    lead_y_change2 = block_size
                    lead_x_change2 = 0


                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= 800:
            lead_x = display_width/2

        if lead_x < display_width/2:
            lead_x = 800

        if lead_y >= 600:
            lead_y = 0

        if lead_y <0:
            lead_y = 600


        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x2 >= display_width/2:
            lead_x2 = 0

        if lead_x2 < 0:
            lead_x2 = display_width/2

        if lead_y2 >= 600:
            lead_y2 = 0

        if lead_y2 <0:
            lead_y2 = 600


        lead_x2 += lead_x_change2
        lead_y2 += lead_y_change2

        gameDisplay.fill(black)

        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        gameDisplay.blit(img2, (randAppleX, randAppleY))
        gameDisplay.blit(img2, (randAppleX2, randAppleY2))





        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        snakeHead2 = []
        snakeHead2.append(lead_x2)
        snakeHead2.append(lead_y2)
        snakeList2.append(snakeHead2)


        if len(snakeList) > snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                player_2_won()

        if len(snakeList2) > snakeLength2:
            del snakeList2[0]
        for eachSegment in snakeList2[:-1]:
            if eachSegment == snakeHead2:
                gameOver = True
                player_1_won()

        snake(block_size, snakeList)
        snake2(block_size, snakeList2)
        score_d("player 1 score: " + str(scorep1), light_yellow,(display_width/2)+5)
        score_d("player 2 score: " + str(scorep2), blue)
        pygame.draw.line(gameDisplay,red,(display_width/2,0),(display_width/2,display_height),5)





        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX,randAppleY = randAppleGen()
            snakeLength += 1
            scorep1 += 10

        if lead_x2 == randAppleX2 and lead_y2 == randAppleY2:
            randAppleX2,randAppleY2 = randAppleGen2()
            snakeLength2 += 1
            scorep2 += 10

        if (i%24 == 0):
            j -= 1

        if (j%60 == 0):
            j = 60
            if(g%24 == 0 and timeo > 0):
                timeo -= 1

        if (timeo == m and j == 1):
            if(scorep1 == scorep2):
                gameOver = True
            elif(scorep1 > scorep2):
                player_1_won()
            elif(scorep2 > scorep1):
                player_2_won()


        text = smallfont.render(str(timeo)+":"+str(j) , True, white)
        gameDisplay.blit(text, [2,display_height-40])
        pygame.display.update()
        clock.tick(FPS)
        i += 1
        g += 1

    pygame.quit()
    quit()
    
game_intro()
#gameLoop()
