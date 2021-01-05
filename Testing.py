import pygame

from physics import colliders

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

box = colliders.BoxCollider(100, 100, 32, 32, True, 0.1, 5)

mouse_rect = colliders.BoxCollider(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)

while True:
    events = pygame.event.get()

    screen.fill((0, 0, 0))
    
    mouse_rect.x, mouse_rect.y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

    # if box.collide_point(pygame.mouse.get_pos()):
    if box.collide_rect(mouse_rect):
        pygame.draw.rect(screen, (255, 0, 0), box.rect, 1)
    else:
        pygame.draw.rect(screen, (255, 255, 255), box.rect, 1)
    
    box.update()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                box.y = 100
    
    pygame.display.update()
    clock.tick(60)