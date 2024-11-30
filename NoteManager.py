import heapq
from datetime import datetime

# Структура для нотаток
class Note:
    def __init__(self, content, event_date):
        self.content = content
        self.event_date = datetime.strptime(event_date, "%d-%m-%Y")
    
    def __lt__(self, other):
        return self.event_date < other.event_date

    def __eq__(self, other):
        return self.content == other.content and self.event_date == other.event_date

# Клас для черги з пріоритетом
class NoteManager:
    def __init__(self):
        self.notes_queue = []
        self.deleted_notes = []

    def add_note(self, content, event_date):
        note = Note(content, event_date)
        if note not in self.notes_queue:
            heapq.heappush(self.notes_queue, note)
            print(f"Нотатка '{content}' додана на дату {event_date}.")
        else:
            print(f"Нотатка з назвою '{content}' на дату {event_date} вже існує.")

    def get_notes_by_date(self, event_date):
        """Отримати всі нотатки на вказану дату"""
        notes_on_date = [note for note in self.notes_queue if note.event_date.strftime('%d-%m-%Y') == event_date]
        return notes_on_date

    def delete_note_by_index(self, event_date, index):
        """Видалити нотатку по індексу з відображеного списку"""
        notes_on_date = self.get_notes_by_date(event_date)
        if 0 <= index < len(notes_on_date):
            note_to_remove = notes_on_date[index]
            self.notes_queue.remove(note_to_remove)
            heapq.heapify(self.notes_queue)  # Оновлюємо чергу
            self.deleted_notes.append(note_to_remove)
            print(f"Нотатку '{note_to_remove.content}' на дату {event_date} видалено.")
        else:
            print("Невірний індекс.")

    def edit_note_by_index(self, event_date, index, new_content):
        """Редагувати нотатку по індексу з відображеного списку"""
        notes_on_date = self.get_notes_by_date(event_date)
        if 0 <= index < len(notes_on_date):
            note_to_edit = notes_on_date[index]
            note_to_edit.content = new_content
            heapq.heapify(self.notes_queue)  # Перебудовуємо чергу після зміни змісту
            print(f"Нотатку на дату {event_date} змінено.")
        else:
            print("Невірний індекс.")

    def display_notes_on_date(self, event_date):
        """Відображає нотатки на вказану дату з нумерацією"""
        notes_on_date = self.get_notes_by_date(event_date)
        if notes_on_date:
            print(f"Нотатки на дату {event_date}:")
            for i, note in enumerate(notes_on_date):
                print(f"{i + 1}. {note.content}")
        else:
            print(f"Немає нотаток на дату {event_date}.")

    def display_notes(self):
        """Відображає всі нотатки"""
        if self.notes_queue:
            sorted_notes = sorted(self.notes_queue)
            print("Список нотаток:")
            for note in sorted_notes:
                print(f"- {note.content}, Дата події: {note.event_date.strftime('%d-%m-%Y')}")
        else:
            print("Немає нотаток для відображення.")

    def display_deleted_notes(self):
        """Відображає всі видалені нотатки"""
        if self.deleted_notes:
            print("Список видалених нотаток:")
            for note in self.deleted_notes:
                print(f"- {note.content}, Дата події: {note.event_date.strftime('%d-%m-%Y')}")
        else:
            print("Список видалених нотаток порожній.")

# Функція для створення NoteManager
def create_note_manager():
    note_manager = NoteManager()
    return note_manager

# Приклад використання меню
def main_menu():
    note_manager = create_note_manager()

    while True:
        print("\nМеню:")
        print("1. Додати нотатку")
        print("2. Видалити нотатку по даті")
        print("3. Редагувати нотатку по даті")
        print("4. Показати список нотаток")
        print("5. Показати список видалених нотаток")
        print("0. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            content = input("Введіть зміст нотатки: ")
            event_date = input("Введіть дату (формат DD-MM-YYYY): ")
            note_manager.add_note(content, event_date)

        elif choice == "2":
            event_date = input("Введіть дату нотатки для видалення (формат DD-MM-YYYY): ")
            note_manager.display_notes_on_date(event_date)
            index = int(input("Оберіть номер нотатки для видалення: ")) - 1
            note_manager.delete_note_by_index(event_date, index)

        elif choice == "3":
            event_date = input("Введіть дату нотатки для редагування (формат DD-MM-YYYY): ")
            note_manager.display_notes_on_date(event_date)
            index = int(input("Оберіть номер нотатки для редагування: ")) - 1
            new_content = input("Введіть новий зміст нотатки: ")
            note_manager.edit_note_by_index(event_date, index, new_content)

        elif choice == "4":
            note_manager.display_notes()

        elif choice == "5":
            note_manager.display_deleted_notes()

        elif choice == "0":
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
