from Engine import Engine

App = Engine()
App.CreateDisplay(title = "Hii", size = (700,700))
App.SetFPS(10)
while True:
    for event in App.Events():
        if event.type == App.quit:
            App.End()
    App.UpdateDisplay()