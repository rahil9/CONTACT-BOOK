from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox, Listbox
from tkinter import filedialog

details = ''
names = []
root = Tk()

root.title('Contact Book')

root.geometry('610x850')

root.configure(bg="black")

mainFont=("Arial",30,"bold")

subFont=("Arial",15,"bold")

contacts=[]

info=[]

name=""
number=0
image= StringVar()


defaultIMG="Default.png"

def createContactInfo():

 global image
 
 decrypt()
    
 contactF=Toplevel()
 
 contactF.title("contact info: %s"%(name))

 contactF.config(bg="black")
     
 print(image)

 print(name)

 print(number)

 dataImage=Image.open(str(image))

 resize=dataImage.resize((400, 400))

 imgf=ImageTk.PhotoImage(resize)
 
 l1=Label(contactF,image=imgf)

 l1.pack(pady=25)

 infoF=Frame(contactF,bg="black")

 infoF.pack()


 nameL=Label(infoF,text=str(name),font=mainFont,fg="white",bg="black")

 nameL.grid(row=0,column=0)
 
 numberL=Label(infoF,text=str(number),font=subFont,fg="white",bg="black")

 numberL.grid(row=1,column=0)

 callB=Button(infoF,text="Dial",font=subFont,fg="white",bg="dark grey",width=20,command=call)

 callB.grid(row=2,column=0)

 if(number=='ERROR'):
     contactF.destroy()

 contactF.mainloop()


 
    

def decrypt():

    global info

    global name

    global image

    global number
    
    name=str(info[0])
    image=str(info[1])
    number=str(info[2])
    
def encrypt(name,image,number):
    global info
    
    info=[name,image,number]
    return info

def writeFile(info):

    global contacts
    
    file=open("contactBook.txt","rt")

    data=str(file.read())

    value=""
    
    subset=[]

    contactsTemp=[]

    for i in range(0,len(data)):


        if data[i]!=' ' and data[i]!='~':
            value+=data[i]

        elif data[i]==' ' and data[i-1]!='~':
            subset.append(value)
            value=""
            
        elif data[i]=="~":
                contactsTemp.append(list(subset))
                subset.clear()
                
        print(subset)

        
    contacts=list(contactsTemp)
    contactsTemp.clear()

    duplicateCheck()
    

    file.close()
    
    file=open("contactBook.txt","wt")
    
    contacts.append(info)

    duplicateCheck()

    for i in range(0,len(contacts)):

        for j in range(0,3):
            file.write("%s " %str(contacts[i][j]))

        file.write("~")

    file.close()

def updateFile():
    file=open("contactBook.txt","wt")
    
    for i in range(0,len(contacts)):

        for j in range(0,3):
            file.write("%s " %str(contacts[i][j]))

        file.write("~")

    file.close()
    

def readFile(name):


    global contacts

    global info
    
    file=open("contactBook.txt","rt")

    data=str(file.read())

    value=""
    
    subset=[]

    contactsTemp=[]

    for i in range(0,len(data)):


        if data[i]!=' ' and data[i]!='~':
            value+=data[i]

        elif data[i]==' ' and data[i-1]!='~':
            subset.append(value)
            value=""
            
        elif data[i]=="~":
                contactsTemp.append(list(subset))
                subset.clear()
                
        print(subset)

        
    contacts=list(contactsTemp)
    contactsTemp.clear()

    duplicateCheck()
    
    print(len(contacts))
    print(contacts)

    for i in range(0,len(contacts)):

        if (name==contacts[i][0]):
            info=contacts[i]
            print("found")
            break
        else:
            info=["NOT FOUND",defaultIMG,"ERROR"]


    createContactInfo()      

    file.close()

def duplicateCheck():

    removeL=[]

    for i in range(0,len(contacts)):

        for j in range(i+1,len(contacts)):

            if(contacts[i][2]==contacts[j][2] and i!=j):
                removeL.append(j)

    for i in range(0,len(removeL)):
        contacts.pop(removeL[i])

    removeL.clear()
    updateFile()

def access():
    
    nam=name_text.get()
    phn=phone_number_text.get()
    photo=photo_text.get()

    for i in range(0,len(nam)):

        if (nam[i]==" " or nam[i]=="~" or nam[i]==None):
            return 0
            break

    for i in range(0,len(phn)):
        
        if (phn[i]==" " or phn[i]=="~" or phn[i]==None):
            return 0
            break
    
    for i in range(0,len(photo)):
        
        if (photo[i]==" " or photo[i]=="~" or photo[i]==None):
            return 0
            break

    return 1

def call():
    print("****************************************")
    print("calling ",name)
    print("****************************************")

def deleteContact(index):
    contacts.pop(int(index))
    updateFile()
    
def fileExsist():
    try:
        file=open("contactBook.txt","rt")
        file.read()
        file.close()
    except IOError:
        file=open("contactBook.txt","wt")
        file.close()
        

    
fileExsist()

def addContact():

    #photo_text.get()
    if(access()==1):
        writeFile(encrypt(name_text.get(),photo_text.get(),phone_number_text.get()))
    
    print(contacts)

def openContact():
    checkName()
    readFile(search_name_text.get())

def removeContact():

    for i in range(0,len(contacts)):
        if(contacts[i][0]==search_name_text.get()):
            deleteContact(i)
    

def clear():
    name_text.delete(0, END)
    phone_number_text.delete(0, END)
    photo_text.delete(0, END)


    


def exit_():
    root.destroy()


def browse():
    file = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetypes=(('JPG File', '*.jpg'), ('PNG File', '*.png'), ('All Files', '*.*')))
    photo_text.insert(0, file)
    img2 = Image.open(file)
    resize = img2.resize((400, 400))
    img_2 = ImageTk.PhotoImage(resize)
    window = Toplevel()
    window.title('Photo Window')
    window.geometry('500x500')
    window_label = Label(window)
    window_label.config(image=img_2)
    window.image = img_2
    window_label.pack()

def update(data):
    # Clear the listbox
    name_list.delete(0, END)
    # Add toppings to listbox
    for item in data:
        name_list.insert(END, item)

def checkName():
    
    typed = search_name_text.get()

    data=[]

    for i in range(0,len(contacts)):

        if(contacts[i][0].startswith(typed)):
            data.append(contacts[i][0])
    
    update(data)


contact_label = Label(root, text='Contacts', font=('Arial', 30), fg='white', bg="black")
contact_label.place(x=7, y=7)

search_name = Label(root, text='Search By Name', font=('Arial', 20, 'bold'), fg="white", bg="black")
search_name.place(x=200, y=285)

search_name_text = Entry(root, width=35, font=('Arial', 15))
search_name_text.place(x=200, y=335)

name_list = Listbox(root, width=35, font=('Arial', 15))
name_list.place(x=200, y=385)

image1 = Image.open("C:\\Users\\chait\\Downloads\\MicrosoftTeams-image.png")

resize_image = image1.resize((70, 50))
img = ImageTk.PhotoImage(resize_image)

img_label = Label(image=img)
img_label.image = img
img_label.place(x=260, y=5)

name_label = Label(root, text='Full Name', font=('Arial', 20), fg='white', bg="black")
name_label.place(x=15, y=80)

name_text = Entry(root, width=26, font=('Arial', 20), fg='white', bg="#696969", bd=5)
name_text.place(x=200, y=75)


phone_number_label = Label(root, text='Phone Number', font=('Arial', 20), fg='white', bg="black")
phone_number_label.place(x=15, y=130)

phone_number_text = Entry(root, width=26, font=('Arial', 20), fg='white', bg="#696969", bd=5)
phone_number_text.place(x=200, y=125)

photo_label = Label(root, text='Photo', font=('Arial', 20), fg='white', bg="black")
photo_label.place(x=15, y=225)

photo_text = Entry(root, width=20, font=('Arial', 20), fg='white', bg="#696969", bd=5)
photo_text.place(x=200, y=220)

browse_button = Button(root, text='Browse', bg='black', fg='#5087D1', font=('Arial', 15), command=browse)
browse_button.place(x=518, y=222)

add_button = Button(root, text='Add to Contacts', bg='black', fg='#5087D1', font=('Arial', 15), command=addContact)
add_button.place(x=15, y=285)

show_button = Button(root, text='Show Contacts', bg='black', fg='#5087D1', font=('Arial', 15), command=openContact)
show_button.place(x=15, y=335)

remove_button = Button(root, text='Remove Contact', bg='black', fg='#5087D1', font=('Arial', 15), command=removeContact)
remove_button.place(x=15, y=385)

clear_button = Button(root, text='Clear All', bg='black', fg='#5087D1', font=('Arial', 15), command=clear)
clear_button.place(x=15, y=435)

exit_button = Button(root, text='Exit Window', bg='black', fg='#5087D1', font=('Arial', 15), command=exit_)
exit_button.place(x=15, y=485)

root.mainloop()
