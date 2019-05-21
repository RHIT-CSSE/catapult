import pygame
from math import *
from pygame.locals import *
from fallingballclasses import *
from pygame.time import *
import random

pygame.init()
background = pygame.image.load("tileclouds.jpg")
screen_width, screen_height = 300,600
screen = pygame.display.set_mode([screen_width, screen_height],0,32)
screen.blit(background, [0,0])
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (80,80))
cover_font = pygame.font.SysFont("Comic Sans MS ", 30)
cover_font2 = pygame.font.SysFont("Comic Sans MS", 28)
cover_text = cover_font.render("OPERATION", True, [0,0,0])
cover_text2 = cover_font2.render("Falling Ball", True, [0,0,0])
button_font = pygame.font.SysFont("Comic Sans MS ", 18, bold = True)
start_text = button_font.render("Start Game", True, [0,0,0])
instruction_text = button_font.render("Instructions", True, [0,0,0])
screen.blit(ball,[40,460])
screen.blit(ball,[180,460])
screen.blit(cover_text, [60,120])
screen.blit(cover_text2, [80,180] )
screen.blit(start_text, [25,485])
screen.blit(instruction_text, [165,485])
pygame.display.flip()
start_game = True
show_instructions = False
my_clock = pygame.time.Clock()
while start_game:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            a = event.pos
            if distance ((80,500), a) < 40:
                start_game = False
            if distance ((220,500), a) < 40:
                show_instructions = True
                start_game = False
            if start_game is True:
                my_clock = 0
              
while show_instructions:  
    screen.blit(background, [0,0])
    instructions_heart_img = pygame.image.load("heart.png")
    instructions_heart_img = pygame.transform.scale(instructions_heart_img, (30,30))
    instructions_plat_img = pygame.image.load("plat.png")
    instructions_plat_img = pygame.transform.scale(instructions_plat_img, (60,20))
    instructions_spike_img = pygame.image.load("spike.png")
    instructions_spike_img = pygame.transform.scale(instructions_spike_img, (60,20))
    instructions_star_img = pygame.image.load("star.png")
    instructions_star_img = pygame.transform.scale(instructions_star_img, (30,30))

    instructions_font = pygame.font.SysFont("Times New Roman", 17)
    instructions_text_1 = instructions_font.render ("Life + 1", True, [0, 0, 0])
    instructions_text_2 = instructions_font.render ("Life - 1", True, [0, 0, 0])
    instructions_text_3 = instructions_font.render ("Use these to stay on screen", True, [0, 0, 0])
    instructions_text_4 = instructions_font.render ("Keep the ball in the window", True, [0, 0, 0])
    instructions_text_5 = instructions_font.render ("using the arrow keys.", True, [0, 0, 0]) 
    instructions_text_6 = instructions_font.render ("Points + 20", True, [0, 0, 0])               
    screen.blit(instructions_heart_img, [35,100])
    screen.blit(instructions_plat_img, [20,208])
    screen.blit(instructions_spike_img, [20,158])
    screen.blit(instructions_star_img, [35,50])
    screen.blit(instructions_text_1, [100,108])
    screen.blit(instructions_text_2, [100,160])
    screen.blit(instructions_text_3, [100,210])
    screen.blit(instructions_text_4, [50,270])
    screen.blit(instructions_text_5, [72,290])
    screen.blit(instructions_text_6, [100,60])
    screen.blit(ball,[110,400])
    start_text = button_font.render("Start Game", True, [0,0,0])
    screen.blit(start_text, [90,425])
    pygame.display.flip()
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        if event.type == MOUSEBUTTONDOWN:
            a = event.pos
            if distance((140,440), a) < 40:
                show_instructions = False

game = True
while game:                            
    pygame.mouse.set_visible(False)
    point_font = pygame.font.SysFont("Arial", 15)
    point_text = point_font.render("Score = ", True, [0,0,0])
    life = 4
    background.set_alpha(180)
    heart_img = pygame.image.load("heart.png")
    heart_img = pygame.transform.scale(heart_img, (30,30))
    heart_font = pygame.font.SysFont("Arial",20)
    heart_text = point_font.render("="+str(life), True, [0,0,0])
    new_plat_vel = -3
    new_spike_vel = -3
    new_heart_vel = new_plat_vel
    new_star_vel = new_plat_vel
    ball = Mover(20,20)
    plats = [platform(new_plat_vel)]
    hearts_life = []
    stars = []
    spikes = []
    fps = 30
    bonuspoints = 0
    l = 800
    r = 1500
    y = 0
    
    magicrect = Rect(0, -50, 300, 2)
    x = randint(800,1500)
    pygame.time.set_timer(USEREVENT, x)  
    pygame.time.set_timer(USEREVENT+1, 25000)
    def update(screen,our_mover,plats,magicrect,clock,hearts_life,spikes,start_time,star,bonuspoints):
        global background, y
        screen.blit(background, [0,-(y%background.get_rect().height)])
        screen.blit(background, [0,-(y%background.get_rect().height)+background.get_rect().height])
        y -= ((new_plat_vel)/2)
        for plat in plats:
            plat.draw_special(screen)
        for spike in spikes:
            spike.draw_special(screen)
        for heart_life in hearts_life:
            heart_life.draw_special(screen)
        for star in stars:
            star.draw_special(screen)
        point_bar = pygame.draw.rect(screen,[240,230,140],Rect(0,0,600,25))
        our_mover.draw_special(screen)
        screen.blit(point_text, [200,3])
        clock_font = pygame.font.SysFont('Arial', 20)
        clock_point = (((pygame.time.get_ticks()-start_time)/1000)+bonuspoints)
        clock_text = clock_font.render(str(clock_point), True, [0,0,0])
        screen.blit(clock_text, [260,0])
        screen.blit(heart_text, [32,2])
        screen.blit(heart_img,[0,-3])
    
    
        pygame.display.flip()
    
    end_game = True
    start_time = pygame.time.get_ticks()
    while end_game:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    ball.set_vel(5,5)
                if event.key == K_LEFT:
                    ball.set_vel(-5,5)
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    ball.set_vel(0,5)
                if event.key == K_LEFT:
                    ball.set_vel(0,5)
            elif event.type == USEREVENT:
                    heart_added = False
                    star_added = False
                    p = platform(new_plat_vel)
                    plats.append(p)
                    chance1 = random.randint(0,10)
                    if chance1 == 2:
                        hearts_life.append(heart(p.rect,new_heart_vel))
                        heart_added = True
                    chance2 = random.randint(0,15)
                    if chance2 == 8:
                        stars.append(Star(p.rect,new_star_vel))
                        star_added = True
                    chance3 = random.randint(0,4)
                    if chance3 == 3:
                        spikes.append(Spike(new_spike_vel))
                        plats.remove(p)
                        if heart_added:
                            hearts_life.remove(hearts_life[-1])
                        if star_added:
                            stars.remove(stars[-1])
                    x = randint(l,r)
                    pygame.time.set_timer(USEREVENT, x)
            elif event.type == USEREVENT+1:
                l -= 50
                r -= 50
                if l <= 0:
                    l = 50
                if r < l:
                    r = l+50

                new_plat_vel -= 1
                new_spike_vel = new_plat_vel
                new_heart_vel = new_plat_vel
                new_star_vel = new_plat_vel
                for plat in plats:
                    plat.yvel = new_plat_vel
                for heart_life in hearts_life:
                    heart_life.yvel = new_heart_vel
                for spike in spikes:
                    spike.yvel = new_spike_vel
                for star in stars:
                    star.yvel = new_star_vel
    
        ball.move_self() 
    
        touched_plat = False
        for plat in plats:
            plat.move_self()
            if ball.rect.colliderect(plat.rect):
                max_implant = abs(ball.yvel) + abs(plat.yvel) * 2
                #print "Platform velocity:",plat.yvel,"Ball velocity:",ball.yvel,"Max implant:",max_implant,"Implant:",ball.rect.bottom-plat.rect.top
                if ball.rect.bottom - plat.rect.top <= max_implant:
                    ball.rect.bottom = plat.rect.top
                    ball.set_yvel(plat.yvel)
                    touched_plat = True
                else:
                    ball.move(-ball.xvel, 0)
            if plat.rect.colliderect(magicrect):
             plats.remove(plats[0])
        if not touched_plat:
            ball.yvel = 5
            
            
        for spike in spikes:
            spike.move_self()
            if ball.rect.colliderect(spike.rect):
                ball.relocate([150,50])
                ball.set_vel(0,5)
                life = life - 1
                heart_text = point_font.render("="+str(life), True, [0,0,0])
            if spike.rect.colliderect(magicrect):
                spikes.remove(spikes[0])
            
        if ball.rect.bottom < 50:
            ball.relocate([150,50])
            ball.set_vel(0,5)
            life = life - 1
            heart_text = point_font.render("="+str(life), True, [0,0,0])
        if ball.rect.top > 600:
            ball.relocate([150,50])
            ball.set_vel(0,5)
            life = life - 1
            heart_text = point_font.render("="+str(life), True, [0,0,0])
        if ball.rect.right < 0:
            ball.relocate([150,50])
            ball.set_vel(0,5)
            life = life - 1
            heart_text = point_font.render("="+str(life), True, [0,0,0])
        if ball.rect.left > 300:
            ball.relocate([150,50])
            ball.set_vel(0,5)
            life = life - 1
            heart_text = point_font.render("="+str(life), True, [0,0,0])
            
        for heart_life in hearts_life:
            heart_life.move_self()
            if ball.rect.colliderect(heart_life.rect):
                life = life + 1
                heart_text = point_font.render("="+str(life), True, [0,0,0])
                hearts_life.remove(heart_life)
        
        for star in stars:
            star.move_self()
            if ball.rect.colliderect(star.rect):
                bonuspoints += 20
                stars.remove(star)
            if star.rect.collidelist([h.rect for h in hearts_life]) != -1:
                stars.remove(star)
        
        if life < 0:
            end_game = False    
            
        update(screen,ball,plats,magicrect,my_clock,hearts_life,spikes,start_time,stars,bonuspoints)
            
        my_clock.tick(fps)
    
    screen.blit(background, [0,0])
    pygame.mouse.set_visible(True)
    over_font = pygame.font.SysFont("Arial", 30)
    over_text = over_font.render("Game Over", True, [0,0,0])
    score_text = over_font.render("Your Score is " + str(((pygame.time.get_ticks()- start_time)/1000)+bonuspoints), True, [0,0,0])

    screen.blit(over_text, [80,120])
    screen.blit(score_text, [60,245])
    retry_text = button_font.render("Retry", True, [0,0,0])
    quit_text = button_font.render("Quit", True, [0,0,0])
    ball = pygame.image.load("ball.png")
    ball = pygame.transform.scale(ball, (80,80))
    screen.blit(ball,[40,400])
    screen.blit(ball,[180,400])
    screen.blit(retry_text, [55,425])
    screen.blit(quit_text, [200,425])
    pygame.display.flip()
    
    start_game = True
    show_instructions = False
    my_clock = pygame.time.Clock()
    while start_game:
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                a = event.pos
                if distance ((60,450), a) < 40:
                    game = True
                    start_game = False
                if distance ((225,450), a) < 40:
                    game = False
                    start_game = False
                if start_game == True:
                    my_clock = 0


