from pytube import YouTube

def download_video(url, output_path='videos'):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(output_path=output_path)
    return f"{output_path}/{stream.default_filename}"
