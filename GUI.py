from tkinter import *

root = Tk()
root.title("AMSZ")
root.geometry("920x650")

# Sección de encabezado. En esta sección se muestra el logo del programa y los algoritmos disponibles.
# Estos son: TRAPEZOIDAL, JORGE BOOLE, T.SIMPSON 3/8, T. SIMPSON 1/3 Y SIMPSON ABIERTO


logo = Label(root,text="LOGO",borderwidth=5,relief="groove",padx=100,pady=10).grid(row=1,column=1,padx= 20, pady= 25)

boton_trapezoidal 	= Button(root, text="TRAPEZOIDAL",padx=8,pady=11).grid(row=1,column=2)
boton_jorgeboole 	= Button(root, text="JORGE BOOLE",padx=8,pady=11).grid(row=1,column=3)
boton_tsimpson3_8 	= Button(root, text="T.SIMPSON 3/8",padx=8,pady=11).grid(row=1,column=4)
boton_tsimpson1_3 	= Button(root, text="T.SIMPSON 1/3",padx=8,pady=11).grid(row=1,column=5)
boton_tsimpsonato 	= Button(root, text="SIMPSON ABIERTO",padx=8,pady=11).grid(row=1,column=6)

# Primera sección de contenido
# Esta sección contiene: Valor de a,b y delta. En caso de implementar el método SIMPSON ABIERTO
# Se muestra en el siguiente orden n,a,b y delta.

limites = Label(root,text="a=n b=n △=n",borderwidth=5,relief="groove",padx=72.5,pady=10).grid(row=2,column=1,padx= 20, pady= 25)
funcion = Entry(root, width=50).grid(row=2,column=2,columnspan=4)
aceptar = Button(root, text="Aceptar",padx=42,pady=11).grid(row=2,column=6)

#Segunda sección de contenido
# Esta sección contiente: Calculadora de datos a entrar, tabla de iteración con datos.



root.mainloop()
