import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self.page = page
        self.page.title = "Template application using MVC and DAO"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.dd_anno = None
        self.btn_grafo = None
        self.dd_metodo = None
        self.btn_prodotti = None
        self.txt_soglia = None
        self.btn_cammino = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self.page.controls.append(self._title)

        self.dd_anno = ft.Dropdown(label="Anno")
        self.btn_grafo = ft.ElevatedButton(text="Crea grafo", on_click=self.controller.handle_crea_grafo)
        row1 = ft.Row([self.dd_anno, self.btn_grafo], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row1)

        self.dd_metodo = ft.Dropdown(label="Metodo")
        self.controller.fill_dds()
        self.btn_prodotti = ft.ElevatedButton(text="Calcola prodotti redditizi",
                                              on_click=self.controller.handle_piu_redditizi)
        row2 = ft.Row([self.dd_metodo, self.btn_prodotti], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row2)

        self.txt_soglia = ft.TextField(label="S")
        self.btn_cammino = ft.ElevatedButton(text="Calcola cammino", on_click=self.controller.handle_cammino)
        row3 = ft.Row([self.txt_soglia, self.btn_cammino], alignment=ft.MainAxisAlignment.CENTER)
        self.page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.page.controls.append(self.txt_result)
        self.page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def update_page(self):
        self.page.update()
