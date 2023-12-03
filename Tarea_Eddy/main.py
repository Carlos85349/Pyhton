from funciones import SistemaTransporteAerea
from interfaz_grafica import mostrar_interfaz_inicio_sesion

def main():
    sistema = SistemaTransporteAerea()
    mostrar_interfaz_inicio_sesion(sistema)

if __name__ == "__main__":
    main()