import flet as ft
import json
import requests

def main(page: ft.Page):

    lbtitolo = ft.Text("🎵 Ricerca Brano 🎵", size=50, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    artista = ft.TextField(label="Inserisci il nome del cantante", hint_text="ANNA")
    brano = ft.TextField(label="Inserisci il titolo del brano", hint_text="Bando")

    testo_stroke = ft.Text(
        spans=[ft.TextSpan(
            text="",
            style=ft.TextStyle(
                size=16,
                foreground=ft.Paint(
                    color=ft.Colors.YELLOW_900,
                    stroke_width=3,
                    style=ft.PaintingStyle.STROKE,
                ),
            ),
        )],
    )

    testo_fill = ft.Text(
        spans=[ft.TextSpan(
            text="",
            style=ft.TextStyle(
                size=16,
                color=ft.Colors.YELLOW,
            ),
        )],
    )

    contenitore_testo = ft.Container(
        content=ft.Stack([testo_stroke, testo_fill]),
        bgcolor=ft.Colors.BLUE_GREY_800,
        border=ft.Border.all(2, ft.Colors.YELLOW),
        border_radius=ft.BorderRadius.all(20),
        padding=20,
        alignment=ft.Alignment(0, 0),
        visible=False,
    )


    slider_label = ft.Text("Dimensione testo: 16", color=ft.Colors.WHITE, size=14)

    def on_slider_change(e):
        nuova_dimensione = int(e.control.value)
        slider_label.value = f"Dimensione testo: {nuova_dimensione}"
        testo_stroke.spans[0].style.foreground.stroke_width = nuova_dimensione / 5
        testo_stroke.spans[0].style.size = nuova_dimensione
        testo_fill.spans[0].style.size = nuova_dimensione
        page.update()

    def aggiorna_bottone(e):
        entrambi_compilati = bool(artista.value.strip() and brano.value.strip())
        btInvia.disabled = not entrambi_compilati
        slider_testo.disabled = not entrambi_compilati
        page.update()

    artista.on_change = aggiorna_bottone
    brano.on_change = aggiorna_bottone

    slider_testo = ft.Slider(
        min=10,
        max=40,
        value=16,
        divisions=30,
        label="{value}",
        on_change=on_slider_change,
        disabled=True,                 
        active_color=ft.Colors.YELLOW,
        inactive_color=ft.Colors.BLUE_GREY_400,
        thumb_color=ft.Colors.YELLOW_700,
        width=400,
    )

    def esegui_ricerca():
        artist = artista.value
        song = brano.value
        try:
            x = requests.get(f"https://api.lyrics.ovh/v1/{artist}/{song}")
            elenco = json.loads(x.text)
            testo_canzone = elenco["lyrics"]
            testo_stroke.spans[0].text = f"Il testo della canzone è:\n{testo_canzone}"
            testo_fill.spans[0].text   = f"Il testo della canzone è:\n{testo_canzone}"
        except Exception as err:
            testo_stroke.spans[0].text = f"Errore: {err}"
            testo_fill.spans[0].text   = f"Errore: {err}"
        contenitore_testo.visible = True
        page.update()

    def mostra_modale(e):

        if not artista.value.strip() or not brano.value.strip():
            page.show_dialog(ft.AlertDialog(
                modal=True,
                title=ft.Text("⚠️ Attenzione"),
                content=ft.Text("Compila entrambi i campi prima di cercare!"),
                actions=[
                    ft.TextButton("OK", on_click=lambda e: page.pop_dialog()),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            ))
            return

        def on_conferma(e):
            page.pop_dialog()
            esegui_ricerca()

        page.show_dialog(ft.AlertDialog(
            modal=True,
            title=ft.Text("🎵 Conferma ricerca"),
            content=ft.Text(
                f"Vuoi cercare il testo di:\n\n"
                f"🎤 Artista: {artista.value}\n"
                f"🎵 Brano:   {brano.value}"
            ),
            actions=[
                ft.TextButton("✅ Sì, cerca!", on_click=on_conferma),
                ft.TextButton("❌ Annulla",    on_click=lambda e: page.pop_dialog()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modale chiuso"),
        ))

    btInvia = ft.Button(
        content="Cerca testo",
        on_click=mostra_modale,
        disabled=True,          
    )

    layout = ft.Column([
        ft.Row([lbtitolo],                      alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([artista],                        alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([brano],                          alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([btInvia],                        alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([slider_label],                   alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([slider_testo],                   alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        ft.Row([contenitore_testo],              alignment=ft.MainAxisAlignment.CENTER),
    ])

    page.title = "IL BRANO CHE TI PIACE"
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_500
    page.add(layout)

ft.run(main)