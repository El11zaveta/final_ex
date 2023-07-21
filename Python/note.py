import json
from datetime import datetime

# Класс для представления заметки
class Note:
    def __init__(self, note_id, title, body, created_at, updated_at):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f"ID: {self.note_id}\nTitle: {self.title}\nBody: {self.body}\nCreated At: {self.created_at}\nUpdated At: {self.updated_at}"


# Класс для управления заметками
class NoteManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.notes = []
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for note_data in data:
                    note = Note(
                        note_data["note_id"],
                        note_data["title"],
                        note_data["body"],
                        note_data["created_at"],
                        note_data["updated_at"],
                    )
                    self.notes.append(note)
        except FileNotFoundError:
            print("Файл не найден. Будет создан новый файл.")

    def save_notes(self):
        data = []
        for note in self.notes:
            note_data = {
                "note_id": note.note_id,
                "title": note.title,
                "body": note.body,
                "created_at": note.created_at,
                "updated_at": note.updated_at,
            }
            data.append(note_data)

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def list_notes(self):
        for note in self.notes:
            print(note)
            print("---------------------")

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        return None

    def add_note(self, title, body):
        note_id = len(self.notes) + 1
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = created_at

        note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(note)
        self.save_notes()
        print("Заметка добавлена.")

    def edit_note(self, note_id, new_title, new_body):
        note = self.get_note_by_id(note_id)
        if note:
            note.title = new_title
            note.body = new_body
            note.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.save_notes()
            print("Заметка отредактирована.")
        else:
            print("Заметка не найдена.")

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)
            self.save_notes()
            print("Заметка удалена.")
        else:
            print("Заметка не найдена.")


# Функция для запуска консольного приложения
def run_app():
    file_path = "notes.json"  # Путь к файлу с заметками
    note_manager = NoteManager(file_path)

    while True:
        print("\n------ Меню ------")
        print("1. Вывести список заметок")
        print("2. Вывести заметку по ID")
        print("3. Добавить заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("0. Выйти из приложения")

        choice = input("Выберите действие: ")
        print("------------------")

        if choice == "1":
            note_manager.list_notes()
        elif choice == "2":
            note_id = input("Введите ID заметки: ")
            note = note_manager.get_note_by_id(note_id)
            if note:
                print(note)
            else:
                print("Заметка не найдена.")
        elif choice == "3":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_manager.add_note(title, body)
        elif choice == "4":
            note_id = input("Введите ID заметки для редактирования: ")
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note_manager.edit_note(note_id, new_title, new_body)
        elif choice == "5":
            note_id = input("Введите ID заметки для удаления: ")
            note_manager.delete_note(note_id)
        elif choice == "0":
            print("Выход из приложения.")
            break
        else:
            print("Некорректный выбор. Попробуйте ещё раз.")

run_app()
