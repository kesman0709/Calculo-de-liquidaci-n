from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from model.logica_liquidacion import (
    DatosLiquidacion,
    calcular_liquidacion,
    SalarioInvalido,
    DiasInvalidos,
    VacacionesInvalidas,
    IndemnizacionInvalida,
)


class LiquidacionApp(App):

    def build(self):
        contenedor = GridLayout(cols=2, padding=20, spacing=10)


        contenedor.add_widget(Label(text="Salario por hora"))
        self.salario = TextInput(text="0")
        contenedor.add_widget(self.salario)

        contenedor.add_widget(Label(text="Días trabajados"))
        self.dias = TextInput(text="0")
        contenedor.add_widget(self.dias)

        contenedor.add_widget(Label(text="Vacaciones pendientes"))
        self.vacaciones = TextInput(text="0")
        contenedor.add_widget(self.vacaciones)

        contenedor.add_widget(Label(text="Aplica indemnización (1=Sí, 0=No)"))
        self.aplica = TextInput(text="0")
        contenedor.add_widget(self.aplica)

        contenedor.add_widget(Label(text="Valor indemnización"))
        self.indemnizacion = TextInput(text="0")
        contenedor.add_widget(self.indemnizacion)

    
        self.resultado = Label(text="Resultado: ")
        contenedor.add_widget(self.resultado)

        
        calcular = Button(text="Calcular")
        contenedor.add_widget(calcular)

        calcular.bind(on_press=self.calcular)

        return contenedor

    def calcular(self, instance):
        try:
            self.validar()
            datos = DatosLiquidacion(
                salario_hora=float(self.salario.text),
                dias_trabajados=int(self.dias.text),
                vacaciones_pendientes=int(self.vacaciones.text),
                aplica_indemnizacion=bool(int(self.aplica.text)),
                valor_indemnizacion=float(self.indemnizacion.text),
            )
            total = calcular_liquidacion(datos)
            self.resultado.text = "Total a pagar: " + str(total)
        except ValueError as err:
            self.mostrar_error(str(err))
        except SalarioInvalido as err:
            self.mostrar_error("El salario por hora debe ser mayor a 0.\n" + str(err))
        except DiasInvalidos as err:
            self.mostrar_error("Los días trabajados deben estar entre 1 y 30.\n" + str(err))
        except VacacionesInvalidas as err:
            self.mostrar_error("Las vacaciones pendientes no pueden ser negativas.\n" + str(err))
        except IndemnizacionInvalida as err:
            self.mostrar_error("El valor de indemnización no puede ser negativo.\n" + str(err))
        except Exception as err:
            self.mostrar_error("Error inesperado.\n" + str(err))

    def validar(self):
        errores = []

        if not self.salario.text.isnumeric():
            errores.append("- El salario por hora debe ser un número entero, sin puntos ni comas.\n  Ejemplo: 15000")
    
        if not self.dias.text.isnumeric():
            errores.append("- Los días trabajados deben ser un número entero.\n  Ejemplo: 15")
    
        if not self.vacaciones.text.isnumeric():
            errores.append("- Las vacaciones pendientes deben ser un número entero.\n  Ejemplo: 5")
    
        if self.aplica.text not in ("0", "1"):
            errores.append("- El campo de indemnización debe ser 0 o 1.")
    
        if not self.indemnizacion.text.isnumeric():
            errores.append("- El valor de indemnización debe ser un número entero, sin puntos ni comas.\n  Ejemplo: 500000")
    
        if self.indemnizacion.text.isnumeric() and self.aplica.text == "0" and int(self.indemnizacion.text) > 0:
            errores.append(
            "- Indicaste que NO aplica indemnización, pero ingresaste un monto de " + self.indemnizacion.text + ".\n"
            "  Si no aplica, deja el valor en 0.\n"
            "  Si sí aplica, cambia el campo a 1."
        )

        if errores:
            raise ValueError("\n\n".join(errores))

    def mostrar_error(self, err):
        contenido = GridLayout(cols=1)
        contenido.add_widget(Label(text=str(err)))
        cerrar = Button(text="Cerrar")
        contenido.add_widget(cerrar)
        popup = Popup(title="Error", content=contenido)
        cerrar.bind(on_press=popup.dismiss)
        popup.open()


if __name__ == "__main__":
    LiquidacionApp().run()