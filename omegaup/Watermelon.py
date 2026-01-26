import sys

def _main():
    w = int(sys.stdin.readline())
    if w > 2 and w % 2 == 0:
        print("SI")
    else:
        print("NO")

if __name__ == '__main__':
    _main()
