import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
from scipy.signal import butter, filtfilt

def whiten(strain, interp_psd, dt):
    Nt = len(strain)
    freqs = np.fft.rfftfreq(Nt, dt)
    freqs1 = np.linspace(0, 2048, Nt // 2 + 1)

    # whitening: transform to freq domain, divide by asd, then transform back, 
    # taking care to get normalization right.
    hf = np.fft.rfft(strain)
    norm = 1./np.sqrt(1./(dt*2))
    white_hf = hf / np.sqrt(interp_psd(freqs)) * norm
    white_ht = np.fft.irfft(white_hf, n=Nt)
    return white_ht

def write_wavfile(filename, fs, data):
    d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
    wavfile.write(filename, int(fs), d)

def reqshift(data, fshift=100, sample_rate=4096):
    """Frequency shift the signal by constant"""
    x = np.fft.rfft(data)
    T = len(data)/float(sample_rate)
    df = 1.0/T
    nbins = int(fshift/df)
    y = np.roll(x.real, nbins) + 1j*np.roll(x.imag, nbins)
    y[0:nbins] = 0.
    z = np.fft.irfft(y)
    return z

def plot_psd(freqs, Pxx_H1, Pxx_L1, Pxx, eventname, f_min=20., f_max=2000.):
    """
    Plot the ASDs for H1 and L1 detectors
    """
    plt.figure(figsize=(10,8))
    plt.loglog(freqs, np.sqrt(Pxx_L1), 'g', label='L1 strain')
    plt.loglog(freqs, np.sqrt(Pxx_H1), 'r', label='H1 strain')
    plt.loglog(freqs, np.sqrt(Pxx), 'k', label='H1 strain, O1 smooth model')
    plt.axis([f_min, f_max, 1e-24, 1e-19])
    plt.grid('on')
    plt.ylabel('ASD (strain/rtHz)')
    plt.xlabel('Freq (Hz)')
    plt.legend(loc='upper center')
    plt.title('Advanced LIGO strain data near ' + eventname)
    plt.show()