def suma(a, b):
    """Función que suma dos números"""
    return a + b

def resta(a, b):
    """Función que resta dos números"""
    return a - b

def multiplicar(a, b):
    """Función que multiplica dos números"""
    return a * b

def dividir(a, b):
    """Función que divide dos números, con control de error"""
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def main():
    print("Resultado suma:", suma(5, 3))
    print("Resultado resta:", resta(10, 4))
    print("Resultado multiplicación:", multiplicar(6, 7))
    print("Resultado división:", dividir(20, 5))

if __name__ == "__main__":
    main()