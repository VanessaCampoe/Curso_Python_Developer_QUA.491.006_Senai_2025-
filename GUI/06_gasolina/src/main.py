import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )import flet as ft

def main(page: ft.Page):
    page.title = "Comparador de Combustível"
    
    # Inputs para os preços
    alcool_input = ft.TextField(label="Preço do Álcool (R$)", keyboard_type="number")
    gasolina_input = ft.TextField(label="Preço da Gasolina (R$)", keyboard_type="number")
    
    # Texto de resultado
    resultado = ft.Text(value="", size=20, color=ft.colors.BLUE)

    def calcular_combustivel(e):
        try:
            preco_alcool = float(alcool_input.value.replace(",", "."))
            preco_gasolina = float(gasolina_input.value.replace(",", "."))
            
            if preco_alcool / preco_gasolina < 0.7:
                resultado.value = "Abasteça com Álcool"
                resultado.color = ft.colors.GREEN
            else:
                resultado.value = "Abasteça com Gasolina"
                resultado.color = ft.colors.ORANGE

        except ValueError:
            resultado.value = "Digite valores válidos para ambos os combustíveis!"
            resultado.color = ft.colors.RED
        
        resultado.update()

    # Botão para calcular
    botao_calcular = ft.ElevatedButton(text="Calcular", on_click=calcular_combustivel)

    # Layout na tela
    page.add(
        ft.SafeArea(
            ft.Container(
                content=ft.Column([
                    ft.Text("Comparador Álcool vs Gasolina", size=24, weight=ft.FontWeight.BOLD),
                    alcool_input,
                    gasolina_input,
                    botao_calcular,
                    resultado
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                alignment=ft.alignment.center,
                padding=20
            ),
            expand=True
        )
    )

ft.app(target=main)



ft.app(main)
