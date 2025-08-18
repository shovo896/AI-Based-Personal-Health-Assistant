# modules/ai_recommendation.py

"""
AIRecommendation Module
Provides AI-based recommendations for the PHEV Assistant, including:

1. Personalized diet suggestions based on health state and detected emotion.
2. Alternative medicine suggestions based on medicine name.
3. Integrated logic to adapt recommendations dynamically.
4. Ready for GUI integration without any external files.

Author: Ahadul Haque Shovo
Date: 2025
"""


class AIRecommendation:
    def __init__(self):

        # Preloaded diet options

        self.diet_options = {
            "Tired_Sad": ["Warm Soup", "Green Tea", "Fruits"],
            "Tired_Happy": ["Light Snacks", "Smoothies", "Nuts"],
            "Normal_Happy": ["Oats", "Vegetables", "Nuts"],
            "Normal_Neutral": ["Salads", "Whole Grains", "Fruits"],
            "Stressed_Sad": ["Herbal Tea", "Dark Chocolate", "Fruits"],
            "Other": ["Hydration", "Light Meals", "Rest"]
        }


        # Preloaded alternative medicines

        self.medicine_options = {
            "paracetamol": ["Tylenol", "Crocin", "Calpol"],
            "ibuprofen": ["Advil", "Brufen", "Motrin"],
            "amoxicillin": ["Mox", "Amoxil", "Trimox"]
        }


    # Diet Suggestions

    def suggest_diet_based_on_state(self, health_state, emotion):
        """
        Provides diet suggestions based on health state and emotion.

        Parameters:
            health_state (str): e.g., "Tired", "Normal", "Stressed"
            emotion (str): e.g., "Happy", "Sad", "Neutral"

        Returns:
            list: Recommended diet items
        """
        key = f"{health_state}_{emotion}"
        if key in self.diet_options:
            return self.diet_options[key]
        elif health_state in ["Tired", "Normal", "Stressed"]:
            # Fallback if emotion-specific key not found
            return self.diet_options.get(health_state, self.diet_options["Other"])
        else:
            return self.diet_options["Other"]


    # Alternative Medicine Suggestions

    def suggest_alternative_medicine(self, medicine_name):
        """
        Suggests alternative medicines for a given generic name.

        Parameters:
            medicine_name (str): Name of the medicine (case-insensitive)

        Returns:
            list: Alternative medicine brand names
        """
        return self.medicine_options.get(medicine_name.lower(), ["No alternatives found"])


    # Full AI Recommendation Report

    def generate_full_recommendation(self, health_state, emotion, medicine_name=None):
        """
        Generates a comprehensive AI-driven recommendation combining:
        1. Diet suggestions
        2. Optional alternative medicine suggestions

        Parameters:
            health_state (str): "Tired", "Normal", "Stressed"
            emotion (str): "Happy", "Sad", "Neutral"
            medicine_name (str, optional): Generic medicine to suggest alternatives

        Returns:
            dict: {"diet": [...], "medicine_alternatives": [...]}
        """
        recommendation = {}
        recommendation["diet"] = self.suggest_diet_based_on_state(health_state, emotion)
        if medicine_name:
            recommendation["medicine_alternatives"] = self.suggest_alternative_medicine(medicine_name)
        else:
            recommendation["medicine_alternatives"] = []
        return recommendation
