import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.core.files.images import ImageFile
import numpy as np
from io import BytesIO
import librosa 
from django.core.files.storage import FileSystemStorage
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
import datetime
import os

def SongInfo(audioFile):
   dir_image = "./media/audioimage"
   audio, sr = librosa.load(audioFile)
    """time = np.arange(0,len(audio))/sfreq
    figure = BytesIO()
    figure.seek(0)
    lineWidth = 8000/len(audio)
    if lineWidth < 0.05:
       lineWidth = 0.05
    plt.plot(time,audio,linewidth=lineWidth)
    frame1 = plt.gca() 
    frame1.axes.get_xaxis().set_visible(False)
    frame1.axes.get_yaxis().set_visible(False)"""

   fig, ax = plt.subplots(1)
   ax.set(title='Monophonic')
   ax.label_outer()
   librosa.display.waveplot(audio, sr=sr, ax=ax)
   plt.show()
   plt.savefig(dir_image + "/imae.png")

    #plt.savefig(figure, bbox_inches='tight',format="png")
    """plt.savefig(dir_image + "/image.png")
    plt.close()
    return (
       InMemoryUploadedFile(figure,'ImageField','image','image/jpeg',sys.getsizeof(figure),None),
       str(datetime.timedelta(seconds=round(librosa.get_duration(y=audio, sr=sfreq),4)))[2:],
       sfreq/1000,
    )"""

   """def SongInfo (audioFile):
      dir_image = "./media/audioimage"
      dir_sound = "./media/songs"
      #audio_files = glob (dir_sound + "/*.wav")
      audio_files = glob (dir_sound + filetype )
      #sound =  os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/song/')
      audio, sr = librosa.load(audio_files[1])
      #time = np.arrange(0, len(audio))/sr
      fig, ax = plt.subplots(1)
      ax.set(title='Monophonic')
      ax.label_outer()
      librosa.display.waveplot(audio, sr=sr, ax=ax)
      plt.show()
      plt.savefig(dir_image + "/image.png")"""