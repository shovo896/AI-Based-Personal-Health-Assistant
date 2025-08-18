import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self):
        pass

    def generate_weekly_report(self, emotion, health_summary):
        report = f"Weekly Report:\nEmotion Status: {emotion}\nHealth Summary: {health_summary}"
        # Create a chart
        categories = list(health_summary.keys())
        values = list(health_summary.values())
        plt.bar(categories, values, color='skyblue')
        plt.title("Weekly Health Summary")
        plt.savefig("weekly_report.png")
        plt.close()
        print("Report saved as weekly_report.png")
        return report
