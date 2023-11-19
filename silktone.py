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
