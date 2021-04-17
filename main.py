from constants import *
import sys, pygame, turtle

clock = pygame.time.Clock()
screen_size = pygame.FULLSCREEN
surface = pygame.display.set_mode((0, 0), screen_size)
pygame.init()




turtles_group = 0







def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Keyboard
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()

                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_r:
                    # Reset map
                    pass

            if event.type == pygame.KEYUP:
                if event.key == 32:#SPACE
                    # updates the bomb group when you set a bomb

                    pass

        draw()
        update()

    pygame.quit()
    sys.exit()



def draw():
    surface.fill((100, 100, 100))#background
    turtles_group.draw(surface)



    pygame.display.flip()


def update():

    turtles_group.update()


if __name__ == "__main__":


    turtles_group = pygame.sprite.Group()
    turtles_group.add(turtle.Turtle(100, RED))
    main()
