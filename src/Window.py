import glfw

class Window():
    def __init__(self):
        self.Window = None
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
        if not self.Window:
            glfw.terminate()
            return

        # Make the window's context current
        glfw.make_context_current(self.Window)
    def poll_events(self):
        glfw.poll_events()
    def swap_buffers(self):
        glfw.swap_buffers(self.Window)
    def terminate(self):
        glfw.terminate()
    def window_should_close(self):
        return glfw.window_should_close(self.Window)