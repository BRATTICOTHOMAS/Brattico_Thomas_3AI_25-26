import flet as ft
from flet import TextField
from flet import ControlEvent
def main(page: ft.Page) -> None:
    page.title = "Increment counter"
    page.vertical_alignment= ft.MainAxisAlignment.CENTER
    page.theme_mode="Light"
 
    text_Number: TextField = TextField(value="0", text_align=ft.TextAlign.RIGHT,width=100)
 
    def decrement(e: ControlEvent) -> None:
        text_Number.value =str(int(text_Number.value) -1)
        page.update()
    def increment(e: ControlEvent) -> None:
        text_Number.value =str(int(text_Number.value) +1)
        page.update()
   
 
    page.add(
        ft.Row(
            [ft.IconButton(ft.Icons.REMOVE, on_click=decrement),
             text_Number,ft.IconButton(ft.Icons.ADD, on_click=increment)],
             alignment=ft.MainAxisAlignment.CENTER
        )
    )
if __name__ == "__main__":
    ft.app(target=main, )
 