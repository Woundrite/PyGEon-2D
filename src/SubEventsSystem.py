import glfw

class MouseEventObserver():
    def __init__(self):
        self.IsMouseButtonDown = False
        self.IsMouseButtonUp = False
        self.IsMouseButtonPressed = False
        self.MouseButtonDown = ""
        self.MouseButtonUp = ""
        self.MouseButtonPressed = ""
    def update(self, Message):
        if Message == None or Message == "None":
            pass
        elif Message == "MouseButtonDown":
            self.MouseButtonDownEvent()
        elif Message == "MouseButtonPressed":
            self.MouseButtonPressedEvent()
        elif Message == "MouseScrollUp":
            self.MouseScrollUpEvent()
        elif Message == "MouseScrollDown":
            self.MouseScrollDownEvent()
        elif Message == "MouseButtonUp":
            self.MouseButtonUpEvent()

    def MouseButtonEvent(self, Window, button, action, modes):
        if action == glfw.PRESS:
            self.MouseButtonDownEvent()
            print(action)
        elif action == glfw.RELEASE:
            self.MouseButtonUpEvent()
            print(action)
        else:
            print(action)

    def MouseMoveEvent(self, Window, MouseX, MouseY):
        self.X = MouseX
        self.Y = MouseY

    def MouseScrollEvent(self, Window, XOffset, YOffset):
        if YOffset < 0:
            self.ScrollDownEvent()
        elif YOffset > 0:
            self.ScrollUpEvent()

    def MouseButtonPressedEvent(self):
        pass
    
    def MouseScrollUpEvent(self):
        pass
    
    def MouseScrollDownEvent(self):
        pass
    
    def MouseButtonUpEvent(self):
        pass
    
    def MouseButtonDownEvent(self):
        pass

    def Reset(self):
        self.IsMouseButtonDown = False
        self.IsMouseButtonUp = False
        self.IsMouseButtonPressed = False
        self.MouseButtonDown = ""
        self.MouseButtonUp = ""
        self.MouseButtonPressed = ""

class WindowEventObserver():
    def __init__(self):
        self.WindowCloseCallback=None
        self.IsWindowResized = False
        self.IsWindowMaximized = False
        self.IsWindowFocused = False
        self.IsWindowCreated = False

    def update(self, Message):
        if Message == None or Message == "None":
            pass
        elif Message == "WindowFocused":
            self.WindowFocusedEvent()
        elif Message == "WindowUnfocused":
            self.WindowUnfocusedEvent()
        elif Message == "WindowClose":
            self.WindowCloseEvent()
        elif Message == "WindowResize":
            self.WindowResizeEvent()

    def WindowFocusedEvent(self, Window, Code):
        self.IsWindowFocused = True
    
    def WindowUnfocusedEvent(self):
        pass
    
    def WindowCloseEvent(self, Window):
        if self.WindowCloseEvent!=None:
            if callable(self.WindowCloseCallback):
                self.WindowCloseCallback()

    def WindowResizeEvent(self, Window, Width, Height):
        self.IsWindowResized = True
    
    def WindowMaximizeEvent(self, window, Size):
        self.IsWindowMaximized = True

    def Reset(self):
        self.IsWindowResized = False
        self.IsWindowMaximized = False
        self.IsWindowFocused = False
        self.IsWindowCreated = False


class KeyboardEventObserver():
    def __init__(self):
        self.IsKeyDown = False
        self.IsKeyUp = False
        self.IsKeyPressed = False
        self.KeyDown = ""
        self.KeyUp = ""
        self.KeyPressed = ""
    def update(self, Message):
        if Message == None or Message == "None":
            pass
        elif Message == "KeyPressed":
            self.KeyPressedEvent()
        elif Message == "KeyUp":
            self.KeyUpEvent()
        elif Message == "KeyDown":
            self.KeyDownEvent()

    def KeyEvent(self, Window, KeyID, ScanCode, ActionType, Mods):
        if ActionType == glfw.PRESS:
            self.KeyDownEvent()
        elif ActionType == glfw.RELEASE:
            self.KeyUpEvent()
        elif ActionType == glfw.REPEAT:
            self.KeyPressedEvent()
        else:
            self.OtherKeyEvent()

    def KeyUpEvent(self):
        pass

    def KeyDownEvent(self):
        pass
    
    def KeyPressedEvent(self):
        pass

    def Reset(self):
        self.IsKeyDown = False
        self.IsKeyUp = False
        self.IsKeyPressed = False
        self.KeyDown = ""
        self.KeyUp = ""
        self.KeyPressed = ""

class EmptyEventObserver():
    def __init__(self):
        pass
    def update(self):
        pass
    def Reset(self):
        pass