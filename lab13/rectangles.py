import pygame #para que podamos usarlo

# Always begin with initialization, sizing, and captioning
pygame.init() #hace referencia ha initiate 
screen = pygame.display.set_mode((800, 600)) #touple
pygame.display.set_caption('Just a Simple Rectangle')

# Not strictly necessary, but good practice for readability
CELESTE = (188, 213, 242)
VERDE_AGUA = (188, 233, 213)
AZUL = (130, 193, 248)


# A best practice is to do the drawing in its own function
def draw_scene():
    screen.fill(CELESTE)  # "Clear the screen"
    the_rectangle = (300, 225, 200, 150)  # (x, y, width, height)
    pygame.draw.rect(screen, VERDE_AGUA, the_rectangle)  # filled
    pygame.draw.rect(screen, AZUL, the_rectangle, 3)  # outlined
    pygame.display.flip()  # Put the drawing on the screen


# Draw the scene then wait for the QUIT event to come in
draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit #es lo mismo como decir break to get out of the loop pero break solo cerraria el for loop 
        