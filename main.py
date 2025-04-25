from task import Task
from todo_list import TodoList
from storage import Storage

def show_menu():
    print("\n=== To-do Aplikace ===")
    print("1. Zobrazit úkoly")
    print("2. Přidat úkol")
    print("3. Dokončit úkol")
    print("4. Odstranit úkol")
    print("5. Uložit a ukončit")
    print("6. Filtrovat podle priority")
    print("7. Filtrovat podle data")
    print("8. Třídit podle názvu")
    print("9. Třídit podle termínu")
    print("10. Upravit úkol")

def get_valid_date_input(prompt):
    while True:
        date = input(prompt)
        if date == "":
            return None
        if Task.validate_date(date):
            return date
        print("Neplatné datum. Zadej ve formátu YYYY-MM-DD.")

todo = TodoList()
todo.tasks = Storage.load_from_file()

while True:
    show_menu()
    choice = input("Zvol možnost: ")

    if choice == "1":
        todo.list_tasks()

    elif choice == "2":
        title = input("Název úkolu: ")
        desc = input("Popis: ")
        due = get_valid_date_input("Termín (YYYY-MM-DD nebo Enter pro žádný): ")
        priority = input("Priorita (Low, Normal, High): ")
        task = Task(title, desc, due, priority)
        todo.add_task(task)
        print("Úkol přidán.")

    elif choice == "3":
        todo.list_tasks()
        idx = int(input("Zadej číslo úkolu ke splnění: ")) - 1
        todo.complete_task(idx)

    elif choice == "4":
        todo.list_tasks()
        idx = int(input("Zadej číslo úkolu k odstranění: ")) - 1
        todo.remove_task(idx)

    elif choice == "5":
        Storage.save_to_file(todo.tasks)
        print("Uloženo. Konec.")
        break

    elif choice == "6":
        prio = input("Zadej prioritu (Low, Normal, High): ")
        tasks = todo.filter_by_priority(prio)
        for i, task in enumerate(tasks):
            status = "✓" if task.completed else "✗"
            print(f"{i+1}. [{status}] {task.title} | {task.priority} | {task.due_date}")

    elif choice == "7":
        date = get_valid_date_input("Zadej datum: ")
        tasks = todo.filter_by_date(date)
        for i, task in enumerate(tasks):
            status = "✓" if task.completed else "✗"
            print(f"{i+1}. [{status}] {task.title} | {task.priority} | {task.due_date}")

    elif choice == "8":
        todo.sort_by_title()
        print("Seřazeno podle názvu.")

    elif choice == "9":
        todo.sort_by_due_date()
        print("Seřazeno podle termínu.")

    elif choice == "10":
        todo.list_tasks()
        idx = int(input("Zadej číslo úkolu k úpravě: ")) - 1
        title = input("Nový název (Enter ponechá původní): ")
        desc = input("Nový popis (Enter ponechá původní): ")
        due = get_valid_date_input("Nový termín (Enter ponechá původní): ")
        priority = input("Nová priorita (Enter ponechá původní): ")

        task = todo.tasks[idx]
        if title: task.title = title
        if desc: task.description = desc
        if due: task.due_date = due
        if priority: task.priority = priority

        print("Úkol upraven.")

    else:
        print("Neplatná volba.")
