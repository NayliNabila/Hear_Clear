from django.apps import AppConfig
import librosa

class PageConfig(AppConfig):
    name = 'page'
    """file = "/home/lilyadenium/Music/music1"
    plt.clf()
    signal, sr = librosa.load(file)
    plt.figure(figsize=(20,5))
    plot.subplot(211)
    librosa.display.waveplot(signal.sr)
    plt.title('Waveform')"""