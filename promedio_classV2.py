from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, DictProperty

Builder.load_file('promedio_classV2.kv')

class CalcularPromedio(Screen):
    notas = DictProperty({})
    mensaje = StringProperty("Ingresa un nombre de una materia y una nota (0-20)")

    def agregar_nota(self):
        texto_nota = self.ids.input_nota.text
        texto_nombre = self.ids.input_nombre.text.strip()

        try:
            nota = float(texto_nota)
            if 0 <= nota <= 20:
                nombre = str(texto_nombre)
                self.notas.update({nombre: nota})
                self.mensaje = f"Materia {len(self.notas)}: {nombre} y la nota añadida: {nota}"
                self.ids.input_nota.text = ""
                self.ids.input_nombre.text = ""
            else:
                self.mensaje = "Error: la nota debe ser de 0 a 20"
        except ValueError:
            self.mensaje = "Error: ingresa una nota válida"
    
    def calcular(self):
        cantidad = len(self.notas)
        if cantidad > 0:
            suma_nota = 0
            for materia, nota in self.notas.items():
                suma_nota += nota

            promedio = suma_nota / cantidad
            self.mensaje = f"Promedio Final ({cantidad} notas): {promedio:.2f}"
            self.notas = {}
        else:
            self.mensaje = "Error: no hay notas para calcular"

class PromedioApp(App): 
    def build(self):
        return CalcularPromedio()
    
if __name__ == '__main__':
    PromedioApp().run()