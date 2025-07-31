from tkinter import *
from PIL import Image, ImageTk
import requests
from pygame.examples.aliens import load_image
from to import BytestIO

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

