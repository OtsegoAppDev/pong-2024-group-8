import pygame as pygame

def MoveBall():
    global ballSpeedx, ballSpeedy, ballLocation, ball, scoreA, scoreB
    
    if ballLocation[0] > screenWidth:
        ballSpeedx = -ballSpeedx
        scoreA = scoreA + 1
    
    if ballLocation[0] < 0:
        ballSpeedx = -ballSpeedx
        scoreB = scoreB + 1

    
    if ballLocation[1] < 0:
        ballSpeedy = -ballSpeedy
    
    if ballLocation[1] > screenHeight:
        ballSpeedy = -ballSpeedy
    ballLocation[0] = ballLocation[0] + ballSpeedx
    ballLocation[1] = ballLocation[1] + ballSpeedy
    ball = pygame.draw.circle(window, purple, ballLocation, radius, 0,)
    
    #if ballLocation
def MovePaddle():
    global PadASpeed, PadA, PadB, PadBSpeed
    """
    Moves the paddle up and down but not off the screen
    """
    
    if PadA.top <= 0:
        print("Top of Screen")
        PadA = PadA.move(0,2)
        PadASpeed = 0
    if PadB.top <= 0:
        print("Top of Screen")
        PadB=PadB.move(0,2)
        PadBSpeed = 0
    
    PadA = PadA.move(0,PadASpeed)
    pygame.draw.rect(window, purple, PadA)
    PadB = PadB.move(0,PadBSpeed)
    pygame.draw.rect(window, purple, PadB)

def DrawCenterLine():
    global screenWidth, screenHeight
    
    pygame.draw.line(window, white, (screenWidth//2,0), (screenWidth//2,screenHeight))
    

def DrawScore(font):
    global scoreA, scoreB
    
    text=font.render(str(scoreA), True, white)
    window.blit(text, (200,30))
    text=font.render(str(scoreB), True, white)
    window.blit(text, (700,30))

def VictoryText():
    global scoreA, scoreB
    if scoreA == 10:
        text=font.render("Congrats, you won! Press enter to play again.", True, white)
        window.blit(text, (50,300))
        stopGame()
    if scoreB == 10:
        text=font.render("Congrats, you won! Press enter to play again.", True, white)
        window.blit(text, (50,300))
        stopGame()
    
def stopGame():
    global ballSpeedx, ballSpeedy
    ballSpeedx = 0
    ballSpeedy = 0

def startGame():
    global ballSpeedx, ballSpeedy, ballLocation, scoreA, scoreB
    scoreA = 0
    scoreB = 0
    ballLocation = [500,300]
    ballSpeedx = 5
    ballSpeedy = 5
    


timer = pygame.time.Clock()

screenWidth = 1000
screenHeight = 600

window = pygame.display.set_mode([1000, 600])

ballSpeedx = 5
ballSpeedy = 5
black = (0,0,0)
white = (255,255,255)
purple = (128, 0, 128)
radius = 20
ballLocation = [500,300]
ball = pygame.Rect(ballLocation, (radius, radius))
textsmallx = 100
textsmally = 30
textsmallx2 = 250



PadA = pygame.Rect((0,150), (50,200))
PadASpeed = 0
PadB = pygame.Rect((950,150), (50,200))
PadBSpeed = 0

scoreA = 0
scoreB = 0

pygame.font.init()
font=pygame.font.SysFont("georgia", 56)

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                PadASpeed = 4
            if event.key == pygame.K_s:
                PadBSpeed = 4
            if event.key == pygame.K_UP:
                PadASpeed = -4
            if event.key == pygame.K_w:
                PadBSpeed = -4
        elif event.type ==pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                PadASpeed = 0
            if event.key == pygame.K_s:
                PadBSpeed = 0
            if event.key == pygame.K_UP:
                PadASpeed = 0
            if event.key == pygame.K_w:
                PadBSpeed = 0
            if event.key == pygame.K_RETURN:
                startGame()
            if event.key == pygame.K_1:
                radius = 40
                PadA = pygame.Rect((0,150), (80,300))
                PadB = pygame.Rect((1140,150), (80,300))
                window = pygame.display.set_mode([1220, 880])
                screenWidth = 1220
                screenHeight = 880
                ballLocation = [610,440]
                font=pygame.font.SysFont("georgia", 66)
                text=font.render(str(scoreA), True, white)
                window.blit(text, (100,30))
                text=font.render(str(scoreB), True, white)
                window.blit(text, (100,30))
            if event.key == pygame.K_2:
                radius = 20
                PadA = pygame.Rect((0,150), (50,200))
                PadB = pygame.Rect((950,150), (50,200))
                window = pygame.display.set_mode([1000, 600])
                screenWidth = 1000
                screenHeight = 600
                ballLocation = [500,300]
                font=pygame.font.SysFont("georgia", 56)
            if event.key == pygame.K_3:
                radius = 5
                PadA = pygame.Rect((0,150), (10,100))
                PadB = pygame.Rect((490,150), (10,100))
                window = pygame.display.set_mode([500, 300])
                screenWidth = 500
                screenHeight = 300
                ballLocation = [250,150]
                font=pygame.font.SysFont("georgia", 26)
                text=font.render(str(scoreA), True, white)
                window.blit(text, (textsmallx,textsmally))
                text=font.render(str(scoreB), True, white)
                window.blit(text, (textsmallx2,textsmally))
    if PadA.colliderect(ball):
        ballSpeedx = -ballSpeedx
    if PadB.colliderect(ball):
        ballSpeedx = -ballSpeedx
    timer.tick(60)
    window.fill(black)
    MoveBall()
    MovePaddle()
    DrawCenterLine()
    DrawScore(font)
    VictoryText()
    pygame.display.flip()
    #check quit event
    #check up, down, spacebar event
    #print(pygame.font.get_fonts())