import pyautogui
import time

# Coordenadas do arquivo (exemplo)
coordenadas_arquivo = (422, 54)  # Substitua pelas coordenadas reais

# Função para abrir o arquivo automaticamente usando as coordenadas fornecidas
def abrir_arquivo(coordenadas):
    pyautogui.doubleClick(coordenadas)
    time.sleep(10)  # Reduzido o tempo de espera para o arquivo abrir

# Abrir o arquivo usando as coordenadas fornecidas
time.sleep(7)
abrir_arquivo(coordenadas_arquivo)

# Tempo para o usuário fechar o VS Code e clicar na área de trabalho
print("Você tem 10 segundos para fechar o VS Code e clicar na área de trabalho...")
time.sleep(10)

# Coordenada para o clique
coordenada_primeiro_clique = (1052, 334)

# Função para realizar as ações nas coordenadas fornecidas e pressionar as teclas
def realizar_acoes(coordenada):
    # Clique na coordenada fornecida
    pyautogui.click(coordenada)
    time.sleep(1)
    
    # Pressionar a tecla down e enter
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    
    # Pressionar a tecla down duas vezes
    pyautogui.press('down', presses=2, interval=0.05)
    
    # Pressionar a tecla tab
    pyautogui.press('tab')
    
    # Digitar "9174" e pressionar enter
    pyautogui.write("9174", interval=0.05)
    pyautogui.press('enter')
    
    # Clique na coordenada adicional
    pyautogui.click((445, 479))

# Realizar as ações nas coordenadas fornecidas
realizar_acoes(coordenada_primeiro_clique)

print("Ações concluídas com sucesso!")