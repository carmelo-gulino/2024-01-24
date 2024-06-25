import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.chosen_method = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fill_dds(self):
        for y in range(2015, 2019):
            self.view.dd_anno.options.append(ft.dropdown.Option(f"{y}"))
        for m in self.model.methods:
            self.view.dd_metodo.options.append(ft.dropdown.Option(text=m.Order_method_type,
                                                                  data=m.Order_method_code,
                                                                  on_click=self.choose_method))
    
    def choose_method(self, e):
        if e.control.data is None:
            self.chosen_method = None
        self.chosen_method = e.control.data

    def handle_crea_grafo(self, e):
        year = int(self.view.dd_anno.value)
        soglia = float(self.view.txt_soglia.value)
        self.model.build_graph(year, self.chosen_method, soglia)
        self.view.txt_result.controls.clear()
        nodi, archi = self.model.get_graph_details()
        self.view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nodi} nodi e {archi} archi"))
        self.view.update_page()

    def handle_piu_redditizi(self, e):
        piu_redditizi = self.model.get_piu_redditizi()
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"I cinque prodotti più redditizi sono:"))
        for r in piu_redditizi:
            self.view.txt_result.controls.append(ft.Text(f"{r[0]} --> Archi entranti: {r[1]} "
                                                         f"Ricavo: {float(r[0].ricavo_tot)}"))
        self.view.update_page()

    def handle_cammino(self, e):
        path = self.model.get_percorso()
        self.view.txt_result.controls.clear()
        self.view.txt_result.controls.append(ft.Text(f"Il percorso di lunghezza massima ({len(path)+1}) "
                                                     f"trovato è il seguente:"))
        for p in path:
            self.view.txt_result.controls.append(ft.Text(f"{p[0]} --> {p[1]}"))
        self.view.update_page()

    @property
    def view(self):
        return self._view

    @property
    def model(self):
        return self._model
