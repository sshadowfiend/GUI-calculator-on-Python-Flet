import flet as ft
from buttons import Button, ButtonNum
global operation
global num1


def main(page: ft.Page):

    def convert(n: str):
        if n.count('.') == 0:
            return int(n)
        i = n.index('.')
        if n[i + 1:] == '0':
            return int(n[:i])
        return float(n)

    def clear_fast(e):
        if len(txt1.value) == 1 or txt1.value == " Error" or txt1.value.count("e") != 0 or (len(txt1.value) == 2 and txt1.value[0] == '-'):
            txt1.value = '0'
            page.update()
        else:
            txt1.value = txt1.value[:-1]
            page.update()

    def clear_long(e):
        txt1.value = '0'
        page.update()

    def change(e):
        try:
            txt1.value = str(convert(txt1.value) * -1)
            page.update()
        except ValueError:
            pass

    def percent(e):
        try:
            txt1.value = str(convert(str(convert(txt1.value) / 100)))
            page.update()
        except ValueError:
            pass

    def dot(e):
        if txt1.value.count('.') == 0 and txt1.value.count(' ') == 0:
            txt1.value += '.'
        page.update()

    def math_operations(e):
        try:
            global operation
            operation = e.control.data
            global num1
            num1 = convert(txt1.value)
            txt1.value = ' ' + txt1.value
        except ValueError:
            pass

    def equal(e):
        num2 = convert(txt1.value)
        result = 0
        if operation == '÷':
            if num2 != 0:
                result = convert(str(num1 / num2))
            else:
                result = 'Error'
        elif operation == 'x':
            result = convert(str(num1 * num2))
        elif operation == '+':
            result = convert(str(num1 + num2))
        elif operation == '-':
            result = convert(str(num1 - num2))
        txt1.value = ' ' + str(result)
        page.update()

    page.title = "Super calculator"
    page.window_width = 365
    page.window_height = 510
    page.window_resizable = False
    page.bgcolor = ft.colors.BLUE_200
    page.horizontal_alignment = "CENTER"
    page.vertical_alignment = "CENTER"
    page.update()

    txt1 = ft.Text(value='0', size=52, color="WHITE", text_align=ft.TextAlign.RIGHT)
    all_numbers = ft.Card(content=txt1, height=100, width=340, color=ft.colors.BLUE_200)

    btn1 = ButtonNum("1", txt1, page).create_btn()
    btn2 = ButtonNum("2", txt1, page).create_btn()
    btn3 = ButtonNum("3", txt1, page).create_btn()
    btn4 = ButtonNum("4", txt1, page).create_btn()
    btn5 = ButtonNum("5", txt1, page).create_btn()
    btn6 = ButtonNum("6", txt1, page).create_btn()
    btn7 = ButtonNum("7", txt1, page).create_btn()
    btn8 = ButtonNum("8", txt1, page).create_btn()
    btn9 = ButtonNum("9", txt1, page).create_btn()
    btn0 = ButtonNum("0", txt1, page, width=160).create_btn()

    btn_clear = Button("AC", txt1, page, ft.colors.BLUE_300).create_btn()
    btn_change = Button("+-", txt1, page, ft.colors.BLUE_300).create_btn()
    btn_percent = Button("%", txt1, page, ft.colors.BLUE_300).create_btn()
    btn_div = Button("÷", txt1, page, ft.colors.PINK_200).create_btn()
    btn_mult = Button("x", txt1, page, ft.colors.PINK_200).create_btn()
    btn_minus = Button("-", txt1, page, ft.colors.PINK_200).create_btn()
    btn_plus = Button("+", txt1, page, ft.colors.PINK_200).create_btn()
    btn_equal = Button("=", txt1, page, ft.colors.PINK_200).create_btn()
    btn_dot = Button(",", txt1, page).create_btn()

    btn_clear.on_click = clear_fast
    btn_clear.on_long_press = clear_long
    btn_change.on_click = change
    btn_percent.on_click = percent
    btn_dot.on_click = dot
    btn_div.data = '÷'
    btn_mult.data = 'x'
    btn_plus.data = '+'
    btn_minus.data = '-'
    btn_div.on_click = math_operations
    btn_mult.on_click = math_operations
    btn_plus.on_click = math_operations
    btn_minus.on_click = math_operations
    btn_equal.on_click = equal

    page.add(
        ft.Column(
            [
                all_numbers,
                ft.Row([btn_clear, btn_change, btn_percent, btn_div]),
                ft.Row([btn7, btn8, btn9, btn_mult]),
                ft.Row([btn4, btn5, btn6, btn_minus]),
                ft.Row([btn1, btn2, btn3, btn_plus]),
                ft.Row([btn0, btn_dot, btn_equal])
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
