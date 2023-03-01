class Todo:
    def __init__(self, code_id: int, title: str, description: str):
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"

    pass


class TodoBook:

    def __init__(self):
        self.todos = {}

    def add_todo(self, title: str, description: str) -> int:
        generate_id = len(self.todos) + 1

        generate_todo = Todo(generate_id, title, description)

        self.todos[generate_id] = generate_todo

        object_todobook = TodoBook()

        generate_id = object_todobook.add_todo("Comprar vehiculo", "Comprar vehiculo en el concesionario")

        print(generate_id)

        print(object_todobook.todos[generate_id])

        object_todobook.add_todo("Comprar vegetales", "Comprar vegetal en el supermercado")
        object_todobook.add_todo("Hacer ejercicio", "Hacer ejercicio en el gimnasio")
        object_todobook.add_todo("Pagar impuestos", "Pagar impuesto a través del banco")
        object_todobook.todos[1].mark_completed()
        completed_todos = object_todobook.completed_todos()

        for todo in completed_todos:
            print(todo.title)

        return generate_id

    generate_todo = Todo(1, "Comprar vehiculo", "Comprar vehiculo en el concesionario")

    def pending_todos(self):

        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self):

        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self):

        tag_count = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                if tag in tag_count:
                    tag_count[tag] += 1
                else:
                    tag_count[tag] = 1

        return tag_count
