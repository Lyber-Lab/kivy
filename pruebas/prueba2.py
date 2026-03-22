from kivy.app import App
from kivy.uix.screenmanager import Screen

class pantalla(Screen):
    def validar_usuario(self):
        print("Intentando conectar con el servidor")


class Miapp(App):
    def build(self):
        return pantalla()

if __name__ == '__main__':
    Miapp().run()