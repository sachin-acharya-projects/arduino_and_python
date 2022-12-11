from tkinter import Tk, PhotoImage, colorchooser, Button

def chooseColor():
    print(colorchooser.askcolor())

root = Tk()
root.title("Color Picker for Arduino")
root.iconphoto(False, PhotoImage(file="my-logo.png"))
root.geometry("500x400")
button = Button(root, text="Choose Color", command=chooseColor).pack()
root.mainloop()