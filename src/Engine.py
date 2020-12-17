import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Engine:
    def __init__(self):
        self.DisplaySize = None
        self.WindowDisplayName = None
        self.events = None
        self.quit = pygame.QUIT
        self.fps = 100

    def CreateDisplay(self, **kwargs):
        pygame.init()
        self.WindowDisplayName = kwargs.get('title')
        self.DisplaySize = kwargs.get('size')
        pygame.display.set_caption(self.WindowDisplayName)
        pygame.display.set_mode(self.DisplaySize, DOUBLEBUF|OPENGL|RESIZABLE)


    def UpdateDisplay(self):
        pygame.display.flip()
        pygame.time.wait(self.fps)

    def Events(self):
        self.events = pygame.event.get()
        return self.events
    
    def SetFPS(self, fps):
        self.fps = fps
    
    def End(self):
        pygame.quit()
        quit()
        print("endii")