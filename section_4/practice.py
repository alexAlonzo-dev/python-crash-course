products = ["Apple", "Pear", "Banana", "Watermelon", "Apple"]

def count_elements_in_array(array, target ):
    duplicates = 0
    for val in array:
        if val == target:
            duplicates += 1
    return duplicates

print(f"duplicates: {count_elements_in_array(products, 'Apple')}")

products.remove('Apple')
products.append('Kiwi')
products.sort()

print(products)

data = [15, 3, 8, 20, 10]
print(f"\n{data}")
data.append(12)
data.sort()
data.pop(0)
print(data)