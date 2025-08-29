from tkinter import *


vocales = ['a', 'e', 'i', 'o', 'u']

def contador_vocales(palabra):
    """Cuenta las vocales en la palabra"""
    vocales_contador = 0
    for p in palabra.lower():  
        if p in vocales:
            vocales_contador += 1
    return vocales_contador

def mostrar_resultado():
    """Obtiene la palabra del campo de texto y muestra el número de vocales"""
    palabra = entry_palabra.get()
    cantidad = contador_vocales(palabra)
    resultado.config(text=f"Cantidad de vocales encontradas: {cantidad}")


ventana = Tk()
ventana.title("Contador de Vocales")
ventana.geometry("400x200")


Label(ventana, text="Ingresa una palabra:").pack(pady=10)


entry_palabra = Entry(ventana, width=30)
entry_palabra.pack(pady=5)

Button(ventana, text="Contar vocales", command=mostrar_resultado).pack(pady=10)

resultado = Label(ventana, text="")
resultado.pack(pady=10)

ventana.mainloop()
