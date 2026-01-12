topping = ''
while topping != 'exit':
    topping = input("Enter your favorite pizza's topping or 'exit' to quit: " )
    if topping != 'exit':
        print(f"you'll add : {topping} to your pizza\n")
    else:
        print('...')


