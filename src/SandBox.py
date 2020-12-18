from Engine import Engine
from Logger import Logger
"""
App = Engine()
App.CreateDisplay(title = "Hii", size = (700,700))
App.SetFPS(10)
while True:
    for event in App.Events():
        if event.type == App.quit:
            App.End()
    App.UpdateDisplay()
"""
test = Logger(__file__)
test.Log("error", "warning to someone")
test.Log("info", "jsjksdjjd")
test.Log("text", "kpsdlkv")

test.add(Level = "test", Color=test.ForeMagenta)

test.Log("test", "yada yada")