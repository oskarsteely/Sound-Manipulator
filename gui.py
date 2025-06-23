import tkinter as tk
from tkinter import messagebox
import main as main

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height= 5, font=('Arial', 16))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Message", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))

MyGUI()

"""
def main():
    root = tk.Tk()

    root.geometry("800x500")
    root.title("Sound Manipulator")

    optionsframe = tk.Frame(root)
    optionsframe.columnconfigure(0, weight=1)
    optionsframe.columnconfigure(1, weight=1)

    filechbtn = tk.Checkbutton(optionsframe, text = "Audio file", font=(18))
    filechbtn.grid(row = 0, column = 0, sticky = tk.W+tk.E)

    fileentry = tk.Entry(optionsframe)
    fileentry.grid(row = 0, column = 1, sticky = tk.W+tk.E)

    attackchbtn = tk.Checkbutton(optionsframe, text = "Attack", font=(18))
    attackchbtn.grid(row = 1, column = 0, sticky = tk.W+tk.E)

    attackentry = tk.Entry(optionsframe)
    attackentry.grid(row = 1, column = 1, sticky = tk.W+tk.E)

    optionsframe.pack()

    playbtn = tk.Button(root, text="play", height = 2, width = 7, font=(18))
    playbtn.pack(padx = 10, pady = 10)

    root.mainloop()

if __name__ == "__main__":
    main()
"""