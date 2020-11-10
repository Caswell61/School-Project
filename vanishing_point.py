# Write your code here :-)
from graphics import graphics
import random


def draw_sky(gui):
    '''
    Draws the sky and the land.
    gui should be a graphics object.
    '''
    gui.rectangle(0, 0, 600, 600, 'sky blue')
    gui.ellipse(475, 120, 100, 100, 'yellow')

def draw_clouds(gui, x_coord, y_coord):
    gui.ellipse(x_coord, y_coord, 110, 70, 'white')
    gui.ellipse(x_coord - 20, y_coord + 40, 140, 90, 'white')
    gui.text(5, 5, "x = " + str(gui.mouse_x), 'black')
    gui.text(5, 24, "y = " + str(gui.mouse_y), 'black')

def draw_landscape(gui):
    y = (gui.mouse_y * - 1.5) / 2
    size = 300 + y
    shape_x = ((y * -1) / 4) + 402
    shape_y = (((y * -1) / 10) ** 1.6)
    shift = shape_y / 8
    gui.rectangle(0, 400,600,600, 'green2')
    gui.triangle(140, 400, 300, size, 480, 400, 'brown')
    i = 0
    while i < 650:
        gui.line(i, 390, i, 400, 'dark green', 1)
        i += 3
    gui.rectangle(150, 400, 40, 100, 'brown')
    gui.rectangle(430, 400, 40, 100, 'brown')
    gui.ellipse(170, 380, 100, 130, 'dark green')
    gui.ellipse(450, 380, 100, 130, 'dark green')
    gui.ellipse(300, shape_x, shape_y, shift, 'dark blue')
def draw_hut(gui):
    '''
    This function SHOULD draw a hut.
    gui should be a graphics object.
    '''
    pass

def main():
    gui = graphics(600, 600, 'Vanishing Point')
    cloud1x, cloud1y = random.randint(10, 600), random.randint(0, 300)
    cloud2x, cloud2y = random.randint(10, 600), random.randint(0, 300)
    cloud3x, cloud3y = random.randint(10, 600), random.randint(0, 300)
    while True:
        gui.clear()
        draw_sky(gui)
        draw_clouds(gui, cloud1x, cloud1y)
        draw_clouds(gui, cloud2x, cloud2y)
        draw_clouds(gui, cloud3x, cloud3y)
        draw_landscape(gui)
        gui.update_frame(60)


main()
