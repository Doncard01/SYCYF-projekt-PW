import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
import scipy.io.wavfile

# poniżej niewykorzystany kod do czytania z pliku .wav oraz odszumiania

# odczyt sygnału z pliku .wav
sampleRate, data = scipy.io.wavfile.read('PointA.wav')
times = np.arange(len(data))/sampleRate

sampleRate2, data2 = scipy.io.wavfile.read('x_signal8.wav')
times2 = np.arange(len(data2))/sampleRate2

sampleRate3, data3 = scipy.io.wavfile.read('PointB.wav')
times3 = np.arange(len(data3))/sampleRate3

# użycie filtra dolnopasmowego z 0.005 częstotliwości Nyquista
b, a = scipy.signal.butter(3, [0.01, 0.005], 'band') #scipy.signal.butter(3, 0.01, 'lowpass')
filtered = scipy.signal.filtfilt(b, a, data)

d, c = scipy.signal.butter(3, [0.01, 0.005], 'band') #test dla 'band'
filtered2 = scipy.signal.filtfilt(d, c, data3)
# wykresy
plt.figure(figsize=(10, 4))

plt.subplot(122)
plt.plot(times2, data2)
plt.title("Sygnał X")
plt.margins(0, .05)

plt.subplot(121)
plt.plot(times, filtered)
plt.title("Przefiltrowany sygnał A")
plt.margins(0, .05)

plt.subplot(133)
plt.plot(times3, filtered2)
plt.title("Przefiltrowany sygnał B")
plt.margins(0, .05)

plt.show()