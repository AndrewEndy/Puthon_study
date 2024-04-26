#test2

from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
selected_folder = ""

def choose_folder():
    global selected_folder
    folder_path = filedialog.askdirectory()
    if folder_path:
        selected_folder = folder_path
        print("Вибрана папка:", selected_folder)

# Створення вікна Tkinter
root = tk.Tk()
root.title("Вибір папки для збереження файлу")
root.geometry('500x500+200-200')
root.resizable(False,False)

# Створення кнопки для виклику діалогового вікна вибору папки
button = tk.Button(root, text="Вибрати папку", command=choose_folder)
button.place(x=10, y=10)

# Запуск головного циклу
root.mainloop()

video_url = 'https://www.youtube.com/watch?v=MunPNYumw6M'
ytb = YouTube(video_url)
for el in ytb.streams.filter(progressive=True,res='720p'):
    print(el)
    print(el.filesize_mb)
    el.download(f'{selected_folder}/')



# video_format = ytb.streams.get_highest_resolution()
# video_file = video_format.download('C:/Users/Endi/Desktop/python/Youtube_downloader/')

# print(f'Відео скачане: {video_file}')