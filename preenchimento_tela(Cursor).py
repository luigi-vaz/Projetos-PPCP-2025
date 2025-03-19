import pyautogui
import time

# Dados a serem preenchidos
dados = [
    "191642",  # Número de OS
    "130607",  # Código TR
    "16",  # Quantidade
    "19/03/2025",  # Necessidade
    "PRATICA 30000 TRIDEM  - CAMPANELLI"  # Descrição do Produto
]

# Coordenadas do campo de descrição (exemplo)
coordenadas_descricao = (372, 800)  # Substitua pelas coordenadas reais

# Função para escrever texto na posição inicial do mouse e usar Enter para navegar entre os campos
def preencher_campos(dados):
    for i, texto in enumerate(dados):
        pyautogui.write(texto, interval=0.1)
        if i == 3:  # Se for o campo Data Necessidade
            pyautogui.press('down')
        else:
            pyautogui.press('enter')
        if i == 1:  # Se for o campo Código TR
            time.sleep(3)
        time.sleep(3)  # Espera de 3 segundos antes de pressionar Enter

# Espera para posicionar o cursor no primeiro campo
print("Posicione o cursor no primeiro campo e aguarde...")
time.sleep(5)

# Preencher os campos com os dados fornecidos
preencher_campos(dados)

# Passar pela área de fabricação sem alterar nada
pyautogui.press('down', presses=3, interval=0.1)

# Clicar no campo de descrição pela coordenada e escrever a descrição do produto
pyautogui.click(coordenadas_descricao)
pyautogui.write(dados[-1], interval=0.1)

print("Preenchimento concluído!")