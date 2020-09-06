from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget can take all window
        self.pack(fill=BOTH, expand=1)

        menu=Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit",command=self.clickExitButton)
        menu.add_cascade(label="File",menu=fileMenu)


        editMenu = Menu(menu)
        editMenu.add_command(label="edit1")
        editMenu.add_command(label="edit2")
        menu.add_cascade(label="Edit",menu=editMenu)



        text1=Label(self,text="Ready set go!!",fg="red",font=("Helvetica",20))
        text1.place(x=50,y=50)
        #text1=Label(master,)

        # create button, link it to clickExitButton()
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=50, y=80)

    def clickExitButton(self):
        exit()

root = Tk()
app = Window(root)
root.wm_title("Tkinter button")
root.geometry("320x200")
root.mainloop()
