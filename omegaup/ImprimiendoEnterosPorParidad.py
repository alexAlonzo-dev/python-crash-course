import sys

def _main() -> None:
    N = sys.stdin.readline()
    
    linea2 = sys.stdin.readline().split()
    arr = [int(x) for x in linea2]

    p = int(sys.stdin.readline().strip()[0])

    resultados = []
    for i in arr:
        if i % 2 == p:
            resultados.append(str(i))

    print(" ".join(resultados))

if __name__ == '__main__':
    _main()