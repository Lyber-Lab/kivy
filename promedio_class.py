from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

Builder.load_file('promedio_class.kv')

class CalcularPromedio(Screen):
    notas = ListProperty([])
    mensaje = StringProperty("Ingresa una nota (0-20)")

    def agregar_nota(self):
        texto_nota = self.ids.input_nota.text

        try:
            nota = float(texto_nota)
            if 0 <= nota <= 20:
                self.notas.append(nota)
                self.mensaje = f"Nota {len(self.notas)} añadida: {nota}"
                self.ids.input_nota.text = ""
            else:
                self.mensaje = "Error: la nota debe ser de 0 a 20"
        except ValueError:
            self.mensaje = "Error: ingresa una nota válida"
    
    def calcular(self):
        if len(self.notas) > 0:
            promedio = sum(self.notas) / len(self.notas)
            self.mensaje = f"Promedio Final ({len(self.notas)} notas): {promedio:.2f}"
            self.notas = []
        else:
            self.mensaje = "Error: no hay notas para calcular"

class PromedioApp(App): 
    def build(self):
        return CalcularPromedio()
    
if __name__ == '__main__':
    PromedioApp().run()