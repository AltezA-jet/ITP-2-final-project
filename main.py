import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

player_x = 400
player_y = 300

running = True
while running:
    screen.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= 5
    if keys[pygame.K_d]:
        player_x += 5

    pygame.draw.rect(screen, (139,69,19), (player_x, player_y, 50, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
