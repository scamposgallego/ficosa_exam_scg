from .ShapeFactory import ShapeFactory
import PySimpleGUI as sg

class FactoryPatternDemo():
    def __init__(self):
        sf = ShapeFactory()
        sh1 = sf.get_shape('circle')
        sh2 = sf.get_shape('rectangle')
        sh3 = sf.get_shape('square')
        sg.popup(sh1.draw(),
                 sh2.draw(),
                 sh3.draw()
                 )


def menu():
    FactoryPatternDemo()
