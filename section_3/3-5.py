dinner_guests = ['j. casablancas', 'a. turner', 'clairo']

cant_make_dinner = dinner_guests.pop(0)

print(f"{cant_make_dinner} CANT MAKE THE DINNER")
dinner_guests.append('chino moreno')
print(f"{dinner_guests[-1]}  is the new guest instead of {cant_make_dinner}")
print(f"They can do it {dinner_guests}")


dinner_guests.insert(0, 'g. angel')
dinner_guests.insert(2, 'tame impala')
dinner_guests.append('cartman')

print(f"these are all the guests for dinner because i hava a longer table: {dinner_guests}")