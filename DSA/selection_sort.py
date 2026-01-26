def selection_sort(arr):
    for i in range(0, len(arr)):
        min = i

        for j in range(i+1, len(arr)):
            if arr[min] < arr[j]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return arr


def selection_sort_paso_a_paso(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        print(f"\nIteración {i + 1}")
        print(f"Estado inicial: {arr}")

        for j in range(i + 1, n):
            print(f"  Comparando {arr[j]} con {arr[min_index]}")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"  → Nuevo mínimo encontrado: {arr[min_index]}")

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Intercambio → {arr}")

    return arr


#print(selection_sort([1,9,8,7,1,2,3,45,]))

selection_sort_paso_a_paso([1,9,8,7,1,2,3,45,])