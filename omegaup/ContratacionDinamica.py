import sys

def _main() -> None:
    linea1 = sys.stdin.readline().split()
    if not linea1:
        return
    n = int(linea1[0])
    k = int(linea1[1])

    linea2 = sys.stdin.readline().split()
    dias = [int(x) for x in linea2]

    resultados = []
    for i in range(n - k + 1):
        ventana = dias[i : i + k]
        resultados.append(str(max(ventana)))

    print(" ".join(resultados))

if __name__ == '__main__':
    _main()

