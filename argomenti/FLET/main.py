import flet as ft

def main(page: ft.Page):
    # Eventi
    

    def btPartecipa_click(e):
       nome=tfNome.value
       cognome=tfCognome.value
       comune=DropdownComune.value
       classe=DropdownClasse.value
       attivita=Radioattività.value


       
          
    
    

    # Controlli
    # https://flet-controls-gallery.fly.dev/
    # https://examples.flet.dev/icons_browser/


    # Layout pagina
    
    Radioattività=ft.RadioGroup(value="Niente", content=ft.Row(  #il value nel radio group è l'impostazione di default.
                    [
                        ft.Radio(value="Niente",label="Nessuna attività",),
                        ft.Radio(value="Sport",label="Sport",),
                        ft.Radio(value="Games",label="Videogiochi",),
                        ft.Radio(value="RPG",label="Giochi da tavolo",),
                    ]
                ))
    DropdownClasse=ft.Dropdown(label="classe       ",
                              options=[ft.dropdown.Option("1A   "),
                                       ft.dropdown.Option("2A   "),
                                       ft.dropdown.Option("3AI  "),
                                       ft.dropdown.Option("4AI  "),
                                       ft.dropdown.Option("5AI  "), ]) 
    DropdownComune=ft.Dropdown(label="comune di provenieza",
                              options=[ft.dropdown.Option("Dalmine"),
                                       ft.dropdown.Option("Osio Sopra"),
                                       ft.dropdown.Option("Almenno San Bartolomeo"),
                                       ft.dropdown.Option("Curno"),
                                       ft.dropdown.Option("Romano di Lombardia"),
                                       ft.dropdown.Option("Almè"), ])
    tfNome=ft.TextField(label="inserisci il tuo nome", hint_text="john")
    tfCognome=ft.TextField(label="inserisci il tuo cognome", hint_text="ciccio")
    view = ft.Column([
        ft.Row([ ft.Text("Iscrizione alla festa di fine anno.    ") ]),
        ft.Row([tfNome]), #le parentesi quadre servono per aggiungere piu controlli in una riga
        ft.Row([tfCognome]),
        ft.Row([ DropdownComune ]),
        ft.Row([ DropdownClasse]),
        
        ft.Divider(),
        ft.Row([ ft.Checkbox(value=False, label="Xbox"), 
                ft.Checkbox(value=True, label="Psx"),
                ft.Checkbox(value=False, label="Switch"),
                ft.Checkbox(value=False, label="Ds"),
                ft.Checkbox(value=False, label="Ouya"),
                ft.Checkbox(value=False, label="Wii"),
                ]),
        ft.Row([ft.Button("Partecipa",on_click=btPartecipa_click) ]),
        
        #hint text quando clicco sulla casella per scrivere ti da un suggerimento di quello che devi scrivere
    ])

    page.title = "Festa di fine anno scolastico"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.add(view)

ft.app(main)