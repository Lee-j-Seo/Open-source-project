import tkinter as tk
import calendar
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month

cal = calendar.Calendar(calendar.SUNDAY)
month_days = cal.monthdayscalendar(year, month)

cell_width = 4
num_cols = 7

root = tk.Tk()
root.title("Calendar")
root.configure(bg="white")

month_name = calendar.month_name[month] + " " + str(year)
title_label = tk.Label(
    root,
    text=month_name,
    font=("Consolas", 16, "bold"),
    bg="white"
)
title_label.pack(pady=(10,0))

days_frame = tk.Frame(root, bg="white")
days_frame.pack()
weekdays = ["Su","Mo","Tu","We","Th","Fr","Sa"]
for i, day in enumerate(weekdays):
    if day == "Su":
        color = "red"
    elif day == "Sa":
        color = "blue"
    else:
        color = "black"
    lbl = tk.Label(days_frame, text=day, font=("Consolas",12), width=cell_width, fg=color, bg="white")
    lbl.pack(side="left")

for week in month_days:
    week_frame = tk.Frame(root, bg="white")
    week_frame.pack()
    for i, day in enumerate(week):
        text = str(day) if day != 0 else ""
        if i == 0:
            fg = "red"
        elif i == 6:
            fg = "blue"
        else:
            fg = "black"
        lbl = tk.Label(week_frame, text=text, font=("Consolas",12), width=cell_width, fg=fg, bg="white")
        lbl.pack(side="left")

root.update_idletasks()
root.geometry(f"{root.winfo_reqwidth()}x{root.winfo_reqheight()}")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - root.winfo_width()) // 2
y = (screen_height - root.winfo_height()) // 2
root.geometry(f"+{x}+{y}")

root.mainloop()
