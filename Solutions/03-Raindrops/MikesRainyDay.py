import pygame, sys, time, random


class Raindrop:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
        # self.speed = 2

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > 600

    def draw(self):
        pygame.draw.line(self.screen, (0, 0, 150), (self.x, self.y), (self.x, self.y + 5), 2)


class Hero:
    def __init__(self, screen, x, y, with_umbrella, without_umbrella):
        self.screen = screen
        self.x = x
        self.y = y
        self.image_with_umbrella = pygame.image.load(with_umbrella).convert()
        self.image_without_umbrella = pygame.image.load(without_umbrella).convert()
        self.last_hit_time = 0

    def draw(self):
        if time.time() > self.last_hit_time + 1:
            self.screen.blit(self.image_without_umbrella, (self.x, self.y))
        else:
            self.screen.blit(self.image_with_umbrella, (self.x, self.y))

    def hit_by(self, raindrop):
        return pygame.Rect(self.x, self.y, 170, 192).collidepoint((raindrop.x, raindrop.y))


class Cloud:
    def __init__(self, screen, x, y, image):
        self.screen = screen
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.raindrops = []

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        new_raindrop = Raindrop(self.screen, random.randint(self.x, self.x + 300), self.y + 100)
        self.raindrops.append(new_raindrop)


def main():
    print("ready")
    pygame.init()
    pygame.display.set_caption("Mike's Rainy Day")
    screen = pygame.display.set_mode((1000, 600))

    #  Make a Clock, Hero and Cloud with appropriate images, starting at appropriate positions.
    clock = pygame.time.Clock()
    # test_drop = Raindrop(screen, 320, 10)  # Test code
    mike = Hero(screen, 300, 400, "Mike_umbrella.png", "Mike.png")

    cloud = Cloud(screen, 300, 50, "cloud.png")

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Move the cloud (notice this is AFTER the event loop).
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_RIGHT] and event.type == pygame.KEYDOWN:
            cloud.x = cloud.x + 5
        if pressed_keys[pygame.K_LEFT] and event.type == pygame.KEYDOWN:
            cloud.x = cloud.x - 5
        if pressed_keys[pygame.K_UP] and event.type == pygame.KEYDOWN:
            cloud.y = cloud.y - 5
        if pressed_keys[pygame.K_DOWN] and event.type == pygame.KEYDOWN:
            cloud.y = cloud.y + 5

        screen.fill((255, 255, 255))

        # Test code that is removed for the final version of the code.
        # test_drop.move()
        # if test_drop.off_screen():
        #     test_drop.y = 10
        # test_drop.draw()
        # if mike.hit_by(test_drop):
        #     mike.last_hit_time = time.time()

        cloud.draw()

        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()

                # Optionally remove the raindrop from the list in these cases.
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        mike.draw()
        pygame.display.update()


main()
