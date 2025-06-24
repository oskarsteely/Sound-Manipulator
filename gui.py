import tkinter as tk
from tkinter import filedialog as fd
import sounddevice as sd
import scipy.io.wavfile as wav

class MainWINDOW:

    def __init__(self):
        self.filename = ""

        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.openButton = tk.Button(self.root, text="Open audio file", font=('Arial', 18), command=self.openFile)
        self.openButton.pack(padx=10, pady=10)

        self.filenameLabel = tk.Label(self.root, text="choose file", font=('Arial', 14))
        self.filenameLabel.pack(padx=10, pady=10)

        self.playButton = tk.Button(self.root, text="Play audio", font=('Arial', 18), command=self.play)
        self.playButton.pack(padx=10, pady=10)

        self.stopButton = tk.Button(self.root, text="Stop audio", font=('Arial', 18), command=sd.stop)
        self.stopButton.pack(padx=10, pady=10)

        self.root.mainloop()

    def openFile(self):
        filetypes = (('audio files', '*.wav'), ('All files', '*.*'))
        self.filename = fd.askopenfilename(title = 'Open an audio file', initialdir='/', filetypes=filetypes)
        print(self.filename)

    def play(self):
        if not self.filename:
            tk.messagebox.showwarning(title="Warning", message="Choose file first!")
        else:
            sample_rate, sound = wav.read(self.filename)
            sd.play(sound, samplerate=sample_rate)

MainWINDOW()

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