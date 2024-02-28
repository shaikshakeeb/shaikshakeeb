from tkinter import *
from tkinter import Tk,ttk

from PIL import Image, ImageTk
from tkinter import filedialog as fd

import cv2

#colors
co0 = "#ffffff"
co1 = "#000000" 
co2 = "#63b9ff"

window = Tk()
window.title(" ")
window.geometry('500x556')
window.configure(background=co0)
window.resizable(width=FALSE,height=FALSE)
window.title("PENCIL SKETCH")
icon=PhotoImage(file='ll.png')
window.iconphoto(True,icon)

global original_img, l_img, img

original_img = ['']

def choose_img():
    global original_img, l_img, img

    img = fd.askopenfilename()      
    print(img)
    original_img.append(img) 

    img = Image.open(img)
    img = img.resize((350,340))
    img  = ImageTk.PhotoImage(img)

    l_img = Label(window, image = img,bg=co0, fg=co1)
    l_img.place(x=60, y=78)
 
def convert_img():

    global original_img, l_img, img
    

    scale_value = scale.get()

    # load the choosen image
    img = cv2.imread(original_img[-1])



    #convert one colorspace to another
    converted_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blurred_img = cv2.GaussianBlur(converted_img,(25,25), 300, 300)

    img_to_pencil = cv2.divide(converted_img, blurred_img, scale = scale_value)

    cv2.imwrite(fd.asksaveasfilename(initialfile='saved_img.png',defaultextension='.png',
    
     filetypes=[("Image files","*.png")]) ,img_to_pencil)
    cv2.imshow(fd.askopenfilename(),img)
     
    img = Image.open(fd.askopenfilename())
    img = img.resize((350,340))
    img  = ImageTk.PhotoImage(img)

    l_img = Label(window, image = img,bg=co0, fg=co1)
    l_img.place(x=60, y=78)

style = ttk.Style(window)
#style.configure('window',foreground='red')
style.theme_use("clam")

app_img = Image.open("logo.png")
app_img = app_img.resize((50, 50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(window, image=app_img, text="ATTACK ON SKETCH NOTE",width=500,compound=LEFT,relief=RAISED,anchor=NW,font=('Consolas 15 bold'),bg = co0, fg = co1)
app_logo.place(x=0, y=0)

l_options = Label(window,text = "-------------------------SETTINGS---------------------------------".upper(), anchor=NW, font=('Verdana 10 bold'),bg=co0, fg=co1)
l_options.place(x=10, y=460)



scale = Scale(window,from_=0, to=255, length = 300, bg=co0, fg='red', orient=HORIZONTAL)
scale.place(x=20, y=500)


b_choose= Button(window, text = "Choose img",command = choose_img, width=15,overrelief=RIDGE,font=('Ivy 10'),bg=co2,fg=co1)
b_choose.place(x=347,y=487)
   
b_save= Button(window, text = "Save img",command = convert_img,width=15,overrelief=RIDGE,font=('Ivy 10'),bg=co2,fg=co1)
b_save.place(x=347,y=517)

window.mainloop()

