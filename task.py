from datetime import datetime

class Task:
    def __init__(self, title, description="", due_date=None, priority="Normal", completed=False):
        self.title = title
        self.description = description
        self.due_date = due_date  # string ve formátu YYYY-MM-DD
        self.priority = priority
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "priority": self.priority,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            priority=data["priority"],
            completed=data["completed"]
        )

    @staticmethod
    def validate_date(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
