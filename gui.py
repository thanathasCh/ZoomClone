import tkinter as tk

window = tk.Tk()
window.title('Zoom Clone Program')
window.geometry('300x200')

label_target_ip = tk.Label(window, text='Target IP:')
label_target_ip.pack()

text_target_ip = tk.Text(window, height=1)
text_target_ip.pack()

listen_btn = tk.Button(window, text='Start listening', width=50)
listen_btn.pack(anchor=tk.CENTER, expand=True)

camera_btn = tk.Button(window, text='Start camera', width=50)
camera_btn.pack(anchor=tk.CENTER, expand=True)

sharing_btn = tk.Button(window, text='Start sharing', width=50)
sharing_btn.pack(anchor=tk.CENTER, expand=True)

audio_btn = tk.Button(window, text='Start audio', width=50)
audio_btn.pack(anchor=tk.CENTER, expand=True)


def start():
    window.mainloop()
