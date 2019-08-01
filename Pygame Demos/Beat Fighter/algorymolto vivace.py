# Developed by Isabella Patterson, Allison Abernathie, and Cassandra Lutes
# First Place Project for 2019 Operation Catapult Session 2! 

import pygame
import time
import sys

class Dancer:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = 204
        self.y = 170

        self.image_idle = pygame.image.load('dancer_idle.png')
        self.image_idle = pygame.transform.scale(self.image_idle, (233, 300))
        self.image_leftpunch = pygame.image.load('dancer_leftpunch.png')
        self.image_leftpunch = pygame.transform.scale(self.image_leftpunch, (233, 300))
        self.image_rightpunch = pygame.image.load('dancer_rightpunch.png')
        self.image_rightpunch = pygame.transform.scale(self.image_rightpunch, (233, 300))
        self.image_uppunch = pygame.image.load('dancer_uppunch.png')
        self.image_uppunch = pygame.transform.scale(self.image_uppunch, (233, 300))
        self.image_downpunch = pygame.image.load('dancer_downpunch.png')
        self.image_downpunch = pygame.transform.scale(self.image_downpunch, (233, 300))
        self.image_idle.set_colorkey((0, 0, 0))
        self.image_leftpunch.set_colorkey((0, 0, 0))
        self.image_rightpunch.set_colorkey((0, 0, 0))
        self.image_uppunch.set_colorkey((0, 0, 0))
        self.image_downpunch.set_colorkey((0, 0, 0))

    def draw(self):
        self.screen.blit(self.image_idle, (self.x, self.y))

    def punch_left(self):
        self.screen.blit(self.image_leftpunch, (self.x, self.y))

    def punch_right(self):
        self.screen.blit(self.image_rightpunch, (self.x, self.y))

    def punch_up(self):
        self.screen.blit(self.image_uppunch, (self.x, self.y))

    def punch_down(self):
        self.screen.blit(self.image_downpunch, (self.x, self.y+100))

class Orb:
    def __init__(self, screen, direction):
        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height
        self.color = (0, 0, 0)
        self.xspeed = 0
        self.yspeed = 0
        self.x = 0
        self.y = 0
        self.direction = direction
        self.isdead = False
        if self.direction == 'up':
            self.x = self.screen_width // 2
            self.y = self.screen_height + 30
            self.color = (255, 240, 0)
            self.yspeed = -2
        elif self.direction == 'down':
            self.x = self.screen_width // 2
            self.y = -30
            self.color = (191, 0, 254)
            self.yspeed = 2
        elif self.direction == 'left':
            self.x = -30
            self.y = self.screen_height // 2
            self.color = (230, 10, 150)
            self.xspeed = 2
        elif self.direction == 'right':
            self.x = self.screen_width + 30
            self.y = self.screen_height // 2
            self.color = (0, 255, 225)
            self.xspeed = -2

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), 30)

    def hit_by(self, punchDirection):
        return pygame.Rect(94, 60, 453, 520).collidepoint((self.x, self.y)) and punchDirection == self.direction

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed


class HPBar:
    def __init__(self, screen):
        self.screen = screen
        self.score = 1000
        self.font = pygame.font.Font(None, 30)

    def draw(self):
        for hp in range(self.score // 100):
            pygame.draw.rect(self.screen, (255, hp * 25, 0), (5 + 20 * (hp), 5, 20, 10))
        # text_as_image = self.font.render("Health:" + str(self.score), True, (155, 75, 160))
        # self.screen.blit(text_as_image, (5, 5))


class Face:
    def __init__(self, screen, name):
        self.screen = screen
        if name == "Jared":
            self.image = pygame.image.load("Jared.png")
        if name == "Susan":
            self.image = pygame.image.load("Susan.png")
        if name == "Jackson":
            self.image = pygame.image.load("Jackson.png")
        self.position = "i"

    def draw(self):
        x = 0
        y = 0
        image = pygame.transform.scale(self.image, (100, 100))
        if self.position == "i":
            x = 240
            y = 130
        elif self.position == "u":
            x = 240
            y = 190
            image = pygame.transform.scale(self.image, (80, 80))
        elif self.position == "d":
            x = 235
            y = 300
            image = pygame.transform.scale(self.image, (80, 80))
        elif self.position == "r":
            x = 230
            y = 130
        elif self.position == "l":
            x = 310
            y = 130
        self.screen.blit(image, (x, y))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    # start screen
    pygame.display.set_caption("Beat Fighter")
    screen = pygame.display.set_mode((640, 640))
    intro = True
    counselors = ["Jared", "Susan", "Jackson"]
    songs = ["albatraoz.mp3", "old_town_road_diplo.mp3", "EXO Power.mp3", "Chicken Dance.mp3"]
    song_files = ["albatraoz_bk.txt", "old_town_road.txt", "Power.txt", "chicken_dance.txt"]
    counselor_num = 0
    song_num = 0
    selection_row = 0
    backflash = False
    pygame.mixer.music.load("if elevators had trap music.mp3")
    pygame.mixer.music.play(10, 19)
    while intro:
        screen.fill((0, 0, 0,))
        screen.blit(pygame.font.Font(None, 28).render("Press arrow keys to punch in that direction.", True, (255, 255, 255)), (30, 500))
        screen.blit(pygame.font.Font(None, 28).render("Punch the orbs in time to the music.", True, (255, 255, 255)), (30,530))
        screen.blit(pygame.font.Font(None, 28).render("Press space at any time to reset.", True, (255, 255, 255)), (30, 560))
        screen.blit(pygame.font.Font(None, 12).render("press s to toggle background", True, (255, 255, 255)), (500, 600))
        if backflash:
            screen.blit(pygame.font.Font(None, 12).render("ON", True, (255, 255, 255)), (550, 615))
        screen.blit(pygame.font.Font(pygame.font.match_font('impact'), 64).render("Beat Fighter", True, (0, 150, 150)), (170, 10))
        if selection_row == 0:
            pygame.draw.rect(screen, (0, 0, 100), (25, 95, 590, 30))
        elif selection_row == 1:
            pygame.draw.rect(screen, (0, 0, 100), (25, 195, 590, 30))
        elif selection_row == 2:
            pygame.draw.rect(screen, (0, 0, 100), (25, 295, 590, 30))
        counselor_text = pygame.font.Font(None, 28).render(counselors[counselor_num], True, (255, 255, 255))
        screen.blit(counselor_text, (30, 100))
        song_text = pygame.font.Font(None, 28).render(songs[song_num], True, (255, 255, 255))
        screen.blit(song_text, (30, 200))
        if selection_row == 2:
            screen.blit(pygame.font.Font(None, 28).render("Press Enter to Start", True, (255, 255, 255)), (30, 300))
        else:
            screen.blit(pygame.font.Font(None, 28).render("Start?", True, (255, 255, 255)), (30, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pressedkeys = pygame.key.get_pressed()
            if pressedkeys[pygame.K_UP]:
                selection_row -= 1
                if selection_row < 0:
                    selection_row = 2
            if pressedkeys[pygame.K_DOWN]:
                selection_row += 1
                if selection_row > 2:
                    selection_row = 0
            if pressedkeys[pygame.K_LEFT]:
                if selection_row == 0:
                    counselor_num -= 1
                    if counselor_num < 0:
                        counselor_num = len(counselors) - 1
                elif selection_row == 1:
                    song_num -= 1
                    if song_num < 0:
                        song_num = len(songs) - 1
            if pressedkeys[pygame.K_RIGHT]:
                if selection_row == 0:
                    counselor_num += 1
                    if counselor_num > len(counselors) - 1:
                        counselor_num = 0
                elif selection_row == 1:
                    song_num += 1
                    if song_num > len(songs) - 1:
                        song_num = 0
            if pressedkeys[pygame.K_RETURN] or pressedkeys[pygame.K_KP_ENTER]:
                if selection_row == 2:
                    intro = False
            if pressedkeys[pygame.K_s]:
                if backflash:
                    backflash = False
                else:
                    backflash = True
    #setup
    hpbar = HPBar(screen)
    face = Face(screen, counselors[counselor_num])
    dancer = Dancer(screen, 90, 90)
    funished = pygame.image.load("Funished.png")
    winner = pygame.image.load("victory_screen.png")
    winner = pygame.transform.scale(winner, (640, 640))
    pygame.mixer.music.load(songs[song_num])
    punchbox = (129, 95, 383, 450)
    hurtbox = (204, 170, 233, 300)
    orblist = []
    timeline_dict = {}
    with open(song_files[song_num]) as file:
        for line in file:
            line = line.rstrip('\n')
            current_line = line.split(',')
            time_ms = int(current_line[0])
            action = current_line[1]
            timeline_dict[time_ms] = action
    background_image_frames = []
    background_image_frames.append(pygame.image.load("frame_00.gif"))
    background_image_frames.append(pygame.image.load("frame_01.gif"))
    background_image_frames.append(pygame.image.load("frame_02.gif"))
    background_image_frames.append(pygame.image.load("frame_03.gif"))
    background_image_frames.append(pygame.image.load("frame_04.gif"))
    background_image_frames.append(pygame.image.load("frame_05.gif"))
    background_image_frames.append(pygame.image.load("frame_06.gif"))
    background_image_frames.append(pygame.image.load("frame_07.gif"))
    background_image_frames.append(pygame.image.load("frame_08.gif"))
    background_image_frames.append(pygame.image.load("frame_09.gif"))
    background_image_frames.append(pygame.image.load("frame_10.gif"))
    background_image_frames.append(pygame.image.load("frame_11.gif"))
    background_image_frames.append(pygame.image.load("frame_12.gif"))
    current_image = 0
    is_game_over = False
    pygame.mixer.music.play()
    start_milli_time = int(round(time.time() * 1000))
    #  main game loop
    gameplay = True
    win = False
    while gameplay:
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE]:
            gameplay = False
        clock.tick(250)
        if backflash:
            screen.blit(background_image_frames[current_image], (0,0))
            current_image = (current_image + 1) % len(background_image_frames)
        else:
            screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 0, 15), punchbox)
        pygame.draw.rect(screen, (0, 0, 0), hurtbox)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
        hpbar.draw()

        current_milli_time = int(round(time.time() * 1000))
        time_since_start = current_milli_time - start_milli_time
        rounded_time = time_since_start - time_since_start % 5

        if rounded_time in timeline_dict:
            action = timeline_dict[rounded_time]
            if action == 'over' and not is_game_over:
                is_game_over = True
                win = True
                pygame.mixer.music.stop()
                pygame.mixer.music.load("win_music.mp3")
                pygame.mixer.music.play()
            else:
                orb = Orb(screen, action)
                orblist.append(orb)

        punchway = ''
        if not is_game_over:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_DOWN]:
                dancer.punch_down()
                punchway = 'up'
                face.position = "d"
            elif pressed_keys[pygame.K_UP]:
                dancer.punch_up()
                punchway = 'down'
                face.position = "u"
            elif pressed_keys[pygame.K_LEFT]:
                dancer.punch_left()
                punchway = 'left'
                face.position = "l"
            elif pressed_keys[pygame.K_RIGHT]:
                dancer.punch_right()
                punchway = 'right'
                face.position = "r"
            else:
                dancer.draw()
                face.position = "i"
            face.draw()

            if hpbar == 0:
                is_game_over = True
            # deal with orbs
            for orb in orblist:
                orb.move()
                orb.draw()
                if pygame.Rect(hurtbox).collidepoint((orb.x, orb.y)):
                    hpbar.score -= 100
                    orb.isdead = True
                if orb.hit_by(punchway):
                    orb.isdead = True
            pygame.display.update()
            for orb in orblist:
                if orb.isdead:
                    orblist.remove(orb)

        if hpbar.score <= 0:
            pygame.mixer.music.stop()
            is_game_over = True
            hpbar.score = 69
            pygame.mixer.music.load("My Heart Will Go On (terrible recorder meme).mp3")
            pygame.mixer.music.play(1, 19)
        if is_game_over:
            if win:
                screen.blit(winner, (0, 0))
                pygame.display.update()
            else:
                screen.blit(funished, (-150, 0))
                pygame.display.update()


while True:
    main()
    pygame.mixer.music.stop()
