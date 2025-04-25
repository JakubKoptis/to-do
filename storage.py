import json
from task import Task

class Storage:
    FILE_NAME = "tasks.json"

    @staticmethod
    def save_to_file(tasks):
        with open(Storage.FILE_NAME, "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4, ensure_ascii=False)

    @staticmethod
    def load_from_file():
        try:
            with open(Storage.FILE_NAME, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except FileNotFoundError:
            return []
