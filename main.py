import pygame


# game variables
screen_size = 900


# main function
def main():
    # initialize pygame module
    pygame.init()

    # load and set the logo
    logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((screen_size, screen_size))

    # defining colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # drawing the grid
    screen.fill(black)
    pygame.draw.rect(screen, white, pygame.Rect(2, 2, screen_size - 2, screen_size - 2))

    pygame.draw.rect(screen, black, pygame.Rect(screen_size/3 - 1, 0, 2, screen_size))
    pygame.draw.rect(screen, black, pygame.Rect(2*screen_size/3 - 1, 0, 2, screen_size))
    pygame.draw.rect(screen, black, pygame.Rect(0, screen_size/3 - 1, screen_size, 2))
    pygame.draw.rect(screen, black, pygame.Rect(0, 2*screen_size/3 - 1, screen_size, 2))

    pygame.display.flip()

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, get all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                running = False


# run the main function
if __name__ == '__main__':
    print("Running main function")
    main()
