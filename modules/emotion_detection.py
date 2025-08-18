import random

class EmotionDetectionEngine:
    def __init__(self):
        # Optional: load ML models here
        self.facial_model = None
        self.voice_model = None

    def analyze_emotion(self, input_text):
        # Dummy ML fallback
        emotions = ["Happy", "Sad", "Neutral", "Stressed", "Tired"]
        emotion = random.choice(emotions)
        print(f"Detected Emotion: {emotion}")
        return emotion
