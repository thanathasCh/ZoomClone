import tkinter as tk


def init(start_listening, start_camera_steam, start_screen_sharing, start_audio_stream):
    window = tk.Tk()
    window.title('Zoom Clone Program')
    window.geometry('300x200')

    label_target_ip = tk.Label(window, text='Target IP:')
    label_target_ip.pack()

    text_target_ip = tk.Text(window, height=1)
    text_target_ip.pack()

    listen_btn = tk.Button(window, text='Start listening', width=50, command=start_listening)
    listen_btn.pack(anchor=tk.CENTER, expand=True)

    camera_btn = tk.Button(window, text='Start camera', width=50, command=start_camera_steam)
    camera_btn.pack(anchor=tk.CENTER, expand=True)

    sharing_btn = tk.Button(window, text='Start sharing', width=50, command=start_screen_sharing)
    sharing_btn.pack(anchor=tk.CENTER, expand=True)

    audio_btn = tk.Button(window, text='Start audio', width=50, command=start_audio_stream)
    audio_btn.pack(anchor=tk.CENTER, expand=True)

    window.mainloop()
