class DietSuggestion:
    def __init__(self):
        self.diet_data = {
            "fever": ["Soup", "Rice", "Hydration"],
            "cold": ["Honey", "Lemon", "Warm Tea"],
            "diabetes": ["Oats", "Vegetables", "Nuts"]
        }

    def suggest_diet(self, condition):
        return self.diet_data.get(condition.lower(), ["No diet suggestions available"])
