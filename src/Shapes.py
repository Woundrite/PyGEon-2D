# a collection of base shapes for the window event system to draw and for the user to use
from OpenGL.GL import *
class Triangle():
    def __init__(self, x, y):
        pass
    def draw(self, x, y):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glVertex2f(x/100+0, y/100+0.5)
        glVertex2f(x/100-0.5, y/100-0.5)
        glVertex2f(x/100+0.5, y/100-0.5)
        glEnd()