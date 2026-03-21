# thread = a flow of execution like a seperate order of instructions
#          However each thread takes a turn running to achieve concurrency
#          GIL = (global interpreter lock)
#          allows only one thread to hold the control of python interpretur

# cpu bound = program/task spends most of its time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = prgram/task spends most of its time waiting for external events (user input , web scraping)
#            use multithreading

# import threading 
# import time

# def eat_breakfast():
#     time.sleep(3)
#     print("You eat brakfast")
    
# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffee")
    
# def study():
#     time.sleep(5)
#     print("You finish studying")
    
# x = threading.Thread(target=eat_breakfast , args= ()) #Thread used 1
# x.start()

# y = threading.Thread(target= drink_coffee , args= ()) # Thread used 2
# y.start()

# z = threading.Thread(target= study, args = ()) # Thread used 3
# z.start()
    
# # eat_breakfast()
# # drink_coffee()
# # study()


# print(threading.active_count()) # print active count of threads running in our program
# print(threading.enumerate()) # print total no of threads that are available

# daemon Multi Threading 

# a thread that runs in the background, not important for program to run 
# your program will not wait for daemon to complete before exiting
# non-daemo n threads cannot normally be killed, stay alive until task is complete

# ex :- background tasts , garbage collection , waiting for input , long running process

import threading
import time

def timer():
    print()
    count=0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for : {count} seconds")
        
x = threading.Thread(target=timer , daemon= True)
x.start()

answer = input("Do you want to exit?")