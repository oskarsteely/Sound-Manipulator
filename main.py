import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
from moviepy import VideoFileClip as vfc
import synth
import gui

sample_rate: int=44100

def main():
    gui.MyGUI

def play(sample_rate, sound):
    sd.play(sound, samplerate=sample_rate)
    sd.wait()

def wav_data(src: str):
    sample_rate, data = wav.read(src)
    return sample_rate, data

"""
def main():
    #extract_from_mp4("Kazi & Madlib - To Be Lost.mp4")

    sample_rate, sound = wav_data("D:\\oskarsteely\\assets\\sound effects\\steely watermark\\steely.wav")

    #wave = sum([sine_tone(200, 2, 0.6), sine_tone(205, 2, 0.6)])
    #sound = synth.sine_tone(200, 6)
    #sound = am_synthesis(220, sound)
    #sound = fm_synthesis(47, sound, modulation_index=3)
    #sound = synth.apply_envelope(sound, [0.5, 0.2, 0.6, 2])
    sd.play(sound, samplerate=sample_rate)
    sd.wait()

def extract_from_mp4(src: str):
    clip = vfc(src)
    audio = clip.audio
    audio.write_audiofile("Kazi & Madlib - To Be Lost.wav")

def wav_data(src: str):
    sample_rate, data = wav.read(src)

    #print(sample_rate)
    #print(data.shape)
    #print(data.dtype)

    #mono
    #if len(data.shape) == 2:
    #    data = np.mean(data, axis=1, dtype=data.dtype)

    #volume
    #data = (data * 0.2).astype(data.dtype)

    #reverse
    #data = data[::-1]

    #trim
    #start_time = 1.2
    #end_time = 1.9

    #start_sample = int(start_time * sample_rate)
    #end_sample = int(end_time * sample_rate)

    #data = data[start_sample:end_sample]

    #loop
    #data = np.tile(data, (5, 1))

    #speed
    #sample_rate = int(sample_rate * 0.5)

    #export
    #wav.write("edited_audio.wav", sample_rate, data)

    return sample_rate, data
"""
if __name__ == "__main__":
    main()