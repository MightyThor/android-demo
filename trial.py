import kivy
kivy.require('1.5.1')

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout

class MainUI(FloatLayout):
    pass

class SerialBTApp(App):
    
    def build(self):
        #        root = MainUI()
        return MainUI()

if __name__=='__main__':
    SerialBTApp().run()
