import tkinter as tk
from tkinter import messagebox
import threading
import time
from datetime import datetime

class MedicineAlarm:
    def __init__(self, root):
        self.root = root
        self.alarms = []

    def add_medicine(self, name, hour, minute):
        self.alarms.append({"name": name, "hour": hour, "minute": minute, "notified": False})

    def check_alarms_loop(self):
        while True:
            now = datetime.now()
            for alarm in self.alarms:
                if not alarm["notified"]:
                    if now.hour == alarm["hour"] and now.minute == alarm["minute"]:
                        self.show_alarm_popup(alarm["name"])
                        alarm["notified"] = True
            time.sleep(30)  # check every 30 seconds

    def show_alarm_popup(self, medicine_name):
        messagebox.showinfo("Medicine Reminder", f"It's time to take your medicine: {medicine_name}")


