import glfw
from EventSystem import EventSystem
from SubEventsSystem import MouseEventObserver, WindowEventObserver, KeyboardEventObserver, EmptyEventObserver
from OpenGL.GL import *
from OpenGL.GLU import *
from Logger import Logger
from Window import Window

class Engine:
    def __init__(self, file = None):
        self.EndLoopRunTime=5
        self.DisplaySize = None
        self.WindowDisplayName = None
        self.Events = EventSystem()
        self.MouseEventsObserver = MouseEventObserver()
        self.WindowEventsObserver = WindowEventObserver()
        self.KeyboardEventsObserver = KeyboardEventObserver()
        self.EmptyEventsObserver = EmptyEventObserver()
        self.Events.Register(EventType="MouseEvent", Event=self.MouseEventsObserver)
        self.Events.Register(EventType="KeyboardEvent", Event=self.KeyboardEventsObserver)
        self.Events.Register(EventType="EmptyEvent", Event=self.EmptyEventsObserver)
        self.Events.Register(EventType="WindowEvent", Event=self.WindowEventsObserver)
        if file != None:
            self.Logger = Logger(file.split("\\")[-1])
        else:
            self.Logger = Logger(__file__.split("\\")[-1])

        #setting up the supported colors
        self.Reset="\033[0m"
        self.Bright = "\033[1m"
        self.Dim = "\033[2m"
        #____________________________________________________# 
        self.NormalBright = "\033[22m"
        self.ForeBlack ="\033[30m"
        self.ForeRed = "\033[31m"
        self.ForeGreen = "\033[32m"
        self.ForeYellow = "\033[33m"
        self.ForeBlue = "\033[34m"
        self.ForeMagenta = "\033[35m"
        self.ForeCyan = "\033[36m"
        self.ForeWhite = "\033[37m"
        self.ForeReset = "\033[39m"
        #____________________________________________________#
        self.BackBlack = "\033[40m"
        self.BackRed = "\033[41m"
        self.BackGreen = "\033[42m"
        self.BackYellow = "\033[43m"
        self.BackBlue = "\033[44m"
        self.BackMagenta = "\033[45m"
        self.BackCyan = "\033[46m"
        self.BackWhite = "\033[47m"
        self.BackReset = "\033[49m"

        self.IsGLFW = False

        if not glfw.init():
            return
        else:
            self.IsGLFW=True

        self.Window = Window(self.Events)


    def Run(self, **kwargs):
        self.Window.Create(title=kwargs.get("title"), size=kwargs.get("size"))
        # Loop until the user closes the window
        self.ShouldWindowClose = self.Window.window_should_close()
        while (not self.ShouldWindowClose or self.EndLoopRunTime==0):
            self.Events.Reset()
            self.Events.CheckForEvents()
            #"""
            # Render here, e.g. using pyOpenGL

            # Swap front and back buffers
            self.Window.swap_buffers()

            if self.Events.IsWindowClosed():
                print("Hii")

            # Poll for and process events
            self.Window.poll_events()
            self.ShouldWindowClose = self.Window.window_should_close()
            if self.ShouldWindowClose == False:
                if self.Events.IsWindowClosed():
                    print("Hii")
                self.EndLoopRunTime -= 1
            #"""
        self.Terminate()

    def Terminate(self):
        if self.IsGLFW:
            glfw.terminate()
            self.Window.terminate()
        quit()

    def Log(self, typee, value):
        self.Logger.Log(typee, value)
    
    def addLoggingID(self, id, val):
        self.Logger.addID(id, val)
    
    def addLogType(self, **kwargs):
        self.Logger.add(Color=kwargs.get("Color"), Format = kwargs.get("Format"), Level=kwargs.get("Level"))


