import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import librosa
import librosa.display
import sys
import os

def SongInfo(songfile):
   y, sr = librosa.load(songfile, sr=None)
   fig, ax = plt.subplots(nrows=3, sharex=True, sharey=True)
   ax[0].set(title='Monophonic')
   ax[0].label_outer()
   ay=librosa.display.waveplot(y, sr=sr, ax=ax[0])