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
        pass
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


    def WindowFocusedEvent(self):
        pass
    
    def WindowUnfocusedEvent(self):
        pass
    
    def WindowCloseEvent(self):
        pass
    
    def WindowResizeEvent(self):
        pass
    def Reset(self):
        pass

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