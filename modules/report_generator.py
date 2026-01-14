import os

import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self):
        pass

    def generate_weekly_report(self, emotion, health_summary, output_dir="reports"):
        report = f"Weekly Report:\nEmotion Status: {emotion}\nHealth Summary: {health_summary}"
        os.makedirs(output_dir, exist_ok=True)
        chart_path = os.path.join(output_dir, "weekly_report.png")
        # Create a chart
        categories = list(health_summary.keys())
        values = list(health_summary.values())
        plt.bar(categories, values, color='skyblue')
        plt.title("Weekly Health Summary")
        plt.savefig(chart_path)
        plt.close()
        print(f"Report saved as {chart_path}")
        return report, chart_path
