import time
import tkinter as tk
import threading
from tkinter import ttk, PhotoImage

class PorodomoTimer():

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Porodomo Timer")
        self.root.tk.call('wm','iconphoto', self.root._w, PhotoImage(file="logo.png"))

        self.s = ttk.Style()
        self.s.configure("TNotebook.tab",font=("Ubuntu",16) )
        self.s.configure("TButton",font=("Ubuntu",16) )

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both",expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)

        self.porodomo_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu",48))
        self.porodomo_timer_label.pack()

        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu",48))
        self.short_break_timer_label.pack()

        self.long_break_timer_label = ttk.Label(self.tab3, text="10:00", font=("Ubuntu",48))
        self.long_break_timer_label.pack()

        self.tabs.add(self.tab1,text="Porodomo")
        self.tabs.add(self.tab2,text="Short break")
        self.tabs.add(self.tab3,text="Long break")


        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)
        
        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0,column=0)

        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0,column=1)

        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0,column=2)


        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoros: 0", font = ("Ubuntu",16))
        self.pomodoro_counter_label.grid(row=1,column=0, columnspan=3, pady=10)

        self.pomodoros = 0
        self.skipped = False
        self.stopped = False

        self.root.mainloop()

        

    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()


    def start_timer(self):
        self.stopped = False
        self.skipped = False

        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes,seconds = divmod(full_seconds,60)
                self.porodomo_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                    self.start_timer()
                else:
                    self.tabs.select(1)
                    self.start_timer()
        elif timer_id == 2:
            full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes,seconds = divmod(full_seconds,60)
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        elif timer_id == 3:
            full_seconds = 5
            while full_seconds > 0 and not self.stopped:
                minutes,seconds = divmod(full_seconds,60)
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        else:
            print("invalid tab")



    def skip_clock(self):
        current_tab = self.tabs.index(self.tabs.select())
        if current_tab == 0:
            self.porodomo_timer_label.config(text="25:00")
        elif current_tab == 1:
            self.short_break_timer_label.config(text="05:00")
        elif current_tab == 2:
            self.long_break_timer_label.config(text="10:00")
        self.stopped = True
        self.skipped = True

    def reset_clock(self):
        self.skipped = False
        self.stopped = True
        self.pomodoros = 0
        self.porodomo_timer_label.config(text="25:00")
        self.short_break_timer_label.config(text="05:00")
        self.long_break_timer_label.config(text="10:00")
        self.pomodoro_counter_label.config(text="Pomodoros: 0")

PorodomoTimer()
