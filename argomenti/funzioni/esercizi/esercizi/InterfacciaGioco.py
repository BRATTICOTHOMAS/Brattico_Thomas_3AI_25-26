#SOLO ROBA STRA DI BASE
import flet as ft

def main(page: ft.Page):
    page.title = "Exit Menu Example"

    # Create the exit dialog
    exit_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Massimo"),
        content=ft.Text("Vuoi uscire?"),
        actions=[
            ft.TextButton("Cancel", on_click=lambda e: close_dialog()),
            ft.TextButton("Exit", on_click=lambda e: exit_app()),
        ],
        open=False,
    )

    def close_dialog():
        exit_dialog.open = False
        page.update()

    def exit_app():
        page.window_close(), # closes the window (works in desktop/web)

    # Keyboard handler
    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Escape":
            if not exit_dialog.open:
                exit_dialog.open = True
                page.update()
            else:
                close_dialog()

    page.on_keyboard_event = on_keyboard

    page.add(ft.Text("Press ESC to open the exit menu."), exit_dialog)

ft.app(main)
