import PySimpleGUI as sg
from . import FifoList as fl


def menu():
    fifo_list = fl.FifoList()

    layout = [[sg.Text('FIFO LIST')],
              [sg.Output(size=(50,10), key='-OUTPUT-')],
              [sg.InputText()],
              [sg.Button('Add'),
               sg.Button('Remove oldest'),
               sg.Button('Get size'),
               sg.Button('Get times'),
               sg.Button('Exit')]
              ]

    window = sg.Window('Window Title', layout)

    # Event Loop
    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == 'Add':
            window['-OUTPUT-'].update('')
            item = values[0]
            fifo_list.push(item)
            print("Item added with ID {}\n".format(item))
        if event == 'Remove oldest':
            window['-OUTPUT-'].update('')
            fifo_list.pop()
            print("Oldest element dequed\n")
        if event == 'Get size':
            window['-OUTPUT-'].update('')
            print("Queue size: {}\n".format(fifo_list.size()))
        if event == 'Get times':
            window['-OUTPUT-'].update('')
            print(fifo_list.times())

    window.close()
    5