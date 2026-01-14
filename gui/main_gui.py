import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import threading
from modules.ai_recommendation import AIRecommendation
from modules.doctor_alert import DoctorAlert
from modules.health_insight import HealthInsightEngine
from modules.medicine_alarm import MedicineAlarm
from modules.report_generator import ReportGenerator

class PHEVGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PHEV Assistant")
        self.root.geometry("1000x750")
        self.root.configure(bg="#f0f4f7")

        self.ai_module = AIRecommendation()
        self.doctor_alert = DoctorAlert()
        self.medicine_alarm = MedicineAlarm(self.root)
        self.health_insight = HealthInsightEngine()
        self.report_generator = ReportGenerator()

        header_frame = tk.Frame(root, bg="#4a90e2", height=60)
        header_frame.pack(fill="x")
        tk.Label(header_frame, text="PHEV Assistant", font=("Helvetica", 24, "bold"),
                 bg="#4a90e2", fg="white").pack(pady=10)

        input_frame = tk.LabelFrame(root, text="Enter Health Data", padx=10, pady=10,
                                    font=("Arial",12,"bold"), bg="#f0f4f7")
        input_frame.pack(padx=20, pady=10, fill="x")

        tk.Label(input_frame, text="Sleep Hours:", bg="#f0f4f7").grid(row=0, column=0, sticky="w", pady=5)
        self.sleep_var = tk.DoubleVar()
        tk.Entry(input_frame, textvariable=self.sleep_var).grid(row=0, column=1, pady=5)

        tk.Label(input_frame, text="Heart Rate:", bg="#f0f4f7").grid(row=1, column=0, sticky="w", pady=5)
        self.hr_var = tk.IntVar()
        tk.Entry(input_frame, textvariable=self.hr_var).grid(row=1, column=1, pady=5)

        tk.Label(input_frame, text="Steps Count:", bg="#f0f4f7").grid(row=2, column=0, sticky="w", pady=5)
        self.steps_var = tk.IntVar()
        tk.Entry(input_frame, textvariable=self.steps_var).grid(row=2, column=1, pady=5)

        tk.Label(input_frame, text="Systolic BP:", bg="#f0f4f7").grid(row=3, column=0, sticky="w", pady=5)
        self.bp_sys_var = tk.IntVar()
        tk.Entry(input_frame, textvariable=self.bp_sys_var).grid(row=3, column=1, pady=5)

        tk.Label(input_frame, text="Diastolic BP:", bg="#f0f4f7").grid(row=4, column=0, sticky="w", pady=5)
        self.bp_dia_var = tk.IntVar()
        tk.Entry(input_frame, textvariable=self.bp_dia_var).grid(row=4, column=1, pady=5)

        tk.Label(input_frame, text="Emotion (Happy/Sad/Neutral):", bg="#f0f4f7").grid(row=5, column=0, sticky="w", pady=5)
        self.emotion_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.emotion_var).grid(row=5, column=1, pady=5)

        tk.Label(input_frame, text="Medicine Name (Optional):", bg="#f0f4f7").grid(row=6, column=0, sticky="w", pady=5)
        self.medicine_var = tk.StringVar()
        tk.Entry(input_frame, textvariable=self.medicine_var).grid(row=6, column=1, pady=5)

        btn_frame = tk.Frame(root, bg="#f0f4f7")
        btn_frame.pack(pady=10)
        btn_config = {"width":30, "height":2, "bg":"#4a90e2", "fg":"white", "font":("Arial",12,"bold")}

        tk.Button(btn_frame, text="Get AI Suggestions", command=self.show_ai_suggestions, **btn_config).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Show Vital Signs Dashboard", command=self.show_vital_dashboard, **btn_config).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Check Doctor Alerts", command=self.show_doctor_alerts, **btn_config).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Add Daily Health Entry", command=self.add_daily_entry, **btn_config).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(btn_frame, text="Generate Weekly Report", command=self.generate_weekly_report, **btn_config).grid(row=4, column=0, padx=10, pady=10)

        self.log_status = tk.Label(root, text="No daily logs yet.", bg="#f0f4f7", fg="#555", font=("Arial", 10))
        self.log_status.pack(pady=(0, 10))

        self.auto_set_medicine_alarms()

    def auto_set_medicine_alarms(self):
        default_schedule = [
            {"name": "Paracetamol", "hour": 9, "minute": 0},
            {"name": "Vitamin C", "hour": 14, "minute": 0},
            {"name": "Antibiotic", "hour": 20, "minute": 0}
        ]
        for med in default_schedule:
            self.medicine_alarm.add_medicine(med["name"], med["hour"], med["minute"])
        threading.Thread(target=self.medicine_alarm.check_alarms_loop, daemon=True).start()

    def show_ai_suggestions(self):
        health_state = self.get_health_state()
        emotion = self.emotion_var.get() if self.emotion_var.get() else "Neutral"
        medicine = self.medicine_var.get() if self.medicine_var.get() else None

        recommendations = self.ai_module.generate_full_recommendation(health_state, emotion, medicine)
        diet = recommendations["diet"]
        meds = recommendations["medicine_alternatives"]

        messagebox.showinfo("AI Suggestions", f"Health State: {health_state}\nEmotion: {emotion}\nDiet: {diet}\nMedicine Alternatives: {meds}")

    def get_health_state(self):
        sleep = self.sleep_var.get()
        hr = self.hr_var.get()
        if sleep < 6 or hr > 100:
            return "Tired"
        elif 6 <= sleep <= 8 and 60 <= hr <= 100:
            return "Normal"
        else:
            return "Stressed"

    def show_doctor_alerts(self):
        health_state = self.get_health_state()
        bp_sys = self.bp_sys_var.get() if self.bp_sys_var.get() else 120
        bp_dia = self.bp_dia_var.get() if self.bp_dia_var.get() else 80
        pulse = self.hr_var.get() if self.hr_var.get() else 75

        alerts = self.doctor_alert.suggest_doctor_visit(health_state, bp_sys, bp_dia, pulse)
        messagebox.showinfo("Doctor Alerts", "\n".join(alerts))

    def add_daily_entry(self):
        try:
            sleep = float(self.sleep_var.get())
            heart_rate = int(self.hr_var.get())
            steps = int(self.steps_var.get())
            self.health_insight.add_entry(sleep, heart_rate, steps)
        except ValueError as exc:
            messagebox.showerror("Invalid Entry", str(exc))
            return
        total_entries = len(self.health_insight.health_data)
        self.log_status.config(text=f"Daily entry added. Total entries: {total_entries}")
        messagebox.showinfo("Entry Saved", "Daily health entry added successfully.")

    def generate_weekly_report(self):
        emotion = self.emotion_var.get() if self.emotion_var.get() else "Neutral"
        health_summary = self.health_insight.analyze_health()
        report, chart_path = self.report_generator.generate_weekly_report(emotion, health_summary)
        messagebox.showinfo("Weekly Report Ready", f"{report}\n\nChart saved to: {chart_path}")

    def show_vital_dashboard(self):
        dash_win = tk.Toplevel(self.root)
        dash_win.title("Vital Signs Dashboard")
        dash_win.geometry("600x450")

        systolic = self.bp_sys_var.get() if self.bp_sys_var.get() else 120
        diastolic = self.bp_dia_var.get() if self.bp_dia_var.get() else 80
        pulse = self.hr_var.get() if self.hr_var.get() else 75

        fig, ax = plt.subplots(figsize=(5, 4))
        ax.set_title("Vital Signs", fontsize=14)
        ax.set_ylim(0, 200)

        categories = ["Systolic BP", "Diastolic BP", "Pulse Rate"]
        values = [systolic, diastolic, pulse]
        colors = ["#4a90e2", "#50e3c2", "#f5a623"]

        bars = ax.bar(categories, values, color=colors)
        ax.set_ylabel("Measurements")
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 3, f'{height}', ha='center', fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=dash_win)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = PHEVGUI(root)
    root.mainloop()


