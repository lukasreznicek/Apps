import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_816=tk.Button(root)
        GButton_816["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_816["font"] = ft
        GButton_816["fg"] = "#000000"
        GButton_816["justify"] = "center"
        GButton_816["text"] = "Button"
        GButton_816.place(x=100,y=110,width=93,height=31)
        GButton_816["command"] = self.GButton_816_command

    def GButton_816_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
