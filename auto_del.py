from os import system 
import time
def start():
    while True :
        system("rm -fr ./downloads/*")
        print("Done")
        time.sleep(600)

print("Started Cleaning ....\nby : @GGG66")
start()
