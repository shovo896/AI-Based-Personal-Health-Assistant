import datetime

class TaskRoutineManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, time_str):
        task_time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        self.tasks.append({"task": task, "time": task_time})
        print(f"Task added: {task} at {task_time}")

    def list_tasks(self):
        return [f"{t['task']} - {t['time']}" for t in self.tasks]
