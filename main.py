import pygame, fruit, snake, sys, random

if __name__ == '__main__':
    pygame.init()
    
    screen_height = 1280
    screen_width = 720

    screen = pygame.display.set_mode((screen_height, screen_width))
    clock = pygame.time.Clock()
    dt = 0
    pygame.mouse.set_visible(False)
    
    y = None
    x = None

    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    snake = snake.Snake(30, 30, 100, 100, (0,255,0))

    fruit = fruit.Fruit(30, 30, random.randrange(0, screen_width), random.randrange(0, screen_height), (255,0,0))
    
    #snake group
    snake_group = pygame.sprite.Group()
    snake_group.add(snake)
    #fruit group
    fruit_group = pygame.sprite.Group()
    fruit_group.add(fruit)

    while True:
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        snake_group.draw(screen)
        fruit_group.draw(screen)
        snake_group.update(player_pos.x,player_pos.y)
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            y = True
            x = None
        if keys[pygame.K_s]:
            y = False
            x = None
        if keys[pygame.K_a]:
            x = False
            y = None
        if keys[pygame.K_d]:
            x = True
            y = None
        
        if y == True:
            player_pos.y -= 300 * dt
        elif y == False:
            player_pos.y += 300 * dt
        if x == True:
            player_pos.x += 300 * dt
        elif x == False:
            player_pos.x -= 300 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

            