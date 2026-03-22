from kivy.app import App
from kivy.uix.button import Button

class testApp(App):
    def build(self):
        return Button(text='¡Kivy funcionando correctamente!', 
                      font_size = '20sp')

if __name__ == '__main__':
    testApp().run()