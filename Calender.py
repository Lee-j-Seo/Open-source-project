import tkinter as tk
import calendar
from datetime import datetime

now = datetime.now()
current_year = now.year
current_month = now.month

memo_data = {}

root = tk.Tk()
root.title("Calendar")
root.configure(bg="white")

title_label = tk.Label(root, font=("Consolas", 16, "bold"), bg="white")
title_label.pack(pady=(10, 0))

calendar_frame = tk.Frame(root, bg="white")
calendar_frame.pack()

def open_memo_window(year, month, day):
    win = tk.Toplevel(root)
    win.title(f"{year}-{month}-{day}")
    win.geometry("260x180")

    tk.Label(win, text=f"{year}-{month}-{day} 메모", font=("Consolas", 12)).pack(pady=5)

    text_box = tk.Text(win, width=28, height=7)
    text_box.pack()

    key = (year, month, day)
    if key in memo_data:
        text_box.insert("1.0", memo_data[key])

    def save_memo():
        memo_data[key] = text_box.get("1.0", "end").strip()
        win.destroy()
        update_calendar(year, month)

    tk.Button(win, text="저장", command=save_memo).pack(pady=5)

def update_calendar(year, month):
    title_label.config(text=f"{calendar.month_name[month]} {year}")

    for widget in calendar_frame.winfo_children():
        widget.destroy()

    weekdays = ["Su","Mo","Tu","We","Th","Fr","Sa"]
    for col, day in enumerate(weekdays):
        color = "red" if col == 0 else ("blue" if col == 6 else "black")
        tk.Label(calendar_frame, text=day, font=("Consolas",12),
                 fg=color, bg="white", width=4).grid(row=0, column=col)

    cal = calendar.Calendar(calendar.SUNDAY)
    month_days = cal.monthdayscalendar(year, month)

    for row, week in enumerate(month_days, start=1):
        for col, day in enumerate(week):
            if day == 0:
                tk.Label(calendar_frame, text="", bg="white", width=4).grid(row=row*2-1, column=col)
                tk.Label(calendar_frame, text="", bg="white", width=4).grid(row=row*2, column=col)
                continue

            fg = "red" if col == 0 else ("blue" if col == 6 else "black")

            btn = tk.Button(
                calendar_frame,
                text=str(day),
                font=("Consolas", 12),
                fg=fg,
                bg="white",
                width=4,
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                command=lambda d=day: open_memo_window(year, month, d)
            )
            btn.grid(row=row*2-1, column=col, pady=(0, 0))

            key = (year, month, day)
            if key in memo_data and memo_data[key].strip() != "":
                tk.Label(
                    calendar_frame,
                    text="●",
                    font=("Consolas", 7),
                    fg="green",
                    bg="white"
                ).grid(row=row*2, column=col)
            else:
                tk.Label(calendar_frame, text="", bg="white").grid(row=row*2, column=col)

def prev_month():
    global current_year, current_month
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1
    update_calendar(current_year, current_month)

def next_month():
    global current_year, current_month
    current_month += 1
    if current_month == 13:
        current_month = 1
        current_year += 1
    update_calendar(current_year, current_month)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="◀ Prev", command=prev_month).pack(side="left", padx=5)
tk.Button(btn_frame, text="Next ▶", command=next_month).pack(side="left", padx=5)

update_calendar(current_year, current_month)

root.mainloop()
