import numpy as np
import scipy.io.wavfile as wav
import scipy.signal as signal

sample_rate: int=44100

def sine_tone(
        frequency: int=440,
        duration: float=1.0,
        amplitude: float=0.1,
) -> np.ndarray:

    n_samples = int(sample_rate * duration)

    time_points = np.linspace(0, duration, n_samples, False)

    sine = np.sin(2* np.pi * frequency * time_points)

    sine *= amplitude

    return sine

def white_noise(
        duration: float=1.0,
        amplitude: float=0.1,
) -> np.ndarray:

    n_samples = int (duration * sample_rate)

    noise = np.random.uniform(-1, 1, n_samples)

    noise *= amplitude

    return noise

def am_synthesis(
        carrier_frequency: float,
        modulator_wave: np.array,
        modulation_index: float=0.5,
        amplitude: float=0.5,
) -> np.ndarray:

    total_samples = len(modulator_wave)

    time_points = np.arange(total_samples) / sample_rate

    carrier_wave = np.sin(2 * np.pi * carrier_frequency * time_points)

    am_wave = (1 + modulation_index * modulator_wave) * carrier_wave

    max_amplitude = np.max(np.abs(am_wave))
    am_wave = amplitude * (am_wave / max_amplitude)

    return am_wave

def fm_synthesis(
        carrier_frequency: float,
        modulator_wave: np.array,
        modulation_index: float=3,
        amplitude: float=0.5,
) -> np.ndarray:

    total_samples = len(modulator_wave)

    time_points = np.arange(total_samples) / sample_rate

    fm_wave = np.sin(2 * np.pi * carrier_frequency * time_points + modulation_index * modulator_wave)

    max_amplitude = np.max(np.abs(fm_wave))
    fm_wave = amplitude * (fm_wave / max_amplitude)

    return fm_wave

def apply_envelope(
        sound: np.array,
        adsr:list,
) -> np.array:

    sound = sound.copy()

    attack_samples = int(adsr[0] * sample_rate)
    decay_samples = int(adsr[1] * sample_rate)
    release_samples = int(adsr[3] * sample_rate)
    sustain_samples = len(sound) - (attack_samples + decay_samples + release_samples)

    #Attack
    sound[:attack_samples] *= np.linspace(0, 1, attack_samples)

    #Decay
    sound[attack_samples:attack_samples + decay_samples] *= np.linspace(1, adsr[2], decay_samples)

    #Sustain
    sound[attack_samples + decay_samples:attack_samples + decay_samples + sustain_samples] *= adsr[2]

    #Release
    sound[attack_samples + decay_samples + sustain_samples:] *= np.linspace(adsr[2], 0, release_samples)

    return sound