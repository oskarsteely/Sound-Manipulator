import tkinter as tk
from tkinter import filedialog as fd
import os
import sounddevice as sd
import soundfile as sf
import numpy as np
import time

class App:

    def __init__(self):
        self.file_path = None
        self.blocksize = 1024

        self.root = tk.Tk()
        self.root.geometry("800x300")
        self.root.resizable(False, False)
        self.root.title("Sound App")

        self.openButton = tk.Button(self.root, text="Open audio file", command=self.openFile)
        self.openButton.pack(pady=10)

        self.fileLabel = tk.Label(self.root, text="Nothing to play")
        self.fileLabel.pack(pady=1)

        self.elapsedLabel = tk.Label(self.root, text="00:00")
        self.elapsedLabel.pack(pady=1)

        self.playButton = tk.Button(self.root, text="Play audio", command=self.play)
        self.playButton.pack(pady=10)

        self.pauseButton = tk.Button(self.root, text="Pause audio", command=self.pause)
        self.pauseButton.pack(pady=1)

        self.stopButton = tk.Button(self.root, text="Stop audio", command=self.stop)
        self.stopButton.pack(pady=10)

        self.root.mainloop()

    def openFile(self):
        self.file_path = fd.askopenfilename(title = 'Open an audio file', filetypes=[("WAV files", "*.wav")])

        if not self.file_path:
            return

        self.file = os.path.basename(self.file_path)
        self.fileLabel.config(text="Now playing: " + self.file)

        self.sample, self.sample_rate = sf.read(self.file_path, dtype='float32')
        self.current_sample = 0

        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=self.sample.shape[1] if self.sample.ndim > 1 else 1,
            callback=self.callback,
            blocksize=self.blocksize
        )
        self.stream.start()

        tk.messagebox.showinfo("Loaded", f"Loaded: {self.file}")

    def callback(self, outdata, frames, time_info, status):
        if not self.file_path:
            outdata.fill(0)
            return

        end_sample = self.current_sample + frames
        if end_sample >= len(self.sample):
            remaining = len(self.sample) - self.current_sample
            outdata[:remaining] = self.sample[self.current_sample:]
            outdata[remaining:] = 0
            return

        chunk = self.audio_data[self.current_sample:end_sample]
        outdata[:len(chunk)] = chunk
        self.current_sample += frames

    def play(self):
        if not self.file_path:
            tk.messagebox.showwarning(title="Warning", message="Choose file first!")
            return



        self.playing = True
        self.elapsing()

    def pause(self):
        self.playing = False

        sd.stop()

    def stop(self):
        sd.stop()
        self.playing = False
        self.elapsedLabel.config(text="00:00")
        self.elapsed = 0

    def elapsing(self):
        if not self.sample_playing:
            return
        self.elapsed = int(time.time() - self.start)
        self.elapsed_samples = int(self.elapsed * self.sample_rate)
        minutes = self.elapsed // 60
        seconds = self.elapsed % 60
        self.elapsedLabel.config(text=f"{minutes:02d}:{seconds:02d}")
        self.root.after(500, self.elapsing)

App()