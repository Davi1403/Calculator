import flet as ft
from flet import colors
from decimal import Decimal

botoes = [
    {'operador': 'AC', 'fonte': colors.BLACK, 'fundo':colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo':colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo':colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo':colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo':colors.ORANGE}, 
    {'operador': '4', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo':colors.ORANGE}, 
    {'operador': '1', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo':colors.ORANGE}, 
    {'operador': '0', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo':colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo':colors.ORANGE}
]

def main(page: ft.Page):
    page.bgcolor = '#000' # Cor da tela
    page.window_resizable = False #Não permite o usuário redimencionar a tela
    page.window_width = 270 #Largura
    page.window_height = 400 #Altura
    page.title = "Calculator" #Título
    page.window_always_on_top = True #Janela sempre na frente

    result = ft.Text(value= '0', color = colors.WHITE, size = 20, text_align= ft.TextAlign.RIGHT)

    def calculate(operador, value_atual):

        try:    
            value = eval(value_atual) #
            
            if operador == '%':
                value /= 100
            elif operador == '±':
                value = - value
        except:
            return "Error"

        digits = min(abs(Decimal(value).as_tuple().exponent), 5) # 5 casa decimais
        return format(value,f'.{digits}f')

    def select(e):
        value_atual = result.value if result.value not in ('0','Error') else '' #Valor do painel
        value = e.control.content.value #Valor do botão (evento,elementos do evento,conteúdo,valor) Linha 48
        
        if value.isdigit():
            value = value_atual + value
        elif value == 'AC':
            value = '0'
        else:
            if value_atual and value_atual[-1] in ('/','*','-','+','.'): # [-1] Pega o ultimo elemento de uma string
                value_atual = value_atual[:-1] #Remove o ultimo caracter do calor atual
                

            value = value_atual + value

            if value[-1] in ('=','%','±'):
                value = calculate(operador=value[-1], value_atual=value_atual)
        
        result.value = value
        result.update()
                

    #Criar os itens da página

    display = ft.Row(
        width=270,#Largura
        controls = [result], #Recebe o resultado
        alignment = 'end' #Alinhamento no fim
    )
    btn =[ft.Container(
            content=ft.Text(value=btn['operador'], color=btn['fonte']),
            width=50, #Largura
            height=50, #Altura
            bgcolor=btn['fundo'], #Cor de fundo
            border_radius=100, #Arredonda as bordas
            alignment= ft.alignment.center, #Alinhamento
            on_click=select #Ao clicar no botão chama a função select
            ) for btn in botoes]
    
    keyboard = ft.Row(
        width=250,
        wrap= True, #Quebra para a linha de baixo
        controls=btn,
        alignment='end'
    )

    #Adicionar itens a página
    page.add (display,keyboard)

ft.app(target = main)