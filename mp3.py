from pytube import YouTube
from moviepy.editor import *

# YouTube video linkini girin
link = "Video Bağlantınız"

# Videoyu indirin ve ses dosyasına dönüştürün
try:
    video = YouTube(link).streams.filter(only_audio=True).first().download()
    audio = AudioFileClip(video)
except:
    print("Video indirilemedi --- ses dönüştürme hatası.")
    exit()

# Başlangıç ve bitiş saatlerini belirleyin (saniye cinsinden)
start_time = 00
end_time = 120

# Belirtilen saatler arasındaki bölümü kesin ve kaydedin
clip = audio.subclip(start_time, end_time)
clip.write_audiofile("video_ismi.mp3")

# Kullanılan geçici dosyaları silin
audio.close()
os.remove(video)
