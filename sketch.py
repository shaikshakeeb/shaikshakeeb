from tkinter import *
from tkinter import Tk,ttk

from PIL import Image, ImageTk
from tkinter import filedialog as fd

import cv2

def selfie():
    key = cv2. waitKey(-15)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
             
            check, frame = webcam.read() 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                #img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                
                #print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                #print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                #print("Image saved!")
                break
            
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            #print("Turning off camera.")
            webcam.release()
            #print("Camera off.")
            #print("Program ended.")
            cv2.destroyAllWindows()
            break
    sketch()
        

def sketch():
    main_window.destroy()
    window = Tk()
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

        cv2.imwrite('saved_img.png',img_to_pencil)

        img = Image.open('saved_img.png')
        img = img.resize((350,340))
        img  = ImageTk.PhotoImage(img)

        l_img = Label(window, image = img,bg=co0, fg=co1)
        l_img.place(x=99, y=78)

    style = ttk.Style(window)
    style.theme_use("clam")

    app_img = Image.open("logo.png")
    app_img = app_img.resize((50, 50))
    app_img = ImageTk.PhotoImage(app_img)

    app_logo = Label(window, image=app_img, text="ATTACK ON SKETCH NOTE",width=500,compound=LEFT,relief=RAISED,anchor=NW,font=('system 15 bold'),bg = co0, fg = co1)
    app_logo.place(x=0, y=0)

    l_options = Label(window,text = "----------------------------settings------------------------------".upper(), anchor=NW, font=('Verdana 10 bold'),bg=co0, fg=co1)
    l_options.place(x=10, y=460)

    scale = Scale(window,from_=0, to=255, length = 300, bg=co0, fg='red', orient=HORIZONTAL)
    scale.place(x=20, y=500)

    b_choose= Button(window, text = "Choose img",command = choose_img, width=15,overrelief=RIDGE,font=('Ivy 10'),bg=co2,fg=co1)
    b_choose.place(x=347,y=487)
    
    b_save= Button(window, text = "Save img",command = convert_img,width=15,overrelief=RIDGE,font=('Ivy 10'),bg=co2,fg=co1)
    b_save.place(x=347,y=517)

    window.mainloop()


#colors
co0 = "#ffffff"
co1 = "#000000" 
co2 = "#63b9ff"

main_window = Tk()
main_window.geometry('1000x1000')


canvas = Canvas(main_window, width=1000, height= 1000)
background_image = PhotoImage(width=1000,height=1000,file='bg.png')
canvas.pack(fill= BOTH, expand= True)
canvas.create_image(5,5,anchor=NW,image=background_image)
canvas.pack()
canvas.create_oval(140,270,350,410,fill='tan')
canvas.create_oval(635,270,845,410,fill='tan')

selfie_button = Button(main_window, text= "Selfie", command= selfie, height=3, width=10, font=('Consolas',15),bg='tan',fg="black",borderwidth=0)
selfie_button.place(x= 180, y = 300)
sketch_button = Button(main_window, text= "Sketch", command= sketch, height=3, width=10, font=('Consolas',15),bg='tan',fg='black',borderwidth=0)
sketch_button.place(x= 680, y = 300)
main_window.mainloop()