import cv2
import PyInstaller
from tkinter import *
# import turtle
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np
import math
# turtle = turtle.Screen()
global picture_location
# turtle.bgcolor("grey")
# turtle.title("Faith's Steganography")
picture_shape = 300, 300

app1 = Tk()
app1.configure(background='sky blue')
app1.title(" Faith's Decoding system")
app1.geometry('400x400')
def Encode():
    app=Toplevel(app1)
    app.configure(background='blue')
    app.title("Faith's Encoding system")
    app.geometry('600x600')
    
    def point():
        # Step 1.5

        global picture_location
        # use the tkinter filedialog library to open the file using a dialog box.
        # obtain the image of the path
        picture_location = filedialog.askopenfilename()
        # load the image using the path
        show_picture = Image.open(picture_location)
        # set the image into the GUI using the thumbnail function from tkinter
        show_picture.thumbnail(picture_shape, Image.ANTIALIAS)
        # load the image as a numpy array for efficient computation and change the type to unsigned integer
        np_show_picture = np.asarray(show_picture)
        np_show_picture = Image.fromarray(np.uint8(np_show_picture))
        Faith = ImageTk.PhotoImage(np_show_picture)
        picture = Label(app, image=Faith)
        picture .image = Faith
        picture .place(x=20, y=50)
    def set_encryption_key():
        encryption_key=28522
        success_label = Label(app, text=" Congrats! ecryption key successfully set!",
                bg='lavender', font=("Times New Roman", 12))
        success_label.place(x=50, y=180)
    def embed_data():
        # Step 2
        global picture_location
        data = txt.get(1.0, "end-1c")
        # load the image
        picture  = cv2.imread(picture_location)
        # break the image into its character level. Represent the characyers in ASCII.
        data = [format(ord(i), '08b') for i in data]
        _, width, _ = picture .shape
        # algorithm to encode the image
        PixReq = len(data) * 3

        RowReq = PixReq/width
        RowReq = math.ceil(RowReq)

        count = 0
        charCount = 0
        # Step 3
        for i in range(RowReq + 1):
            # Step 4
            while(count < width and charCount < len(data)):
                char = data[charCount]
                charCount += 1
                # Step 5
                for index_k, k in enumerate(char):
                    if((k == '1' and picture [i][count][index_k % 3] % 2 == 0) or (k == '0' and picture [i][count][index_k % 3] % 2 == 1)):
                        picture [i][count][index_k % 3] -= 1
                    if(index_k % 3 == 2):
                        count += 1
                    if(index_k == 7):
                        if(charCount*3 < PixReq and picture [i][count][2] % 2 == 1):
                            picture [i][count][2] -= 1
                        if(charCount*3 >= PixReq and picture [i][count][2] % 2 == 0):
                            picture [i][count][2] -= 1
                        count += 1
            count = 0
        # Step 6
        # Write the encrypted image into a new file
        cv2.imwrite("encrypted_image.png", picture )
        # Display the success label.
        success_label = Label(app, text=" Congratulations! Message has been embedded Successfully!",
                    bg='lavender', font=("Times New Roman", 12))
        success_label.place(x=160, y=300)

        pixels.

        # display welcome message
    success_label = Label(app, text="Hello! Welcome to an Awesome world of Steganography!", fg='black')
    success_label.place(x=150, y=10)
    # command to indicate where to type the message
    point_button = Button(app, text="Type your message here!", bg='white', fg='black')
    point_button.place(x=350, y=60)
    # button for setting encryption key
    point_label= Label(app, text="Set Encryption Key", fg='black')
    point_label.place(x=10, y=50)
    txt = Text(app, wrap=WORD, width=10)
    txt.place(x=10, y=90, height=20)
    # button for calling the function point
    point_button = Button(app, text="Choose Image", bg='white', fg='black', command=point)
    point_button.place(x=340, y=230)
    # add a text box using tkinter's Text function and place it at (340,55). The text box is of height 165pixels.

    point_button = Button(app, text="SET KEY", bg='white', fg='black', command=set_encryption_key)
    point_button.place(x=10, y=130)

    txt = Text(app, wrap=WORD, width=30)
    txt.place(x=340, y=55, height=165)
    embed_data_button = Button(app, text="Encode", bg='white', fg='black', command=embed_data)
    embed_data_button.place(x=540, y=230)


    # point_button = Button(app, text="encode", bg='white', fg='black', command=)
    # point_button.place(x=350, y=230)

            

def Decode():
    app=Toplevel(app1)
    app.configure(background='sky blue')
    app.title(" Faith's Decoding system")
    app.geometry('600x600')
    
    def decode():
    # load the image and convert it into a numpy array and display on the GUI.
        display = Image.open("encrypted_image.png")
        display.thumbnail(picture_shape, Image.ANTIALIAS)
        display = np.asarray(display)
        display = Image.fromarray(np.uint8(display))
        Faith = ImageTk.PhotoImage(display)
        picture  = Label(app, image=Faith)
        picture .image = Faith
        picture .place(x=100, y=50)

        # Algorithm to decrypt the data from the image
        picture  = cv2.imread("./encrypted_image.png")
        data = []
        stop = False
        for index_i, i in enumerate(picture ):
            i.tolist()
            for index_j, j in enumerate(i):
                if((index_j) % 3 == 2):
                    # first pixel
                    data.append(bin(j[0])[-1])
                    # second pixel
                    data.append(bin(j[1])[-1])
                    # third pixel
                    if(bin(j[2])[-1] == '1'):
                        stop = True
                        break
                else:
                    # first pixel
                    data.append(bin(j[0])[-1])
                    # second pixel
                    data.append(bin(j[1])[-1])
                    # third pixel
                    data.append(bin(j[2])[-1])
            if(stop):
                break

        message = []
        # join all the bits to form letters (ASCII Representation)
        for i in range(int((len(data)+1)/8)):
            message.append(data[i*8:(i*8+8)])
        # join all the letters to form the message.
        message = [chr(int(''.join(i), 2)) for i in message]
        message = ''.join(message)
        message_label = Label(app, text=message, bg='lavender', font=("Times New Roman", 12))
        message_label.place(x=50, y=400)
      
    def decryption_key():

        label = Label(app, text=" Decryption key correct. Proceed to Decryption",
            bg='lavender', font=("Times New Roman", 12))
        label.place(x=50, y=240)
    button = Button(app, text="KEEP SECURE!! BE AWARE OF EAVESDROPPERS!!", bg='white', fg='black')
    button.place(x=50, y=10)
    txt = Text(app, wrap=WORD, width=30)
    txt.place(x=50, y=150, height=20)
    label = Label(app, text="ENTER DECRYPTION KEY", bg='white', fg='black')
    label.place(x=50, y=100)
    button = Button(app, text=" ENTER", bg='white', fg='black', command=decryption_key, cursor="hand2")
    button.place(x=50, y=180)
# Add the button to call the function decrypt.
    main_button = Button(app, text="2. CLICK HERE TO DECODE THE MESSAGE", bg='white', fg='black', command=decode, cursor="hand2")
    main_button.place(x=350, y=300)
label=Label(app1, text="choose an option")
label.place(x=50, y=10)
btn1=Button(app1,text="Encode",command=Encode, cursor="hand2")
btn1.place(x=50, y=40)
btn2=Button(app1,text="Decode",command=Decode, cursor="hand2")
btn2.place(x=150, y=40)
app1.mainloop()