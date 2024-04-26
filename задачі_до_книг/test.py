# test
from pytube import YouTube
import pytube.exceptions as exep

URL = 'https://www.youtube.com/watch?v=Ta5-hL0pW4o'

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Завантаження... {percentage:.2f}% завершено", end='\r')

# Посилання на відео, яке ви хочете завантажити
video_url = URL

# Створення об'єкту YouTube
yt = YouTube(video_url, on_progress_callback=on_progress)

# Вибір потрібного потоку для завантаження (наприклад, перший зі списку потоків)
stream = yt.streams.first()

# Завантаження відео
stream.download()
    
    

        
             

        