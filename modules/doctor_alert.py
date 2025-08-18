

"""
Doctor Alert Module

Provides doctor visit suggestions based on user's vital signs and health state.
"""


class DoctorAlert:
    def __init__(self):
        pass

    def suggest_doctor_visit(self, health_state, bp_systolic, bp_diastolic, pulse):
        """
        Suggests if user should consult a doctor based on vital signs.

        Parameters:
            health_state (str): "Tired", "Normal", "Stressed"
            bp_systolic (int): Systolic blood pressure
            bp_diastolic (int): Diastolic blood pressure
            pulse (int): Pulse rate

        Returns:
            list: Doctor alerts
        """
        alerts = []

        if bp_systolic > 140 or bp_diastolic > 90:
            alerts.append("High Blood Pressure - consult a doctor")
        if pulse < 50 or pulse > 110:
            alerts.append("Abnormal Pulse - consult a doctor")
        if health_state == "Stressed":
            alerts.append("High stress levels - consider professional help")

        return alerts if alerts else ["No immediate doctor visit needed"]
