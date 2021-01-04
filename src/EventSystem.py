from Dict import Dict
from SubEventsSystem import MouseEventObserver, WindowEventObserver, KeyboardEventObserver, EmptyEventObserver

def EventClassifier(Event):
    pass

class EventSystem():
    def __init__(self):
        self.SubEvents = Dict()
        self.Eventype = ["MouseEvent", "WindowEvent", "KeyboardEvent", "EmptyEvent"]
        self.EventSubType = {"MouseEvent" : ["MouseButtonDownEvent", "MouseButtonUpEvent", "MouseScrollDownEvent", "MouseScrollUpEvent", "MouseButtonPressedEvent"], "KeyboardEvent":["KeyPressedEvent", "KeyDownEvent", "KeyUpEvent"], "WindowEvent":["WindowFocusedEvent", "WindowUnfocusedEvent", "WindowCloseEvent", "WindowResizeEvent"], "EmptyEvent":"None"}
    
    def Register(self, **kwargs):
        self.SubEvents.append(kwargs.get("EventType"), kwargs.get("Event"))

    def Unregister(self, who):
        self.Observer.remove(who)
    
    def Send(self, **kwargs):
        for key, value in self.SubEvent:
            if key == kwargs.get("EventType", "EmptyEvent"):
                value.update(kwargs.get("Event", "Empty"))
    def CheckForEvents(self):
        pass

    def Reset(self):
        for key, value in self.SubEvents:
            value.Reset()
    
    def IsMouseButtonDown(self, code):
        for key, value in self.SubEvents:
            if key == "MouseEvent":
                if value.IsMouseButtonDown == True:
                    if code == "Any":
                        return True
                    else:
                        if value.MouseButtonDown == code:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False

    def IsMouseButtonUp(self, code):
        for key, value in self.SubEvents:
            if key == "MouseEvent":
                if value.IsMouseButtonUp == True:
                    if code == "Any":
                        return True
                    else:
                        if value.MouseButtonUp == code:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False

    def IsMouseButtonPressed(self, code):
        for key, value in self.SubEvents:
            if key == "MouseEvent":
                if value.IsMouseButtonPressed == True:
                    if code == "Any":
                        return True
                    else:
                        if value.MouseButtonPressed == code:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False
    #___________________________________
    def IsKeyDown(self, code):
        for key, value in self.SubEvents:
            if key == "KeyboardEvent":
                if value.IsKeyDown == True:
                    if code == "Any":
                        return True
                    else:
                        if value.KeyDown == code:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False

    def IsKeyUp(self, code):
        for key, value in self.SubEvents:
            if key == "KeyboardEvent":
                if value.IsKeyUp == True:
                    if code == "Any":
                        return True
                    else:
                        if value.KeyUp == code:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False

    def IsKeyPressed(self, code):
        for key, value in self.SubEvents:
            if key == "KeyboardEvent":
                if value.IsKeyPressed == True:
                    if code == "Any":
                        return True
                    else:
                        if value.KeyPressed == code:
                            return True
                        else:
                            return False
                else:
                    return False
            else:
                return False
        return False
    #___________________________________
    def GetKeyDown(self):
        for key, value in self.SubEvents:
            if key == "keyboardEvent":
                if value.KeyDown == "":
                    return None
                elif value.KeyDown == []:
                    return value.KeyDown
                else:
                    return str(value.KeyDown)
    def GetKeyUp(self):
        for key, value in self.SubEvents:
            if key == "keyboardEvent":
                if value.KeyUp == "":
                    return None
                elif value.KeyUp == []:
                    return value.KeyUp
                else:
                    return str(value.KeyUp)
    def GetKeyPressed(self):
        for key, value in self.SubEvents:
            if key == "keyboardEvent":
                if value.KeyPressed == "":
                    return None
                elif value.KeyPressed == []:
                    return value.KeyPressed
                else:
                    return str(value.KeyPressed)
    #___________________________________
    def GetMouseButtonDown(self):
        for key, value in self.SubEvents:
            if key == "MouseEvent":
                if value.MouseButtonDown == "":
                    return None
                elif value.MouseButtonDown == []:
                    return value.MouseButtonDown
                else:
                    return str(value.MouseButtonDown)
    def GetMousebuttonUp(self):
        for key, value in self.SubEvents:
            if key == "MouseEvent":
                if value.MouseButtonUp == "":
                    return None
                elif value.MouseButtonUp == []:
                    return value.MouseButtonUp
                else:
                    return str(value.MouseButtonUp)
    def GetMousebuttonPressed(self):
        for key, value in self.SubEvents:
            if key == "MouseEvent":
                if value.MouseButtonPressed == "":
                    return None
                elif value.MouseButtonPressed == []:
                    return value.MouseButtonPressed
                else:
                    return str(value.MouseButtonPressed)
    #____________________________________
    def OnWindowResize(self):
        return "a"
    def OnWindowFocus(self):
        return "a"
    def OnWindowUnfocus(self):
        return "a"
    def OnWindowClose(self):
        return "a"
    def OnWindowOpen(self):
        return "a"