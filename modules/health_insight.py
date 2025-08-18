class HealthInsightEngine:
    def __init__(self):
        # Preloaded sample health data
        self.health_data = [
            {"sleep_hours": 6, "heart_rate": 80, "steps": 3000},
            {"sleep_hours": 7, "heart_rate": 78, "steps": 5000},
            {"sleep_hours": 5, "heart_rate": 85, "steps": 2500},
        ]

    def analyze_health(self):
        sleep_avg = sum(d["sleep_hours"] for d in self.health_data) / len(self.health_data)
        heart_avg = sum(d["heart_rate"] for d in self.health_data) / len(self.health_data)
        steps_avg = sum(d["steps"] for d in self.health_data) / len(self.health_data)
        summary = {"sleep_avg": sleep_avg, "heart_rate_avg": heart_avg, "activity_avg": steps_avg}
        print(f"Health Summary: {summary}")
        return summary
