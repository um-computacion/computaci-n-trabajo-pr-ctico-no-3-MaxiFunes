class NumeroDebeSerPositivo(Exception):
    """Excepción lanzada cuando se ingresa un número negativo."""
    pass

def ingrese_numero():
    entrada = input("Ingrese un número: ")