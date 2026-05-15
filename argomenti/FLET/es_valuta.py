import requests
import json
import flet as ft
 
def main(page: ft.Page):
    # Eventi
    def on_clickConversione(e):
        viniz=ddMoneta1.value
        vfin=ddMoneta2.value
        y = requests.get(f"https://open.er-api.com/v6/latest/{viniz}")
        elenco=json.loads(y.text)
        conversione=elenco["rates"][vfin]
        lbconversium.value=(f"1 {viniz} vale {conversione} {vfin}")
       
 
 
 
    text=""
    valute=[]
    x = requests.get(f"https://open.er-api.com/v6/latest/Eur")
    Api = json.loads(x.text)
 
    for key in Api["rates"]:
        valute.append(ft.DropdownOption(key))
 
 
    # Controlli
    lbtitolo = ft.Text(" scambio valute", size=50,color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    
    ddMoneta1 = ft.Dropdown(
                    label="Inserisci la moneta iniziale",
                    editable=True,
                    value="EUR",
                    options=valute,
                    )
   
    ddMoneta2 = ft.Dropdown(
                    label="Inserisci in quale moneta vuoi convertire",
                    editable=True,
                    value="USD",
                    options=valute,
                    )
   
 
    btInvia= ft.Button(content="Esegui conversione", on_click=on_clickConversione)
 
    lbconversium= ft.Text(color=ft.Colors.YELLOW)
 
    # Layout pagina
    layout = ft.Column([
        ft.Row([lbtitolo]),
        ft.Divider(),
        ft.Row([ddMoneta1, ddMoneta2]),
        ft.Row([btInvia, lbconversium]),
       
    ])
 
    page.add(layout)
 
ft.run(main)