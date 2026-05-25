import sympy
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    """Sub-task 1: Calcolare una Derivata."""
    function = str(input("Inserisci funzione: "))
    variabile = str(input("Inserisci variable: "))
    derivata = sympy.diff(function, variabile)
    return derivata


pass


def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    """Sub-task 2: Calcolare un Integrale Definito."""
    function = str(input("Inserisci funzione: "))
    variabile = str(input("Inserisci variable: "))
    estremo_inf = float(input("Inserisci estremo inferiore: "))
    estremo_sup = float(input("Inserisci estremo superiore: "))
    integrale =sympy.integrate(function,(variabile, estremo_inf, estremo_sup))
    return integrale
    pass


def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""
    funzione = str(input("Inserisci funzione: "))
    variabile = str(input("Inserisci variable: "))
    punto = str(input("Inserisci punto: "))
    limite = sympy.limit(funzione, variabile, espressione, punto)
    return limite
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
