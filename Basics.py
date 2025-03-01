
"""
Building car game:simulation of car game
"""
command = ""
while True:
    command=input("-->> ")
    if command == "start":
        print("car is started...")
    elif command == "stop":
        print("car is stopped...")
    elif command == "help":
        print("""
        start: to start the car 
        stop: to start car 
        quit: to quit the game
        """)
    elif command=="quit":
        break
    else:
       print("Sorry I don't Understand")



