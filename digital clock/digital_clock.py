from tkinter import *
from time import strftime
import datetime

# Create the main window
root = Tk()
root.title("Styled Digital Clock by Aman")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#1e1e2f")  # Dark background

# Time update function
def update_time():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format
    time_label.config(text=current_time)

    current_day = strftime('%A')
    current_date = strftime('%B %d, %Y')
    date_label.config(text=f"{current_day}, {current_date}")

    time_label.after(1000, update_time)

# Frame for rounded-style effect
frame = Frame(root, bg="#2e2e3f", bd=5, relief=FLAT)
frame.pack(pady=40, padx=30, fill=BOTH, expand=True)

# Time label
time_label = Label(frame, font=('Consolas', 48, 'bold'), fg="#00FFCC", bg="#2e2e3f")
time_label.pack(anchor='center', pady=(20, 0))

# Date label
date_label = Label(frame, font=('Helvetica', 18), fg="#FFE600", bg="#2e2e3f")
date_label.pack(anchor='center', pady=(10, 20))

# Run the clock
update_time()
root.mainloop()
