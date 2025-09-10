import flet as ft

# Classe para representar uma tarefa
class Task(ft.Row):
    def __init__(self, title, status_change, delete_task):
        super().__init__()
        self.completed = False

        self.checkbox = ft.Checkbox(
            label=title,
            value=False,
            on_change=self.status_changed
        )

        self.delete_button = ft.IconButton(
            icon=ft.Icons.DELETE,
            on_click=self.delete_clicked
        )

        self.controls = [self.checkbox, self.delete_button]
        self.status_change = status_change
        self.delete_task = delete_task

    def status_changed(self, e):
        self.completed = self.checkbox.value
        if self.status_change:
            self.status_change()

    def delete_clicked(self, e):
        if self.delete_task:
            self.delete_task(self)


# App principal
class TodoApp(ft.Column):
    def __init__(self):
        super().__init__()

        self.new_task = ft.TextField(
            hint_text="O que precisa ser feito?",
            expand=True
        )

        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="todos"),
                ft.Tab(text="ativos"),
                ft.Tab(text="concluidos"),
            ],
        )

        self.items_left = ft.Text("0 item(ns) ativo(s) restante(s)")

        self.width = 600
        self.controls = [
            ft.Row(
                [ft.Text(value="Todos", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD,
                        on_click=self.add_clicked
                    ),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            self.items_left,
                            ft.OutlinedButton(
                                text="Limpar concluídos",
                                on_click=self.clear_clicked
                            ),
                        ],
                    ),
                ],
            ),
        ]

    def add_clicked(self, e):
        if self.new_task.value.strip():
            task = Task(
                self.new_task.value,
                self.task_status_change,
                self.task_delete
            )
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def clear_clicked(self, e):
        for task in self.tasks.controls[:]:
            if task.completed:
                self.task_delete(task)

    def tabs_changed(self, e):
        self.update()

    def task_status_change(self, e=None):
        self.update()

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for task in self.tasks.controls:
            task.visible = (
                status == "todos"
                or (status == "ativos" and not task.completed)
                or (status == "concluidos" and task.completed)
            )
            if not task.completed:
                count += 1
        self.items_left.value = f"{count} item(ns) ativo(s) restante(s)"

    def update(self):
        self.before_update()
        super().update()


# Função principal que inicializa o app
def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    todo = TodoApp()
    page.add(todo)


# Linha para rodar o app
ft.app(target=main)
