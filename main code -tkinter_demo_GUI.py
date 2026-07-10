# Here we will create a login page.

from tkinter import *
from PIL import ImageTk , Image
from tkinter import messagebox

# Added functionality to our code. If user types wrong email or password . It will throw error
def handle_login():
    email = email_input.get()
    password = password_input.get()
    if email == 'vinaygundu249@gmail.com' and password == '1234':
        messagebox.showinfo("Congratulations" , "Login Successful")
    else :
        messagebox.showerror("Error", "Login Failed")

# GUI Coding

root = Tk()
root.title("login")
# root.iconbitmap('detective')

icon = PhotoImage(file="detective.png")   #For Detective logo for .png file
root.iconphoto(True, icon)          #For Detective logo for .png file

root.geometry('400x550')                # if you need specific size of a window popup.
#root.minsize(400 ,300)                 # min size of window
#root.maxsize(1000,800)                 # max size of window

root.configure(background= '#0096DC')    # Flipkart theme color


img = Image.open('flipkart logo.jpg')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
#  img = ImageTk.PhotoImage(Image.open('flipkart logo.jpg'))  # works if above 3 lines are commented
image_label = Label(root ,image = img)
image_label.pack(pady= (10,10))    # PIL library has pack() and grid() .
                                    # Now here we will use pack() . In calculator program we will use grid

# text_label = Label(root , text = 'Flipkart')  # gives flipkart text with white bg and black text (fg i.e foreground)
text_label = Label(root , text = 'Flipkart' , fg = 'white', bg = '#0096DC', font = ('verdana',20))
#text_label.config(font=('verdana' ,24))   # if we hadnt mentioned in the above bracket
text_label.pack()

email_label = Label(root , text = "Enter Email" , fg = 'white' , bg = '#0096DC')
email_label.configure(font = ('verdana' ,12))
email_label.pack(pady=(20,5))

#To take email input
email_input = Entry(root,width=50)
email_input.pack(ipady=6, pady = (1,15))             # ipady For height i.e y axis  , pady for padding outside

password_label = Label(root , text = "Enter Password" , fg = 'white' , bg = '#0096DC')
password_label.configure(font = ('verdana' ,12))
password_label.pack(pady=(20,5))

#To take password input
password_input = Entry(root,width=50)
password_input.pack(ipady=6, pady = (1,15))

#For Login Button
login_btn = Button(root , text = 'Login Here' , height = 2 , width=20 , command = handle_login  ) # Func added to button with "command"
login_btn.pack(pady = (10,20))
login_btn.config(font = ('verdana' , 10))

root.mainloop()


