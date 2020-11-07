import youtube_dl

def getResult(url: str) -> map:
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    with ydl:
        result = ydl.extract_info(url, download=False)
    return result

def isPlaylist(result: map) -> bool:
    return 'entries' in result
