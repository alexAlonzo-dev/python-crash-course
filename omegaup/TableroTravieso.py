import sys

leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

def solve():
    try:
        entrada = sys.stdin.readline().strip()
        if not entrada:
            return
    except (IOError, EOFError):
        return

    presupuesto = 0
    for char in entrada:
        presupuesto += leds[int(char)]

    salida = ""
    espacios_totales = len(entrada)


    for i in range(espacios_totales):
        espacios_restantes = espacios_totales - 1 - i
        
        for digito in range(9, -1, -1):
            costo = leds[digito]
            remanente = presupuesto - costo
            
            if (presupuesto >= costo and 
                remanente >= (espacios_restantes * 2) and 
                remanente <= (espacios_restantes * 7)):
                
                salida += str(digito)
                presupuesto -= costo
                break 
                
    print(salida)

if __name__ == '__main__':
    solve()