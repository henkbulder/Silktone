#!bin/python3.11

from PIL import Image, ImageDraw
import numpy as np
from lloyd import Field
from scipy.spatial import Delaunay

def triangle_height(vertices):
    '''
    Returns the height (the distance between a vertex and opposing base) R to PQ.

    Parameter:
        vertices (list): the vertices of a triangle [P, Q, R]

    Returns:
        height (float)
    '''

    ((a, b), (c, d), (e, f)) = vertices
    
    #               2 x Area                   /        length PQ
    return (a*d - b*c + c*f - d*e + b*e - a*f) / np.sqrt((c - a)**2 + (d - b)**2)


def stochastic_field(shape=(800, 600), coverage=0.01, relaxation=50):
    '''
    Returns 2d array of given dimensions, filled with randomly distributed points.
    
    Parameters:
        shape (tuple, 2 ints): shape of the field
        coverage (float): coverage of the field with points, between 0 and 1
        relaxation (int): number of times the Lloyd's relaxation algorithm is applied to
            the points, where a higher number results in a more even distribution of
            points, which however will take longer to calculate.

    Returns:
        lexically sorted 2-dimensional array of zero's (0), and randomly distributed ones (1)
    '''
    screen = np.random.randint(0, [shape[0], shape[1]], size=[int(np.prod(shape) * coverage), 2])

    field = Field(screen)
    field.jitter_points()

    for _ in range(relaxation):
        print("\rapplying Lloyd's relaxation: "+str(int(_ / relaxation * 100))+"%", end="")
        field.relax()
    print("\rapplying Lloyd's relaxation: 100%", end="\r")
   
    res = field.get_points()

    return res[np.lexsort(screen.T[::-1])]


# TODO
# 
# Apply Delaunay triangulation on stochastic_field, find all triangle_heights for each simplex 
#
# Import image
# 
# Establish the encompassing simplex for each point/pixel of imported image 
#
# find the triangle_heights for each pixel relative to each side of encompassing simplex and
# devide by the simplex's triangle_height in the corresponding direction
#
# 
# 

###################################################################################################

if __name__ == "__main__":
    
    screen = stochastic_field()
    shape = (800, 600)
    path = "./img/test.png"

    image = Image.new("1", shape, color=0)
    draw = ImageDraw.Draw(image)
    count = 0
    
    for dot in screen:
        draw.point(tuple(dot), fill=1)
        count += 1
        
    image.save(path)
