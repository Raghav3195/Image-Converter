import tkinter as tk
from tkinter import filedialog
from PIL import Image
import img2pdf
import os


root=tk.Tk()
canvas1=tk.Canvas(root,width=350,height=300,bg='azure3',relief='raised')
canvas1.pack()

label1=tk.Label(root,text="Image Coverter",bg='azure3')
label1.config(font=('helvetica,20'))
canvas1.create_window(180,60,window=label1)

def get():
    global im1
    import_file_path=filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browse_png = tk.Button(text="Select Image", command=get, bg="royalblue", fg="white", font=('helvetica',12,'bold'))
canvas1.create_window(180,130,window=browse_png)

def convert1():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

def convert2():
    global im1
    export_file_path = filedialog.asksaveasfilename()
    pdf_Data=img2pdf.convert(export_file_path)
    im1.save(pdf_Data) 

saveasbutton = tk.Button(text="Convert to JPG", command=convert1, bg="royalblue", fg="white", font=('helvetica',12,'bold'))
saveasbutton1 = tk.Button(text="Convert to PDF", command=convert2, bg="royalblue", fg="white", font=('helvetica',12,'bold'))
canvas1.create_window(180,170,window=saveasbutton)
canvas1.create_window(180,210,window=saveasbutton1)

root.mainloop()