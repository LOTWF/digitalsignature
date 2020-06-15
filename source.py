import numpy as np
import copy
from tkinter import filedialog,Button,messagebox,Tk,Scale,Label,HORIZONTAL
from PIL import Image,ImageTk
def preview():
    global imw
    ar=np.array(im)
    for i in range(len(ar)):
        for j in range(len(ar[0])):
            if ar[i][j][0]<int(scale.get()):
                ar[i][j][0]=0
            else:
                ar[i][j][0]=255
    im2=Image.fromarray(ar)
    imw=im2
    im3=ImageTk.PhotoImage(im2)
    panel.configure(image=im3)
    panel.image = im3

def save():
    img = imw.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            if item[0] > 150:
                newData.append((0, 0, 0, 255))
            else:
                newData.append(item)
                #print(item)


    img.putdata(newData)
    img.save(root.filename+"_digital.png","PNG")
    messagebox.showinfo("Done", "saved")
imw=[]
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("PNG files","*.PNG"),("all files","*.*")))
#root.geometry("350x200+100+50")
im = Image.open(root.filename).convert('LA')
scale = Scale(root,orient=HORIZONTAL,length=300,width=20,sliderlength=10,from_=50,to=150,tickinterval=10)
scale.pack()
scale.set(110)
img = ImageTk.PhotoImage(Image.open(root.filename))
panel = Label(root, image = img)
panel.pack(fill = "both", expand = "yes")
B = Button(text ="Preview", command = preview)
B.pack()
B2 = Button(text ="Save", command = save)
B2.pack()
root.mainloop()


