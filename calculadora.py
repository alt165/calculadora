from re import I
import tkinter

ventana = tkinter.Tk()
ventana.title("Calculadora")

entrada_texto = tkinter.Entry(ventana, font=("Verdana 20"))
entrada_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady=10)

i = 0
#Funciones
def click_boton(valor):
    global i
    entrada_texto.insert(i, valor)
    i += 1

def click_borrar():
    entrada_texto.delete(0, tkinter.END)
    global i
    i = 0

def resultado():
    operacion = entrada_texto.get()
    resultado = eval(operacion)
    entrada_texto.delete(0, tkinter.END)
    entrada_texto.insert(0, resultado)
    i = 0

#Botones
#numeros
boton_1 = tkinter.Button(ventana, text = "1", width = 5, height = 2, command = lambda: click_boton(1))
boton_2 = tkinter.Button(ventana, text = "2", width = 5, height = 2, command = lambda: click_boton(2))
boton_3 = tkinter.Button(ventana, text = "3", width = 5, height = 2, command = lambda: click_boton(3))
boton_4 = tkinter.Button(ventana, text = "4", width = 5, height = 2, command = lambda: click_boton(4))
boton_5 = tkinter.Button(ventana, text = "5", width = 5, height = 2, command = lambda: click_boton(5))
boton_6 = tkinter.Button(ventana, text = "6", width = 5, height = 2, command = lambda: click_boton(6))
boton_7 = tkinter.Button(ventana, text = "7", width = 5, height = 2, command = lambda: click_boton(7))
boton_8 = tkinter.Button(ventana, text = "8", width = 5, height = 2, command = lambda: click_boton(8))
boton_9 = tkinter.Button(ventana, text = "9", width = 5, height = 2, command = lambda: click_boton(9))
boton_0 = tkinter.Button(ventana, text = "0", width = 13, height = 2, command = lambda: click_boton(0))

#Operadores
boton_borrar = tkinter.Button(ventana, text = "AC", width = 5, height = 2, command = click_borrar)
boton_punto = tkinter.Button(ventana, text = ".", width = 5, height = 2, command = lambda: click_boton("."))
boton_parentesis1 = tkinter.Button(ventana, text = "(", width = 5, height = 2, command = lambda: click_boton("("))
boton_parentesis2 = tkinter.Button(ventana, text = ")", width = 5, height = 2, command = lambda: click_boton(")"))
boton_suma = tkinter.Button(ventana, text = "+", width = 5, height = 2, command = lambda: click_boton("+"))
boton_resta = tkinter.Button(ventana, text = "-", width = 5, height = 2, command = lambda: click_boton("-"))
boton_multiplicacion = tkinter.Button(ventana, text = "*", width = 5, height = 2, command = lambda: click_boton("*"))
boton_division = tkinter.Button(ventana, text = "/", width = 5, height = 2, command = lambda: click_boton("/"))
boton_igual = tkinter.Button(ventana, text = "=", width = 5, height = 2, command = lambda: resultado())

#Interfaz
boton_borrar.grid(row = 1, column = 0,padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_division.grid(row = 1, column = 3, padx = 5, pady = 5)
boton_7.grid(row = 2, column = 0,padx = 5, pady = 5)
boton_8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton_9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_multiplicacion.grid(row = 2, column = 3, padx = 5, pady = 5)
boton_4.grid(row = 3, column = 0,padx = 5, pady = 5)
boton_5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton_6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 3, column = 3, padx = 5, pady = 5)
boton_1.grid(row = 4, column = 0,padx = 5, pady = 5)
boton_2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton_3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column = 3, padx = 5, pady = 5)

boton_0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)



ventana.mainloop()