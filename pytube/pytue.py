from pytube import Playlist
p = Playlist('https://www.youtube.com/watch?v=uacyvwEpdE8&list=PLgsGpHY12wUb2UybUYCOeHa9wuo8m6Xh2')
print(f'Downloading: {p.title}')
for video in p.videos:
    video.streams .filter(progressive=True, file_extension='mp4') .order_by('resolution') .desc() .first() .download()


from pytube import Channel
p = Channel('https://www.youtube.com/@LearnEasyEnglish/videos')
print(f'Downloading: {p.channel_name}')
for video in p.videos:
    video.streams .filter(progressive=True, file_extension='mp4') .order_by('resolution') .desc() .first() .download()

from pytube import YouTube
#YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams .filter(progressive=True, file_extension='mp4') .order_by('resolution') .desc() .first() .download()
#YouTube('https://youtu.be/2lAe1cqCOXo').streams.filter(res="360p").first().download()
