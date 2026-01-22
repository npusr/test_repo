print("Hello2, World12!")
print("Line2")
import json
from pathlib import Path

DATA_FILE = Path("todos.json")


def load_todos():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)


def list_todos(todos):
    if not todos:
        print("No todos yet 🎉")
        return

    for i, todo in enumerate(todos, start=1):
        status = "✅" if todo["done"] else "❌"
        print(f"{i}. {status} {todo['title']}")


def add_todo(todos):
    title = input("Enter todo title: ").strip()
    if not title:
        print("Todo cannot be empty.")
        return

    todos.append({"title": title, "done": False})
    print("Todo added 👍")


def complete_todo(todos):
    list_todos(todos)
    try:
        index = int(input("Which todo number is done? ")) - 1
        todos[index]["done"] = True
        print("Marked as done 🎉")
    except (ValueError, IndexError):
        print("Invalid selection.")


def main():
    todos = load_todos()

    while True:
        print("\n=== TODO APP ===")
        print("1. List todos")
        print("2. Add todo")
        print("3. Complete todo")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_todos(todos)
        elif choice == "2":
            add_todo(todos)
            save_todos(todos)
        elif choice == "3":
            complete_todo(todos)
            save_todos(todos)
        elif choice == "4":
            save_todos(todos)
            print("Bye 👋")
            break
        else:
            print("Unknown option.")


if __name__ == "__main__":
    main()