message = ""
while message != 'exit':
    message = input("\nWrite your message or 'exit' to quit: ")
    print(message)

active = True
while active:
    message = input("\nWrite your message or 'quit' to quit: ")
    if message == 'quit':
       active = False
    else:
        print(message)