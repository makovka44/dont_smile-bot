import speedtest
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import time

class LoadingScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Loading")
        self.master.geometry("300x100")
        self.progress_label = tk.Label(self.master, text="Speedtest in progress...")
        self.progress_label.pack(pady=20)
        self.progress_bar = ttk.Progressbar(self.master, orient="horizontal", mode="indeterminate")
        self.progress_bar.pack(pady=10)
        self.progress_bar.start(10)
    def destroy(self):
        self.progress_bar.stop()
        self.progress_bar.destroy()
        self.progress_label.destroy()
while True:
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')  # format as 'YYYY-MM-DD HH:MM:SS'
    hour = now.hour

    if hour in (6, 9, 12, 15, 18, 20, 21, 22):
        with open("speedtest.txt", "a") as f:
            root = tk.Tk()
            loading_screen = LoadingScreen(root)
            root.mainloop() 
            loading_screen.progress_label.config(text="Speedtest completed!")
            f.write(f"{formatted_date}: \n")
            st = speedtest.Speedtest()
            upload_speed = st.upload()
            download_speed = st.download() 
            f.write(f"  Download Speed: {download_speed / 1_000_000:.2f} Mbps\n")
            f.write(f"  Upload Speed: {upload_speed / 1_000_000:.2f} Mbps\n")
            loading_screen.destroy()
            root = tk.Tk()
            root.title(f"The speedtest was completed. Here are the results: \n Download: {download_speed}Mbps\n Upload {upload_speed}Mbps")
            # Set the window size
            root.geometry("300x200")

            # Create a label with the message
            label = tk.Label(root, text="It's not the right hour", font=("Arial", 16))
            label.pack(pady=50)

            # Start the main event loop
            root.mainloop()

    else: 
        root = tk.Tk()
        root.title("Not the Right Hour")
        # Set the window size
        root.geometry("300x200")

        # Create a label with the message
        label = tk.Label(root, text="It's not the right hour", font=("Arial", 16))
        label.pack(pady=50)

        # Start the main event loop
        root.mainloop()

    # sleep for an hour before checking again
    time.sleep(3600)
