import yt_dlp

url = input("Youtube Link => ")
ydl_opts = {
    'format': 'best[height<=1080]',  # En fazla 1080p çözünürlükte
    'outtmpl': '~/Desktop/%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

