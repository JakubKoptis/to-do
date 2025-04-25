from task import Task
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def update_task(self, index, new_task: Task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = new_task

    def list_tasks(self, show_completed=True):
        for i, task in enumerate(self.tasks):
            if not show_completed and task.completed:
                continue
            status = "✓" if task.completed else "✗"
            print(f"{i+1}. [{status}] {task.title} | {task.priority} | {task.due_date}")

    def filter_by_priority(self, priority):
        return [task for task in self.tasks if task.priority.lower() == priority.lower()]

    def filter_by_date(self, date_str):
        return [task for task in self.tasks if task.due_date == date_str]

    def sort_by_title(self):
        self.tasks.sort(key=lambda t: t.title.lower())

    def sort_by_due_date(self):
        self.tasks.sort(key=lambda t: datetime.strptime(t.due_date, "%Y-%m-%d") if t.due_date else datetime.max)
