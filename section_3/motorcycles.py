motorcycles = ['honda', 'yamaha', 'delete me','suzuki', ]
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('Italika')

motorcycles.insert(0, "Another HONDA")
print(motorcycles)

del motorcycles[4]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(f"Popped value: {popped_motorcycle}")

print(motorcycles)
motorcycles.remove('delete me')
print(motorcycles)


print(f"\nunsort motorcycles {motorcycles}")
motorcycles.sort()
print(f"Sorted motorcycles: {motorcycles}")
motorcycles.sort(reverse=True)
print(f"Reverse Sorted motorcycles: {motorcycles}")
