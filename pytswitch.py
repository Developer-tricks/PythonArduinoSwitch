from tkinter import *
from PIL import Image, ImageTk
import serial

ser =serial.Serial(port = 'COM7', baudrate = 9600);

root = Tk()
root.title("Python - Arduino switch")
root.geometry("190x100")

is_off = True

def switch():
    global is_off
    
    if is_off:
        button.config(image = on)
        label.config(image = lon)
        is_off = False
        ser.write(b'1')
    
    else:
        button.config(image = off)
        label.config(image = loff)
        is_off = True
        ser.write(b'0')
    
on1 = Image.open('on.png'); #ON Switch image
off1 = Image.open('off.png'); #OFF Switch image
lon1 = Image.open('lighton.png'); #ON light image
loff1 = Image.open('lightoff.png'); #OFF light image
on2 = on1.resize((100, 100))
off2 = off1.resize((100 , 100))
lon2 = lon1.resize((90, 100))
loff2 = loff1.resize((90 , 100))
on = ImageTk.PhotoImage(on2)
off = ImageTk.PhotoImage(off2)
lon = ImageTk.PhotoImage(lon2)
loff = ImageTk.PhotoImage(loff2)
label = Label(root, image = loff)
label.place(x=100, y=-1)
button = Button(root, image = off, bd =0, command =switch)
button.place(x=0, y=0)
root.mainloop()