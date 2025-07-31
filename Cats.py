from idlelib.rpc import response_queue
from tkinter import *
from PIL import Image, ImageTk
import requests
from pygame.examples.aliens import load_image
from to import BytestIO

def loade_image():
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytestIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return None


window = Tk()
window.title("Cats")
window.geometry("600*400")

label = Label()
label.pack()

url = "https://cataas.com/cat"
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()

