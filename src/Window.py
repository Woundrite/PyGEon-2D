import glfw
import math
from OpenGL.GL import *
from Shapes import Triangle
from Dict import Dict

class Window():
    def __init__(self, EventSystem, Logger):
        self.Window = None
        self.Events = EventSystem
        self.DrawArr=[]
        self.Logger = Logger
    def Create(self, **kwargs):
        self.WindowDisplayName = kwargs.get('title')
        self.DisplaySize = kwargs.get('size')
        # Initialize the library
        if not glfw.init():
            return
        else:
            self.IsGLFW=True
        # Create a windowed mode window and its OpenGL context
        self.Window = glfw.create_window(self.DisplaySize[0], self.DisplaySize[1], self.WindowDisplayName, None, None)

        glfw.set_window_close_callback(self.Window, self.Events.SubEvents.get("WindowEvent").WindowCloseEvent)
        glfw.set_window_size_callback(self.Window, self.Events.SubEvents.get("WindowEvent").WindowResizeEvent)
        glfw.set_window_maximize_callback(self.Window, self.Events.SubEvents.get("WindowEvent").WindowMaximizeEvent)
        glfw.set_window_focus_callback(self.Window, self.Events.SubEvents.get("WindowEvent").WindowFocusedEvent)
        glfw.set_key_callback(self.Window, self.Events.SubEvents.get("KeyboardEvent").KeyEvent)
        glfw.set_mouse_button_callback(self.Window, self.Events.SubEvents.get("MouseEvent").MouseButtonEvent)
        glfw.set_cursor_pos_callback(self.Window, self.Events.SubEvents.get("MouseEvent").MouseMoveEvent)
        glfw.set_scroll_callback(self.Window, self.Events.SubEvents.get("MouseEvent").MouseScrollEvent)
        glfw.set_error_callback(self.Error)
        if not self.Window:
            glfw.terminate()
            return

        self.MakeContextCurrent()
    def Error(self, error, description):
        self.Logger.log("Error", "Error:{0}:: \n {1}".format(error, description))
    def poll_events(self):
        glfw.poll_events()
    def swap_buffers(self):
        glfw.swap_buffers(self.Window)
    def terminate(self):
        glfw.terminate()
    def window_should_close(self):
        return glfw.window_should_close(self.Window)
    def AddTriangleShape(self, x, y):
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_TRIANGLES)
        glVertex2f(x/100+0, y/100+0.5)
        glVertex2f(x/100-0.5, y/100-0.5)
        glVertex2f(x/100+0.5, y/100-0.5)
        glEnd()
    
    def MakeContextCurrent(self):
        # Make the window's context current
        glfw.make_context_current(self.Window)
        self.Events.SubEvents.get("WindowEvent").IsWindowCreated = True