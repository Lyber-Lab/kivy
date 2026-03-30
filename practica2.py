from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import NumericProperty

Builder.load_file('practica2.kv')

class Pantalla1(Screen):
    cuenta = NumericProperty(0)
    def contador(self):
        self.cuenta += 1

        if self.cuenta >= 10:
            self.manager.current = 'caso2'
            self.cuenta = 0

class Pantalla2(Screen):
    pass

class Administrador(ScreenManager):
    pass

class MiApp(App):
    def build(self):
        return Administrador()
    
if __name__ == '__main__':
    MiApp().run()
