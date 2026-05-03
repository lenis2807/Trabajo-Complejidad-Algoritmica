import tkinter as tk
import customtkinter as ctk
import os
import random 
import math

#interfaz gráfica
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("Algoritmo Rsa")
app.geometry("500x500")

label_titulo = ctk.CTkLabel(app, text="CRIPTOGRAFIA", font=("Arial", 20, "bold"))
label_titulo.grid(padx=20, pady=10)


##si se piensa colocar imagenes
frame = ctk.CTkFrame(master=app,
                     width=100,
                     height=100,
                     corner_radius=10,
                     bg_color="white")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def button_event():
        print("Cargando")

##lineas de texto

# def botton_pres():
##en observacion xd 
diccionario_miniscula = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j',
                         11:'k', 12:'l', 13:'m', 14:'n', 15:'ñ', 16:'o', 17:'p', 18:'q', 19:'r', 20:'s',
                         21:'t', 22:'u', 23:'v', 24:'w', 25:'x', 26:'y', 27:'z'}

diccionario_inverso = {}

def es_primo(a):
    if a < 2: 
        return False
    numero = int(math.sqrt(a))
    for i in range(2, numero + 1):
        if a % i == 0:
            return False
    return True

def algoritmoEuclides(a, b):
    if b == 0: 
        return a
    return algoritmoEuclides(b, a % b) 

#funcion extendida de euclides
def mcd_Extendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mcd, x, y = mcd_Extendido(b%a, a)
        return mcd, y -(b//a) * x, x
    
##se decide crear una variable e aleatoria global
def generar_e(euler):
    while(1):
        e = random.randint(2, euler - 1)
        if algoritmoEuclides(e, euler) == 1:
            return e

def hallar_d(e, euler):
    mcd, x, y = mcd_Extendido(e, euler)
    if mcd != 1:
        return None
    else:
        return x % euler



# restriccion
# n * p debe ser mayor que el numero de posiciones de la tabla
# de equivalencias


##variables globales
n_mod = 0
funEuler = 0
variableD = 0
variableE = 0

def validar_nums_usuario():
    global n_mod, funEuler
    #bucle while
    p, q = 0, 0
    while(1):
        os.system("cls")
        #p = int(input(("Ingrese su primer numero primo: ")))
        p = ctk.CTkEntry(master=frame,
                            placeholder_text="Ingrese su primer numero primo",
                            width=10,
                            height=10,
                            border_width=2,
                            corner_radius=10)
        p.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        if (es_primo(p)):  
            break
        else:
            print("Ingrese un numero primo")
    
    while(1):
        os.system("cls")
        #q = int(input(("Ingrese su segundo numero primo: ")))
        q = ctk.CTkEntry(master=frame,
                            placeholder_text="Ingrese su segundo numero primo",
                            width=10,
                            height=10,
                            border_width=2,
                            corner_radius=10)
        q.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        if(es_primo(q)):
            break
        else:
            print("Ingrese un numero primo")

    n_mod = p * q
    funEuler = (p - 1)*(q - 1)
    return n_mod 
    

def clave_public(n, e):
    #print("Clave publica: ")
    menzaje_entry = ctk.CTkEntry(master=frame,
                            placeholder_text="Clave publica",
                            width=10,
                            height=10,
                            border_width=2,
                            corner_radius=10)
    menzaje_entry.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    return n, e

##se debe guardar la variable 
def cifrarTexto(cadena):
    #cifrar = M^e mod n  
    #validar_nums_usuario()
    valor_e = generar_e(funEuler)      
    arreglo_cifrado = []
    texto = ""
    for i in range(len(cadena)):
        Posicion = ord(cadena[i])
        c = (pow(Posicion, valor_e) % n_mod)
        xd = chr(c)
        texto += xd
        arreglo_cifrado.append(c)

    return arreglo_cifrado, texto 



def descifrar_texto(cadena):
    texto_descifrado = ""
    for i in range(len(cadena[i])):
        Posicion = ord(i)
        M = (pow(Posicion, variableD)) % n_mod
        texto_descifrado += M
    return texto_descifrado



entry_p = ctk.CTkEntry(master=app, placeholder_text="Primo P")
entry_p.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

entry_q = ctk.CTkEntry(master=app, placeholder_text="Primo Q")
entry_q.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

entry_mensaje = ctk.CTkEntry(master=app, placeholder_text="Ingrese su mensaje de texto")
entry_mensaje.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def buttonCifrar():
    #mensaje = input("Ingrese su mensaje a cifrar: ").lower()
    primoP = entry_p.get()
    primoQ = entry_q.get()
    if es_primo(int(primoP)) and es_primo(int(primoQ)) and primoP != primoQ:
        mensaje = entry_mensaje.get()
        
        print(cifrarTexto(mensaje))
        print(clave_public(n_mod, generar_e(funEuler)))
    else:
        print("uno de los numeros no es primo")

    

def button_function2(cadena):
    descifrar_texto(cadena)

#si fuera en consola usaria un bucle while
#-



#

button_cifrar = ctk.CTkButton(master=app, text="1. Cifrar Texto", command=buttonCifrar)
button_cifrar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button_descifrar = ctk.CTkButton(master=app, text="2. Descifrar Texto", command=button_function2)
button_descifrar.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

app.mainloop()

