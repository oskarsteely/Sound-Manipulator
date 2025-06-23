import tkinter as tk
import main as main
import sounddevice as sd

class MyGUI:

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry("500x500")

        self.playButton = tk.Button(self.root, text="Play Audio", font=('Arial', 18), command=self.play)
        self.playButton.pack(padx=10, pady=10)

        self.stopButton = tk.Button(self.root, text="Stop Audio", font=('Arial', 18), command=sd.stop)
        self.stopButton.pack(padx=10, pady=10)

        self.root.mainloop()

    def play(self):
        sample_rate, sound = main.wav_data("Kazi & Madlib - To Be Lost.wav")
        main.play(sample_rate, sound)

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