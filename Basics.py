
#  while conditon
"""
1.Building car game:simulation of car game
2.if car istaretd earlier dont dtart again
3.if car i s stopped earlier don tstop again
"""
command = ""
started = False
while True:
    command=input("-->> ")
    if command == "start":
        if started:
            print("its already started")
        else:
            started=True
            print("car is started...")
    elif command == "stop":
        if  not started:
            print("its already stopped")
        else:
            started=False
            print("car is stopped...")
    elif command == "help":
        print("""
start: to start the car 
stop: to start car 
quit: to quit the game
        """)
    elif command=="quit":
        print("your game is ended...")
        break
    else:
       print("Sorry I don't Understand")



