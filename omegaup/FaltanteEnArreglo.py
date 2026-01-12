array = [1]
suma = sum(array)
n = len(array) + 1  
suma_total = n * (n + 1) // 2   
faltante = suma_total - suma
print("El número faltante es:", faltante)