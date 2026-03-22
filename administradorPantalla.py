from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('administradorPantalla.kv')

class PantallaContador(Screen):
    pass

class PantallaExito(Screen):
    pass

class AdministradorPantalla(ScreenManager):
    pass

class MiApp(App):
    def build(self):
        return AdministradorPantalla()
    
if __name__ == '__main__':
    MiApp().run()