from pytube import YouTube
import pytube.exceptions as exeption
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import font


class Youtube_downloader:
    def __init__(self) -> None:
        self.main_window = tk.Tk()
        self.main_window.title("Youtube downloader")
        self.main_window.geometry('600x400+200-200')
        self.main_window.resizable(False,False)
        
        self.__URL = ''
        self.__selected_folder = ''
        self.__custom_font = font.Font(family="Arial", size=12)
        
        self.quit_button = tk.Button(self.main_window, text='Вийти', bg='#F0493E', width=10, height=2,font='Arial 10', command=self.main_window.destroy)
        self.quit_button.place(x=300,y=320)
        
        self.main_button = tk.Button(self.main_window, text='Далі',width=10, height=2,font='Arial 10')
        self.main_button.place(x=190, y=320)
        
        self.choose_what_to_download()
    
        tk.mainloop()
        
    
    def choose_what_to_download(self):

        self.main_button.config(text='Далі')
        self.main_button.place(x=190, y=320)
        self.quit_button.place(x=300,y=320)
        
        self.__temp_label = tk.Label(self.main_window, text='Виберіть що скачати', font='Arial 16')
        self.__temp_label.place(x=190, y=25)
        
        self.__listbox = tk.Listbox(self.main_window, width=15, height=10, font='Arial 12')
        self.__listbox.place(x=220,y=60)
        
        self.__listbox.insert(0, f'Відео')
        self.__listbox.insert(1, f'Плейлист')
        self.__listbox.insert(2, f'З канала')
        self.__listbox.insert(3, f'З пошука')
        
        self.__listbox.select_set(0)
        
        self.main_button.config(command=self.distribute_what_to_download)
        
        
    def distribute_what_to_download(self):
        
        self.__listbox.place_forget()
        self.__temp_label.place_forget()
        
        index = self.__listbox.curselection()[0]
        
        if index == 0:self.set_URL_to_video()
        if index == 1:self.temp_func()
        if index == 2:self.temp_func()
        if index == 3:self.temp_func()
        
    
    def temp_func(self):
        self.choose_what_to_download()
        messagebox.showinfo(';)',f'Ця функція тимчасово не доступна\nВ розробці ;) ')
        
    
    def set_URL_to_video(self):
        
        self.__temp_label.config(text='Введіть URL адрес:', font = self.__custom_font)
        self.__temp_label.place(x=10, y=50)
        
        
        self.__temp_entry = tk.Entry(self.main_window, width=45, font=self.__custom_font)
        self.__temp_entry.place(x=160,y=52)
        self.__temp_entry.insert(0,f'{self.__URL}')
        
        self.main_button.config(command=self.check_URL_entry)
        
        
    def check_URL_entry(self):
        
        self.__URL = str(self.__temp_entry.get())
        
        self.__temp_entry.place_forget()
        self.__temp_label.place_forget()
        
        if self.__URL == '':
            self.choose_what_to_download()
            messagebox.showinfo('Помилка','Ви нічого не ввели!')
        else:
            try:
                yt = YouTube(self.__URL)
                yt.streams.filter(progressive=True)
                self.select_the_download_format()
            except exeption.PytubeError:
                self.choose_what_to_download()
                messagebox.showinfo('Помилка','Ви ввели щось не те :(')
                
    
    def select_the_download_format(self):
                
        self.__temp_label.config(text='Формат', font='Arial 18')
        self.__temp_label.place(x=240, y=20)
        
        self.__listbox.delete(0, tk.END) 
        
        self.__listbox.insert(0, f'  Відео')
        self.__listbox.insert(1, f'  Аудіо')
        
        self.__listbox.select_set(0)
        
        self.__listbox.place(x=220,y=60)
        
        self.main_button.config(command=self.distribute_the_download_format)
        
        
    def distribute_the_download_format(self):
        index = self.__listbox.curselection()[0]
        
        self.main_button.config(state='disabled', text='Скачати')
        
        if index == 0:self.video_format()
        if index == 1:self.audio_format()
        
    
    def video_format(self):
    
        self.main_button.config(command=self.download_video)
        
        self.__temp_label.config(text='Виберіть якість відео', font='Arial 14')
        self.__temp_label.place(x=200, y=20)
        
        self.__listbox.delete(0, tk.END) 
        
        yt = YouTube(self.__URL)
        i = 0
        
        for el in yt.streams.filter(file_extension='mp4', progressive=True, mime_type='video/mp4'):
            weight = el.filesize_mb 
            grafic = str(el)
            temp_l = grafic.split()
            grafic = temp_l[3]
            temp_l = grafic.split('"')
            grafic = temp_l[1]
            self.__listbox.insert(i,f'{grafic} | {weight:.1f} мб')
            i+=1
        
        self.__listbox.select_set(0)
        self.__listbox.place(x=220,y=60)
        
        self.__way_button = tk.Button(self.main_window, text="Вибрати папку",width=12, height=2, command=self.choose_folder)
        self.__way_button.place(x=80, y=320)
       
        
    def choose_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.__selected_folder = folder_path
            self.main_button.config(state='normal')
            
            
    def download_video(self):

            self.__listbox.place_forget()
            self.__temp_label.place_forget()
            self.__way_button.destroy()
        
            index = self.__listbox.curselection()
            value = str(self.__listbox.get(index))
            
            choice = value.split()[0]
            
            self.main_button.place_forget()
            self.quit_button.place_forget()
            self.str_var = tk.StringVar()
            temp_lab = tk.Label(self.main_window, textvariable=self.str_var, font='Arial 20')
            temp_lab.place(x=60, y=160)
            
            self.main_window.update()
            
            yt = YouTube(self.__URL, on_progress_callback=self.on_progress)
            for el in yt.streams.filter(file_extension='mp4', progressive=True, mime_type='video/mp4',res=f'{choice}'):
                el.download(self.__selected_folder)
                
            temp_lab.destroy()
            self.choose_what_to_download()
        
    
    def audio_format(self):
        self.main_button.config(command=self.download_audio)
        
        self.__temp_label.config(text='Виберіть якість аудіо', font='Arial 14')
        self.__temp_label.place(x=200, y=20)
        
        self.__listbox.delete(0, tk.END) 
        
        yt = YouTube(self.__URL)
        i = 0
        
        for el in yt.streams.filter(only_audio=True):
            weight = el.filesize_mb 
            temp_str = str(el)
            temp_l = temp_str.split()
            mime_type = temp_l[2]
            abr = temp_l[3]
            mime_type = (mime_type.split('/')[1])[:-1]
            abr = abr.split('"')[1]
            self.__listbox.insert(i,f'{abr} | {mime_type} | {weight:.1f} мб')
            i+=1
        
        self.__listbox.select_set(0)
        self.__listbox.config(width=25)
        self.__listbox.place(x=220,y=60)
        
        self.__way_button = tk.Button(self.main_window, text="Вибрати папку",width=12, height=2, command=self.choose_folder)
        self.__way_button.place(x=80, y=320)
        
    
    def download_audio(self):
        self.__listbox.place_forget()
        self.__temp_label.place_forget()
        self.__way_button.destroy()
        
        index = self.__listbox.curselection()
        value = str(self.__listbox.get(index))
        
        abr = value.split()[0]
        mimime_type = value.split()[2]
        
        self.main_button.place_forget()
        self.quit_button.place_forget()
        self.str_var = tk.StringVar()
        temp_lab = tk.Label(self.main_window, textvariable=self.str_var, font='Arial 20')
        temp_lab.place(x=60, y=160)
        
        self.main_window.update()
        
        yt = YouTube(self.__URL, on_progress_callback=self.on_progress)
        for el in yt.streams.filter(only_audio=True, mime_type=f'audio/{mimime_type}', abr=f'{abr}'):
            el.download(self.__selected_folder)
            
        temp_lab.destroy()
        self.choose_what_to_download()
    
    
    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize        
        bytes_downloaded = total_size - bytes_remaining
        percentage = (bytes_downloaded / total_size) * 100
        self.str_var.set(f'Завантаження... {percentage:.2f}% завершено')
        self.main_window.update()

        

if __name__=='__main__':
    a = Youtube_downloader()