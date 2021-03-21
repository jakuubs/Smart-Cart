import definitions
import field
import plant
import pygame
import random
import soil
import tractor
pygame.display.set_caption("Smart Tractor")
def draw_window(tractor1_rectangle):
    definitions.WIN.fill(definitions.WHITE)
    definitions.WIN.blit(definitions.TRACTOR, (tractor1_rectangle.x, tractor1_rectangle.y))
    pygame.display.update()
def is_move_allowed(move, tractor1_rectangle):
    return True
def tractor1_handle_movement(tractor1, tractor1_rectangle):
    random1 = random.randint(1, 4)
    if (random == 1 and is_move_allowed(1, tractor1_rectangle) == True):
        tractor1.move_down()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
    elif (random == 2 and is_move_allowed(2, tractor1_rectangle) == True):
        tractor1.move_left()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
    elif (random == 3 and is_move_allowed(3, tractor1_rectangle) == True):
        tractor1.move_right()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
    elif (random == 4 and is_move_allowed(4, tractor1_rectangle) == True):
        tractor1.move_up()
        tractor1_rectangle.x = tractor1.get_x()
        tractor1_rectangle.y = tractor1.get_y()
def main():
    tractor1 = tractor.Tractor(0, 0)
    tractor1_rectangle = pygame.Rect(tractor1.get_x(), tractor1.get_y(), definitions.TRACTOR_WIDTH, definitions.TRACTOR_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(definitions.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        tractor1_handle_movement(tractor1, tractor1_rectangle)
        draw_window(tractor1_rectangle)
    pygame.quit()
if __name__ == "__main__":
    main()