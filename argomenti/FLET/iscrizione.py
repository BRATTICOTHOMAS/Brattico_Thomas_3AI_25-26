import datetime
import flet as ft

def main(page: ft.Page):
   
    def bottone_click(e):
        pass
    page.bgcolor = ft.Colors.BLUE_100
    def salva(e):
        nome_input=tb_nome_giocatore.value
        cognome_input=tb_cognome_giocatore.value
        età_input_str=tb_età_giocatore.value
        età_input=int(età_input_str)
        if età_input>=18:
            print("ciao")
           
           
       
        print(nome_input,cognome_input,età_input)
   
    txt_TITOLO=ft.Text("ISCRIZIONE TORNEO POKEMON ",size=40,color=ft.Colors.BLACK,weight=ft.FontWeight.BOLD)
    tb_nome_giocatore=ft.TextField(label="mettere il nome",hint_text=" ciccio")
    tb_cognome_giocatore=ft.TextField(label="mettere il cognome",hint_text=" pasticcio")
    tb_età_giocatore=ft.TextField(label="età",hint_text=" 18",width=100)
    tb_dropD_mazzo = ft.Dropdown(
    label="main type",
    options=[
        ft.dropdown.Option("Acqua"),
        ft.dropdown.Option("Fuoco"),
        ft.dropdown.Option("Erba"),
        ft.dropdown.Option("Terra"),
        ft.dropdown.Option("Roccia"),
        ft.dropdown.Option("Acciaio"),
        ft.dropdown.Option("Ghiaccio"),
        ft.dropdown.Option("Elettro"),
        ft.dropdown.Option("Drago"),
    ],padding=40)
    tb_nome_main=ft.TextField(label="nome main",hint_text="sgsg")
    regione_preferita = ft.RadioGroup(
        value="niente",
        content=ft.Row([
            ft.Radio(value="niente", label="nessuna di queste"),
            ft.Radio(value="Games", label="UNIMA"),
            ft.Radio(value="sport", label="KALOS"),
            ft.Radio(value="RPG", label="PALDEA"),
        ])
    )
    bottone_partecipa=ft.Button("PARTECIPA", on_click=salva)    
   
    # !LAYOUT
    view = ft.Column([
           ft.Row([txt_TITOLO],alignment=ft.MainAxisAlignment.CENTER),
           ft.Row([tb_nome_giocatore,tb_cognome_giocatore,tb_età_giocatore],alignment=ft.MainAxisAlignment.CENTER,),
           
           ft.Row([tb_dropD_mazzo,tb_nome_main],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([regione_preferita], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([bottone_partecipa])
 
    ],spacing=30)  
 
 
    page.title="FESTA DI FINE ANNO"
    page.theme_mode=ft.ThemeMode.LIGHT
    page.add(view)
ft.app(main)
 

 