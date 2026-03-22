from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder

Builder.load_file('ejercicio1.kv')

class PantallaContador(Screen): 
    cuenta = NumericProperty(0) 

    def contadorSuma(self):
        self.cuenta += 1
    def contadorResta(self):
        self.cuenta -= 1
    def multiPorDos(self):
        self.cuenta *= 2
    def dividir2(self):
        self.cuenta //= 2

class MiApp(App):
    def build(self):
        return PantallaContador()
    
if __name__ == '__main__':
    MiApp().run()