import tkinter

ventana = tkinter.Tk()
ventana.title("Calculadora")

entrada_texto = tkinter.Entry(ventana, font=("Verdana 20"))
entrada_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady=10)

#Botones
boton = tkinter.Button(ventana, text = "", width = 5, height = 2)
boton.grid(row=1,column=0)
ventana.mainloop()