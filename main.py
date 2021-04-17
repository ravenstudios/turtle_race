from constants import *
import sys, pygame, turtle

clock = pygame.time.Clock()
screen_size = pygame.FULLSCREEN
surface = pygame.display.set_mode((0, 0), screen_size)
pygame.init()




turtles_group = 0


running = True
start_race = False




def main():
    global running, start_race

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
                    if start_race == False:
                        for t in turtles_group:
                            t.start()
                    start_race = True


        draw()
        if start_race == True:
            update()

    pygame.quit()
    sys.exit()



def draw():
    surface.fill((50, 50, 50))#background
    turtles_group.draw(surface)



    pygame.display.flip()


def update():
    global start_race
    turtles_group.update()

    if end_race():
        start_race = False
        for t in turtles_group:
            print(t.get_results())

def end_race():

    for t in turtles_group:
        if t.ended_race == False:
            return False

    return True

if __name__ == "__main__":


    turtles_group = pygame.sprite.Group()
    turtles_group.add(turtle.Turtle(1, 100, RED))
    turtles_group.add(turtle.Turtle(2, 200, GREEN))
    turtles_group.add(turtle.Turtle(3, 300, WHITE))
    turtles_group.add(turtle.Turtle(4, 400, BLUE))
    turtles_group.add(turtle.Turtle(5, 500, (80, 59, 43)))

    main()
