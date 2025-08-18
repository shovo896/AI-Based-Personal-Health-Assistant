class AlternativeMedicine:
    def __init__(self):
        self.medicine_data = {
            "paracetamol": ["Tylenol", "Crocin"],
            "ibuprofen": ["Advil", "Brufen"]
        }

    def suggest_alternatives(self, medicine_name):
        return self.medicine_data.get(medicine_name.lower(), ["No alternatives found"])
