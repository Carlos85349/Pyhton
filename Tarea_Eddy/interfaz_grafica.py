from funciones import SistemaTransporteAerea
import tkinter as tk

def iniciar_sesion(sistema, ventana, entrada_usuario=None, entrada_contrasena=None, etiqueta_estado=None):
    def iniciar_sesion_callback():
        usuario = entrada_usuario.get()
        contrasena = entrada_contrasena.get()
        if sistema.login(usuario, contrasena):
            if usuario in ["admin", "content", "limit"]:
                print("Login exitoso.")
                ventana.destroy()
                # Llamar a la lógica del menú principal o cualquier otra acción del sistema aquí
            else:
                etiqueta_estado.config(text="Usuario no autorizado.")
        else:
            etiqueta_estado.config(text="Usuario o contraseña incorrectos.")

    if entrada_usuario is None:
        etiqueta_usuario = tk.Label(ventana, text="Usuario")
        etiqueta_usuario.pack()

        entrada_usuario = tk.Entry(ventana)
        entrada_usuario.pack()

        etiqueta_contrasena = tk.Label(ventana, text="Contraseña")
        etiqueta_contrasena.pack()

        entrada_contrasena = tk.Entry(ventana, show="*")
        entrada_contrasena.pack()

        etiqueta_estado = tk.Label(ventana, text="")
        etiqueta_estado.pack()

        boton_inicio_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion_callback)
        boton_inicio_sesion.pack()

        ventana.mainloop()
    else:
        # Si ya se proporcionaron los elementos de interfaz, usarlos directamente
        iniciar_sesion_callback()

def mostrar_interfaz_inicio_sesion():
    sistema = SistemaTransporteAerea()  # Crear una instancia de la clase SistemaTransporteAerea
    ventana = tk.Tk()
    ventana.title("Sistema de Vuelos")
    ventana.configure(bg="lightblue")  # Color de fondo para la ventana

    # Ajustar el tamaño y centrar la ventana en la pantalla
    window_width = 500
    window_height = 400
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    ventana.geometry(f'{window_width}x{window_height}+{x}+{y}')

    # Crear y configurar la etiqueta del título
    titulo = tk.Label(ventana, text="Sistema de Vuelos", font=("Arial", 24))
    titulo.pack(pady=20)  # Agregar un espacio vertical alrededor del título

    # Espacios entre usuario y el textbox
    espacio_usuario = tk.Label(ventana, text="", bg="lightblue")
    espacio_usuario.pack()

    # Crear y configurar el campo de entrada para usuario
    etiqueta_usuario = tk.Label(ventana, text="Usuario", font=("Arial", 12))
    etiqueta_usuario.pack()
    entrada_usuario = tk.Entry(ventana, font=("Arial", 14))
    entrada_usuario.pack()

    # Espacios entre contraseña y el textbox
    espacio_contrasena = tk.Label(ventana, text="", bg="lightblue")
    espacio_contrasena.pack()

    # Crear y configurar el campo de entrada para contraseña
    etiqueta_contrasena = tk.Label(ventana, text="Contraseña", font=("Arial", 12))
    etiqueta_contrasena.pack()
    entrada_contrasena = tk.Entry(ventana, show="*",
                                  font=("Arial", 14))  # Muestra asteriscos para ocultar la contraseña
    entrada_contrasena.pack()

    etiqueta_estado = tk.Label(ventana, text="")
    etiqueta_estado.pack()

    # Botón de inicio de sesión
    boton_inicio_sesion = tk.Button(ventana, text="Iniciar Sesión", font=("Arial", 12),
                                    command=lambda: iniciar_sesion(sistema, ventana, entrada_usuario,
                                                                   entrada_contrasena, etiqueta_estado))
    boton_inicio_sesion.pack(pady=20)

    ventana.mainloop()

mostrar_interfaz_inicio_sesion()