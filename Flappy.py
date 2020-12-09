import pygame, sys

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900+in_laptop))
    screen.blit(floor_surface, (floor_x_pos + 576,900+in_laptop))


pygame.init()
in_laptop = 0
in_laptop = -200

#game variables
gravity = 0.25
bird_movement = 0
screen = pygame.display.set_mode((576, 1024+in_laptop))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

bird_surface = pygame.image.load("assets/bluebird-midflap.png").convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100, 512 + in_laptop/2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement = -10

    screen.blit(bg_surface,(0,0+in_laptop))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
