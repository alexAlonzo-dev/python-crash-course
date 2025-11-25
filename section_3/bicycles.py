bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[-1])

print(f"My first bicycle was: {bicycles[0]}")

print(f"Original bycicles: {bicycles}")
print(f"Sorted method: {sorted(bicycles)}")
print(f"Sorted reverse  method: {sorted(bicycles, reverse=True)}")

bicycles.reverse()
print(f"Bicycle reverse: {bicycles}")