import PySimpleGUI as sg
from question1 import main as q1
from question2 import main as q2
from question3 import main as q3
from testanswers import main as test
from architecture import main as arc

layout = [[sg.Text("Ficosa exam - Sergio Campos Gallego")],
          [sg.Button("Question 1")],
          [sg.Button("Question 2")],
          [sg.Button("Question 3")],
          [sg.Button("Architecture")],
          [sg.Button("Test")]]

# Create the window
window = sg.Window("FESCG", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    if event == "Question 1":
        q1.menu()
    if event == "Question 2":
        q2.menu()
    if event == "Question 3":
        q3.menu()
    if event == "Architecture":
        arc.menu()
    if event == "Test":
        test.menu()


window.close()
