my_favorite_food = ['pizza', 'sushi', 'tacos', 'quesadillas', 'camarones']
luz_favorite_food = my_favorite_food[:]

print(f"My favorite food: {my_favorite_food}")
print(f"friend's favorite food: {luz_favorite_food}")

my_favorite_food.append('chilaquiles')
luz_favorite_food.append('stew')

print(f"\nMy favorite food: {my_favorite_food}")
print(f"friend's favorite food: {luz_favorite_food}")

print(f"\nFirst three items in my list are: {my_favorite_food[:3]}")
print(f"Items from the middle are: : {my_favorite_food[2:4]}")
print(f"last three itemns in the list are: : {my_favorite_food[-3:]}")