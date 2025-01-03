import flet as ft
import os

def main(page: ft.Page):
    # Define the size of the window for the app
    page.window_width = 400  
    page.window_height = 800

    # Initial position of the game (first riddle)
    position = 1

    # Dictionary of riddles and codes: The key is the position (charada), the value is the code and the hint
    codes = {
        1: ("8341", "Já sustentei conversas saborosas..."),
        2: ("9474", "Inspiração em cada gole..."),
        # Add more riddles and codes here if needed!
    }

    # Function to show the game screen after the initial message is clicked
    def show_initial_message(e):
        initial_message.visible = False
        start_button.visible = False
        game_container.visible = True
        page.update()

    # Initial welcome message to be displayed
    initial_message = ft.Text(
        "Parabéns pelo seu dia, meu amor!\n"
        "Preparei algo simples, mas cheio de significado...\n"
        "Você terá que embarcar em uma pequena aventura para encontrar o presente misterioso!", 
        size=18,
        color="blue",
        text_align=ft.TextAlign.CENTER,
    )

    start_button = ft.ElevatedButton("Começar", on_click=show_initial_message)

    # Components of the game: current riddle and input area
    label_position = ft.Text(f"Charada {position}", size=30, weight=ft.FontWeight.BOLD)
    label_charade = ft.Text("Carregou o 'peso' de nossas histórias... Onde isso aconteceu?", size=20, color="blue")
    input_code = ft.TextField(label="Digite o código", width=300)
    confirm_button = ft.ElevatedButton("Confirmar", width=200)
    result_message = ft.Text("", color="green", size=18)

    # Function that checks if the user input is correct
    def confirm_action(e):
        nonlocal position
        code_number = input_code.value.strip()
        correct_code, next_hint = codes.get(position, ("", ""))

        if code_number == correct_code:
            position += 1
            if position > len(codes):  # No more riddles
                label_position.value = "Parabéns!"
                label_charade.value = "Espero que goste do presente! 😊"
                confirm_button.disabled = True
                input_code.disabled = True
            else:
                label_position.value = f"Charada {position}"
                label_charade.value = next_hint
            result_message.value = "Correto! Continue!"
            result_message.color = "green"
        else:
            result_message.value = "Código errado! 😅"
            result_message.color = "red"

        input_code.value = ""  # Clear input field after validation
        page.update()

    confirm_button.on_click = confirm_action

    # Game container (initially hidden)
    game_container = ft.Column(
        [
            label_position,
            label_charade,
            input_code,
            confirm_button,
            result_message,
        ],
        visible=False,
    )

    # Add everything to the page
    page.add(
        ft.Column(
            [
                initial_message,
                start_button,
                game_container,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

# Run the app in the browser
ft.app(target=main, view=ft.WEB_BROWSER)
