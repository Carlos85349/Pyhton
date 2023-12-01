class SistemaTransporteAerea:
    def __init__(self):
        self.usuarios = {
            "admin": {"password": "admin", "tipo": "ADMIN"},
            "content": {"password": "content", "tipo": "CONTENT"},
            "limit": {"password": "limit", "tipo": "LIMIT"}
        }
        self.usuario_actual = None
        self.rutas = {
            "HN012": {"Origen": "San Pedro Sula", "Destino": "Roatán", "Cantidad Asiento": 8, "Precio $": 165.7,
                      "Costo Local": 1200.7},
            "HN013": {"Origen": "Comayagua", "Destino": "Roatán", "Cantidad Asiento": 16, "Precio $": 278.9,
                      "Costo Local": 4500},
            "HN016": {"Origen": "Tegucigalpa", "Destino": "San Pedro Sula", "Cantidad Asiento": 10, "Precio $": 125.8,
                      "Costo Local": 1245.69},
            "HN019": {"Origen": "Ceiba", "Destino": "Roatán", "Cantidad Asiento": 20, "Precio $": 124.9,
                      "Costo Local": 2550.54}
        }

        self.ventas = []

    def login(self, username, password):
        if username in self.usuarios and self.usuarios[username]["password"] == password:
            self.usuario_actual = self.usuarios[username]  # Asignar el diccionario completo del usuario
            return True
        return False

    def mostrar_menu_principal(self):
        print("---- MENÚ PRINCIPAL ----")
        print("1. Boletería")
        print("2. Despachar Vuelo")
        print("3. Reportes")
        print("4. Cerrar Sesión")
        print("5. Cerrar Programa")

    # Boleteria
    def menu_boleteria(self):
        print("---- BOLETERÍA ----")
        print("1. Vender Boleto")
        print("2. Cancelar Boleto")
        print("3. Regresar al Menú Principal")

        opcion_boleteria = input("Seleccione una opción: ")
        if opcion_boleteria == "1":
            self.vender_boleto()
        elif opcion_boleteria == "2":
            self.cancelar_boleto()
        elif opcion_boleteria == "3":
            return
        else:
            print("Opción no válida. Intente de nuevo.")

    def vender_boleto(self):
        numero_vuelo = input("Ingrese el número de vuelo: ")

        if numero_vuelo not in self.rutas:
            print("El número de vuelo no existe.")
            return

        ruta = self.rutas[numero_vuelo]
        print(f"Origen: {ruta['Origen']}, Destino: {ruta['Destino']}")

        if ruta["Cantidad Asiento"] <= 0:
            print("NO HAY BOLETOS, AVIÓN LISTO PARA DESPACHAR")
            return

        print(f"Asientos disponibles: {ruta['Cantidad Asiento']}")

        # Lógica para ingresar datos del pasajero
        datos_pasajero = self.ingresar_datos_pasajero(ruta)

        # Lógica para generar factura
        self.generar_factura(datos_pasajero, ruta)

        # Actualizar estadísticas
        self.actualizar_estadisticas(ruta)
        pass

    def ingresar_datos_pasajero(self, ruta):
        print("Ingrese los datos del pasajero:")
        datos_pasajero = {}

        datos_pasajero["Numero Identidad"] = input("Número de Identidad: ")
        datos_pasajero["Nombre Completo"] = input("Nombre Completo: ")
        datos_pasajero["Edad"] = int(input("Edad: "))
        datos_pasajero["Genero"] = input("Género: ")
        datos_pasajero["Fecha Salida"] = input("Fecha de Salida: ")
        datos_pasajero["Fecha Regreso"] = input("Fecha de Regreso: ")

        while True:
            print(f"Asientos disponibles para el vuelo {ruta['Numero Vuelo']}: {ruta['Cantidad Asiento']}")
            asiento_elegido = input("Elija un asiento disponible: ")

            # Verificar si el asiento está disponible
            if asiento_elegido in ruta["Asientos Disponibles"]:
                datos_pasajero["Asiento"] = asiento_elegido
                ruta["Asientos Disponibles"].remove(asiento_elegido)
                break
            else:
                print("El asiento elegido no está disponible. Por favor, elija otro.")

        return datos_pasajero

    def generar_factura(self, datos_pasajero, ruta):
        # Lógica para generar factura con los datos del pasajero y la ruta
        pass

    def actualizar_estadisticas(self, ruta):
        # Lógica para actualizar estadísticas
        pass

    def cancelar_boleto(self):
        if not self.usuario_actual or self.usuario_actual["tipo"] == "CONTENT":
            print("No tiene permisos para realizar esta acción.")
            return
        # Lógica para cancelar boletos
        pass

    # Despachar Vuelo
    def despachar_vuelo(self):
        if not self.usuario_actual or self.usuario_actual["tipo"] != "ADMIN":
            print("No tiene permisos para realizar esta acción.")
            return

    # Reportes opcion 1
    def calcular_estadisticas_generales(self):
        total_ventas = len(self.ventas)
        ingresos_totales = sum(venta["precio"] for venta in self.ventas)
        costos_totales = sum(ruta["costo"] for ruta in self.rutas.values())

        if not total_ventas:
            print("No hay ventas registradas.")
            return

        rutas_ventas = {}
        for venta in self.ventas:
            numero_vuelo = venta["numero_vuelo"]
            if numero_vuelo in rutas_ventas:
                rutas_ventas[numero_vuelo] += 1
            else:
                rutas_ventas[numero_vuelo] = 1

        if not rutas_ventas:
            print("No hay ventas registradas para ninguna ruta.")
            return

        ruta_mas_rentable = max(rutas_ventas, key=rutas_ventas.get)
        ganancia_ruta_mas_rentable = self.rutas[ruta_mas_rentable]["precio"] - self.rutas[ruta_mas_rentable]["costo"]

        print("---- ESTADÍSTICAS GENERALES ----")
        print(f"Total de ventas realizadas: {total_ventas}")
        print(f"Ingresos totales: ${ingresos_totales}")
        print(f"Costos totales: ${costos_totales}")
        print(f"Ruta más rentable: {ruta_mas_rentable} con una ganancia de ${ganancia_ruta_mas_rentable}")

    # Reportes opcion 2
    def calcular_estadisticas_por_ruta(self):
        if not self.usuario_actual:
            print("Debe iniciar sesión para acceder a los reportes.")
            return

        numero_ruta = input("Ingrese el número de ruta para ver estadísticas: ")
        if numero_ruta not in self.rutas:
            print("La ruta ingresada no existe.")
            return

        ruta = self.rutas[numero_ruta]
        ventas_ruta = [venta for venta in self.ventas if venta["numero_vuelo"] == numero_ruta]
        cantidad_boletos_vendidos = len(ventas_ruta)
        ingresos_ruta = sum(venta["precio"] for venta in ventas_ruta)
        costos_ruta = ruta["costo"] * cantidad_boletos_vendidos

        print("---- ESTADÍSTICAS POR RUTA ----")
        print(f"Número de Ruta: {numero_ruta}")
        print(f"Origen: {ruta['Origen']}, Destino: {ruta['Destino']}")
        print(f"Cantidad de boletos vendidos: {cantidad_boletos_vendidos}")
        print(f"Ingresos por esta ruta: ${ingresos_ruta}")
        print(f"Costos asociados a esta ruta: ${costos_ruta}")
        print(f"Ganancias o Pérdidas: ${ingresos_ruta - costos_ruta}")

    # Reportes opcion 3
    def listar_pasajeros_por_ruta(self):
        if not self.usuario_actual:
            print("Debe iniciar sesión para acceder a los reportes.")
            return

        numero_ruta = input("Ingrese el número de ruta para ver el listado de pasajeros: ")
        if numero_ruta not in self.rutas:
            print("La ruta ingresada no existe.")
            return

        ventas_ruta = [venta for venta in self.ventas if venta["numero_vuelo"] == numero_ruta]
        if not ventas_ruta:
            print("No hay ventas registradas para esta ruta.")
            return

        print("---- LISTADO DE PASAJEROS ----")
        for venta in ventas_ruta:
            print(
                f"Asiento: {venta['asiento']}, Nombre: {venta['nombre']}, Identidad: {venta['identidad']}, Edad: {venta['edad']}")

        print(f"Total de pasajeros: {len(ventas_ruta)}")

    # Reportes opcion 4
    def mostrar_mis_datos(self):
        print(f"Valor actual de self.usuario_actual: {self.usuario_actual}")  # Debug
        if not self.usuario_actual:
            print("Debe iniciar sesión para acceder a sus datos.")
            return

        tipo_usuario = self.usuarios.get(self.usuario_actual, {}).get("tipo")  # Accede al tipo de usuario
        print("---- MIS DATOS ----")
        print(f"Usuario: {self.usuario_actual}")
        print(f"Tipo de Usuario: {tipo_usuario}")

    # Reportes
    def reportes(self):
        if not self.usuario_actual:
            print("Debe iniciar sesión para acceder a los reportes.")
            return

        print("---- REPORTES ----")
        print("1. Estadísticas Generales")
        print("2. Estadísticas por Ruta")
        print("3. Listado de Pasajeros")
        print("4. Mis Datos")
        print("5. Regresar al Menú Principal")

        opcion_reporte = input("Seleccione una opción de reporte: ")

        if opcion_reporte == "1":
            self.calcular_estadisticas_generales()
            pass
        elif opcion_reporte == "2":
            self.calcular_estadisticas_por_ruta()
            pass
        elif opcion_reporte == "3":
            self.listar_pasajeros_por_ruta()
            pass
        elif opcion_reporte == "4":
            self.mostrar_mis_datos()
            pass
        elif opcion_reporte == "5":
            return
        else:
            print("Opción de reporte no válida.")

    def cerrar_sesion(self):
        self.usuario_actual = None

    def cerrar_programa(self):
        print("¡Hasta luego!")
        exit()

    def iniciar_sistema(self):
        while True:
            if not self.usuario_actual:
                username = input("Ingrese su username: ")
                password = input("Ingrese su password: ")
                if self.login(username, password):
                    print("Login exitoso.")
                else:
                    print("Usuario o contraseña incorrectos. Intente de nuevo.")
                    continue

            self.mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.menu_boleteria()
            elif opcion == "2":
                self.menu_despachar_vuelo()
            elif opcion == "3":
                self.menu_reportes()
            elif opcion == "4":
                self.cerrar_sesion()
            elif opcion == "5":
                self.cerrar_programa()
            else:
                print("Opción no válida. Intente de nuevo.")