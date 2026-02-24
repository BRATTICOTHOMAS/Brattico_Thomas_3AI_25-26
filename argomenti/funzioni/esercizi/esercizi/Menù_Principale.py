import flet as ft
from flet import TextField
from flet import ControlEvent
from flet import MouseCursor,View, Page, AppBar,Text,RouteChangeEvent,ViewPopEvent,CrossAxisAlignment, MainAxisAlignment
import time
import pygame

pygame.init()
pygame.mixer.init()

Background = pygame.mixer.Sound("assets/Europa Universalis IV - Original Soundtrack _ OST - Main Theme [XdxOh5ooI5k].mp3")
click = pygame.mixer.Sound("assets/Clicksound.mp3")
hover = pygame.mixer.Sound("assets/Overclick.mp3")
initial_volume = 100 # Volume iniziale (0.0 a 1.0)
Background.set_volume(initial_volume / 100) # Imposta il volume iniziale
Background.play()

animation = ft.Animation(100,ft.AnimationCurve.FAST_OUT_SLOWIN)

def main(page: ft.Page) -> None:
    page.title = "Politiks-Dev"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "Light"
    sfx_on = True

    # CONTROLLI E FUNZIONI DI STATO / VOLUME
    
    # Testo dinamico per mostrare la percentuale del volume
    volume_text_display = ft.Text(
        f"{initial_volume}%", 
        size=20, 
        width=50 
    )

    def change_music_volume(e: ft.ControlEvent):
        """Aggiorna il volume di Pygame e il testo dinamico solo quando lo slider cambia."""
        # Prende il valore dello slider (0-100)
        slider_value_int = int(e.control.value)
        
        # Converte in percentuale Pygame (0.0-1.0)
        volume_percent = slider_value_int / 100.0
        
        # Applica il volume al suono Background
        Background.set_volume(volume_percent)
        
        # Aggiorna il testo del volume in tempo reale
        volume_text_display.value = f"{slider_value_int}%"
        
        page.update()
 
    # --- FUNZIONI DI RIPRODUZIONE CON CONTROLLO DI STATO ---

    
    def play_click_sfx():
        nonlocal sfx_on
        """Riproduce il suono del click solo se gli SFX sono ON."""
        if sfx_on:
            click.play()

    def play_hover_sfx():
        nonlocal sfx_on
        """Riproduce il suono dell'hover solo se gli SFX sono ON."""
        if sfx_on:
            hover.play()
            

    # --- HANDLER TOGGLE EFFETTI SONORI ---

    
    sfx_text = ft.Text("Effetti Sonori: ON", size=20)
    
    def toggle_sfx(e):
        """Aggiorna lo stato di sfx_on quando lo switch cambia."""
        nonlocal sfx_on
        sfx_on = e.control.value
        if sfx_on:
            pygame.mixer.unpause()  # Riattiva tutti i suoni
        else:
            pygame.mixer.pause()    # Mette in pausa tutti i suoni
        sfx_text.value = f"Effetti Sonori: {'ON' if sfx_on else 'OFF'}"
        page.update()


    def scale_out_hover(e: ft.ControlEvent):
        # Aumenta leggermente la scala al passaggio del mouse
            try:
                e.control.scale = 1.2
            except Exception:
                pass
            try:
                page.update()
            except Exception:
                pass
        

    def scale_in_hover(e: ft.ControlEvent):
        # Riporta la scala al valore originale quando il mouse esce
            try:
                e.control.scale = 0.95
            except Exception:
                pass
            try:
                page.update()
            except Exception:
                pass
    def go_to_settings(e):
        click.play()
        page.go("/settings")
    def go_to_main_menu(e):
        click.play()
        page.go("/")
    def create_animated_button(text: str, on_click_handler=None):
        # Crea il bottone e il contenitore animato; il container ha
        # `animate_scale` e sarà quello che modifichiamo per attivare
        # l'animazione.
        btn = ft.ElevatedButton(
            text=text,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                padding=ft.padding.symmetric(horizontal=30, vertical=15),
            ),
        )

        container_animato = ft.Container(
            content=btn,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=["#d2b48c", "#a0522d"]
            ),
            border_radius=5,
            animate_scale=animation,
            scale=1.0,
                on_hover=lambda e: scale_out_hover(e) if (e.data is True or str(e.data).lower() == "true") else scale_in_hover(e),
            padding=10,
        )

        def on_click_wrapper(e: ft.ControlEvent):
            # Il click deve animare il container (non il bottone interno)
            original_scale = container_animato.scale
            container_animato.scale = 0.95
            try:
                    page.update()
            except Exception:
                    pass

            play_click_sfx()
            if on_click_handler:
                on_click_handler(e)

            container_animato.scale = original_scale
            try:
                    page.update()
            except Exception:
                    pass

        btn.on_click = on_click_wrapper
        # Assicura che l'hover sul bottone modifichi il container (in alcuni
        # casi l'evento hover può essere catturato dal child); usiamo la
        # stessa logica robusta per rilevare enter/leave.
        btn.on_hover = lambda e: scale_out_hover(e) if (e.data is True or str(e.data).lower() == "true") else scale_in_hover(e)
        btn.on_hover = lambda e: (setattr(container_animato, 'scale', 1.05) or page.update() or play_hover_sfx()) if (e.data is True or str(e.data).lower() == "true") else (setattr(container_animato, 'scale', 1.0) or page.update())
        
        return container_animato
    btn1_animated = create_animated_button("GIOCA")
    btn2_animated = create_animated_button("INFORMAZIONI")
    btn3_animated = create_animated_button("IMPOSTAZIONI")
    btn3_animated.content.on_click= lambda e:(go_to_settings(e),click.play())
    btn4_animated = create_animated_button("ESCI")
    # In Flet, per chiudere l'app
    btn4_animated.content.on_click = lambda e: (page.window.close(),click.play())
    btn_back = create_animated_button("TORNA AL MENU")
    btn_back.content.on_click=lambda e:(go_to_main_menu(e),click.play())
    #switch effetti sonori
    sfx_switch_control = ft.Switch(
        value=sfx_on, # Stato iniziale
        on_change=toggle_sfx # Handler
    )
# Slider volume musica
    music_slider = ft.Slider(
        min=0, 
        max=100, 
        divisions=10, 
        value=initial_volume, 
        width=150,
        on_change=change_music_volume
    )
    # --- LAYOUT VISTA IMPOSTAZIONI ---
  
    
    settings_column = ft.Column(
        controls=[
            ft.Text("IMPOSTAZIONI", size=40, weight=ft.FontWeight.BOLD, ),
            ft.Container(height=30),
            # TESTI RICHIESTI PER IL MENU
            ft.Row(
                [
                    ft.Text("Volume Musica", size=20,width=200),
                    music_slider,
                    volume_text_display
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER,spacing=5
            ),
            
            # Riga per il toggle degli Effetti Sonori
            ft.Row(
                [
                    sfx_text,
                    sfx_switch_control 
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text("Risoluzione: Full HD", size=20, ),
            ft.Text("Lingua: Italiano", size=20, ),
            ft.Container(height=30),
            btn_back
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    settings_menu_container = ft.Container(
        content=settings_column,
        alignment=ft.alignment.center,
        expand=True
    )
    def video_state_changed(e: ft.ControlEvent):
      
        if e.data == "completed":
            e.control.play()
            page.update() 

    Img = ft.Image(src="assets/Logocontrastante.png",width=400, height=225,fit=ft.ImageFit.CONTAIN) 
    video_background = ft.Video(
        playlist=[ft.VideoMedia(resource="assets/Video senza titolo - Realizzato con Clipchamp.mp4")],
        playlist_mode=ft.PlaylistMode.LOOP, 
        autoplay=True,      
        muted=True,         
        show_controls=False,
        expand=True,)

    
    c= ft.Column(controls=[Img,ft.Container(height=25),btn1_animated,btn2_animated,btn3_animated,btn4_animated
        
    ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,)
    
    container=ft.Container(
        content=c, alignment=ft.alignment.center, 
    )
    
    
    page.add(
        ft.Stack(
            [
                video_background,
                container
            ],
            expand=True
        )
    )
    def route_change(e: ft.RouteChangeEvent):
        """Gestisce il cambio di rotta (URL) e aggiorna lo stack di viste."""
        
        # Svuota lo stack di viste per preparare la nuova vista
        page.views.clear()

        # 1. Aggiunge sempre la Vista Principale come base
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Stack(
                        [
                            video_background,
                            c
                        ],
                        expand=True
                    )
                ],
            )
        )

        # 2. Se la rotta è /settings, aggiunge la Vista Impostazioni
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        ft.Stack(
                            [
                                video_background, 
                                settings_menu_container 
                            ],
                            expand=True
                        )
                    ],
                )
            )

        page.update()

    def view_pop(e: ft.ViewPopEvent):
        """Gestisce il ritorno alla vista precedente (es. tasto Back del browser)."""
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
        
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Inizializza la navigazione sulla rotta principale quando l'app si avvia
    page.go(page.route)
    page.update()
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")