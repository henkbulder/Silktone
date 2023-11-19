#!bin/python3.11

from PIL import Image, ImageDraw
import numpy as np
from lloyd import Field
from scipy.spatial import Delaunay

def triangle_height(vertices):
    '''
    Returns the heigth (length of altitude) of R to PQ.

    Parameter:
        vertices (list): the vertices of a triangle [P, Q, R]

    Returns:
        height (float)
    '''

    ((a, b), (c, d), (e, f)) = vertices
    
    return (a*d - b*c + c*f - d*e + b*e - a*f) / np.sqrt((c - a)**2 + (d - b)**2)

triangle = [(0, 10), (20,20),(15, 0)]

def stochastic_dot_screen(width=800, height=600, coverage=0.01, relaxation=20):
    '''
    Returns 2d array of given dimensions, filled with randomly distributed dots.
    
    Parameters:
        width (int): width in 'pixels'
        height (int): height in 'pixels'
        coverage (float): amount of randomly placed dots, between 0 and 1
        relaxation (int): number of times the Lloyd's relaxation algorithm is applied to
            the dot screen, where a higher number results in a more even distribution of
            dots, however taking longer to calculate.

    Returns:
        lexically sorted 2-dimensional array of zero's (0), and randomly distributed ones (1)
    '''
    screen = np.random.randint(0, [width, height], size=[int(width * height * coverage), 2])
    
    #
    # TODO
    #
    # implement Lloyd's relaxation
    #
    #

    return screen[np.lexsort(screen.T[::-1])]


if __name__ == "__main__":
    
    screen = stochastic_dot_screen()
    shape = (800, 600)
    path = "./img/test.png"

    image = Image.new('1', shape, color=0)
    draw = ImageDraw.Draw(image)
    count = 0
    
    for dot in screen:
        print('\r', int(count / 4800 * 100), '%', end='')
        draw.point(tuple(dot), fill=1)
        count += 1
    print('\r100')
        
    image.save(path)


