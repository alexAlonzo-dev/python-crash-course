cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')
print("\nIs car.lower() == 'SUBARU'? I predict False.")
print(car.lower() == 'SUBARU')

age = 18
print("\nIs age == 18? I predict True.")
print(age == 18)
print("\nIs age != 18? I predict False.")
print(age != 18)
print("\nIs age > 10? I predict True.")
print(age > 10)
print("\nIs age < 10? I predict False.")
print(age < 10)
print("\nIs age >= 18? I predict True.")
print(age >= 18)
print("\nIs age <= 17? I predict False.")
print(age <= 17)

age_0 = 22
age_1 = 18
print("\nIs age_0 >= 21 and age_1 >= 21? I predict False.")
print(age_0 >= 21 and age_1 >= 21)
age_1 = 22
print("\nIs age_0 >= 21 and age_1 >= 21? I predict True.")
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print("\nIs age_0 >= 21 or age_1 >= 21? I predict True.")
print(age_0 >= 21 or age_1 >= 21)
age_0 = 18
print("\nIs age_0 >= 21 or age_1 >= 21? I predict False.")
print(age_0 >= 21 or age_1 >= 21)

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("\nIs 'mushrooms' in requested_toppings? I predict True.")
print('mushrooms' in requested_toppings)
print("\nIs 'pepperoni' in requested_toppings? I predict False.")
print('pepperoni' in requested_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print("\nIs user not in banned_users? I predict True.")
print(user not in banned_users)

game_active = True
can_edit = False
print("\nBoolean game_active:")
print(game_active)
print("Boolean can_edit:")
print(can_edit)

car = 'Honda'
print("\nString equality test (False):")
print(car == 'honda')
print("String inequality test (True):")
print(car != 'toyota')
print("Using lower() equality (True):")
print(car.lower() == 'honda')
print("Using lower() inequality (False):")
print(car.lower() == 'toyota')

x = 10
y = 20
print("\nNumerical equality (False):")
print(x == y)
print("Numerical inequality (True):")
print(x != y)
print("Greater than (False):")
print(x > y)
print("Less than (True):")
print(x < y)
print("Greater or equal (False):")
print(x >= y)
print("Less or equal (True):")
print(x <= y)

print("\nand test (True):")
print(x < y and y > 5)
print("and test (False):")
print(x > y and y > 5)
print("or test (True):")
print(x < y or x > y)
print("or test (False):")
print(x == y or y < 0)

fruits = ['apple', 'banana', 'orange']
print("\n'in' test (True):")
print('apple' in fruits)
print("'in' test (False):")
print('pear' in fruits)
print("'not in' test (True):")
print('pear' not in fruits)
print("'not in' test (False):")
print('banana' not in fruits)
