from pytube import YouTube

url = 'https://www.youtube.com/watch?v=sLTvQnjEkRU'

yt = YouTube(url)
print(f'downloading: {yt.title}')
# print(yt.streams.filter(only_audio=True, abr='128kbps'))

yt.streams.filter(only_audio=True, abr='128kbps').first().download(
    filename=f'{yt.title}.mp3')
