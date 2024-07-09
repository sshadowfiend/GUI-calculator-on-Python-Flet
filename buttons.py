import flet as ft


class Button:
    def __init__(self, val: str, field: ft.Text, page: ft.Page, color=ft.colors.BLUE_400, width=75) -> None:
        self.val = val
        self.color = color
        self.width = width
        self.field = field
        self.page = page

    def create_btn(self) -> ft.ElevatedButton:
        txt = ft.Text(value=self.val,
                      color="WHITE",
                      text_align=ft.TextAlign.CENTER,
                      size=20,
                      style=ft.TextStyle()
                      )
        btn = ft.ElevatedButton(content=txt,
                                width=self.width,
                                bgcolor=self.color,
                                height=60,
                                )
        return btn


class ButtonNum(Button):
    def create_btn(self) -> ft.ElevatedButton:
        txt = ft.Text(value=self.val,
                      color="WHITE",
                      text_align=ft.TextAlign.CENTER,
                      size=20,
                      style=ft.TextStyle()
                      )
        btn = ft.ElevatedButton(content=txt,
                                width=self.width,
                                bgcolor=self.color,
                                height=60,
                                on_click=self.add
                                )
        return btn

    def add(self, e) -> None:
        if self.field.value != '0' and self.field.value.count(' ') == 0:
            self.field.value += self.val
        else:
            self.field.value = self.val
        self.page.update()
