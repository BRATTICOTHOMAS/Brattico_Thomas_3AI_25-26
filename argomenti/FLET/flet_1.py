import datetime
import flet as ft

def main(page: ft.Page):
    # Eventi
    def btNome_click(e):
        lbNome.value = "Hai premuto"
        if tbNome.value == "":
            tbNome.value = "Inserire un nome ad es Super Mario"
        else:
            lbNome.value = f"Ciao {tbNome.value} benvenuto."

    # Controlli
    # https://flet-controls-gallery.fly.dev/
    # https://examples.flet.dev/icons_browser/
    tbNome = ft.TextField(label="Inserire nome", icon=ft.Icons.GROUP_ADD)
    btNome = ft.ElevatedButton("Conferma", on_click=btNome_click)
    lbNome = ft.Text("Messaggio")

    # Layout pagina
    view = ft.Column([
        ft.Row([ ft.Text("App dimostrativa per l'uso dei controlli") ]),
        ft.Row([ tbNome, btNome ]),
        ft.Row([ lbNome ]),
        ft.Row([ ft.Text("Divertiti con il mio programma") ]),
    ])

    page.title = "Controlli"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(view)

ft.app(main)