import pyautogui
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# Função para mostrar a área de trabalho
def mostrar_area_de_trabalho():
    pyautogui.hotkey('win', 'd')  # Atalho do Windows para mostrar a área de trabalho

# Função para exibir a caixa de diálogo
def exibir_caixa_de_dialogo():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    resposta = messagebox.askquestion("Confirmação", "Deseja continuar?")
    root.destroy()
    return resposta

# Mostrar a área de trabalho
mostrar_area_de_trabalho()

# Exibir a caixa de diálogo
resposta = exibir_caixa_de_dialogo()

# Verificar a resposta do usuário
if resposta == 'no':
    print("Ação cancelada pelo usuário.")
else:
    # Coordenada pasta usinagem
    coordenada_duplo_clique = (192, 142)

    # Abrindo pasta de usinagem
    pyautogui.doubleClick(coordenada_duplo_clique)
    time.sleep(2)  # Tempo aumentado para maior confiabilidade

    # Coordenada para arquivo de usinagem
    coordenada_duplo_clique = (475, 176)

    # Realizar o duplo clique no arquivo
    pyautogui.doubleClick(coordenada_duplo_clique)
    time.sleep(2)  # Tempo aumentado para maior confiabilidade

    # Pressionar Enter após 2 segundos
    time.sleep(2)
    pyautogui.press('enter')

    # Coordenada para mudar guia e ir até usinagem
    coordenada_duplo_clique = (302, 989)

    # Aumentar o tempo para garantir que o Excel esteja completamente carregado
    time.sleep(5)  # Aguarda 5 segundos para garantir que o Excel esteja pronto

# Realizar o clique na guia de usinagem
    pyautogui.click(coordenada_duplo_clique)
    time.sleep(4)  # Aguarda 4 segundos para garantir que a guia seja aberta corretamente

    # Criar a interface gráfica para inserir a célula final
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal

    # Solicitar ao usuário a célula final
    celula_final = simpledialog.askstring("Entrada", "Digite a célula final (ex: A52):")

    # Selecionar o intervalo de A9 até a célula final
    pyautogui.hotkey('ctrl', 'g')  # Abrir a caixa "Ir Para"
    time.sleep(3)  # Aumentar o tempo para garantir que a caixa seja aberta
    pyautogui.write(f'A9:{celula_final}')  # Digitar o intervalo
    time.sleep(1.5)  # Pequena pausa antes de pressionar Enter
    pyautogui.press('enter')  # Confirmar
    time.sleep(2)  # Garantir que a seleção foi concluída

    # Copiar a seleção para a área de transferência
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Garantir que a cópia foi concluída

    # Mostrar a área de trabalho
    mostrar_area_de_trabalho()

    # Coordenada para abrir a pasta que fica os downloads da fabricação
    coordenada_duplo_clique_pasta_download_fabricação = (36, 139)
    pyautogui.doubleClick(coordenada_duplo_clique_pasta_download_fabricação)
    time.sleep(2)  # Tempo aumentado para maior confiabilidade

    # Coordenada para abrir o arquivo Excel dentro da pasta de downloads da fabricação
    coordenada_duplo_clique_arquivo = (467, 176)
    pyautogui.doubleClick(coordenada_duplo_clique_arquivo)
    time.sleep(2)  # Tempo aumentado para maior confiabilidade

    # Esperar 25 segundos para evitar bugs (não alterado)
    time.sleep(25)

# Ir para a célula A3
pyautogui.hotkey('ctrl', 'g')  # Abrir a caixa "Ir Para"
time.sleep(2)  # Aguarda 2 segundos para garantir que a caixa seja aberta
pyautogui.write('A3')  # Digitar a célula A3
time.sleep(1)  # Pequena pausa antes de pressionar Enter
pyautogui.press('enter')  # Confirmar
time.sleep(2)  # Garantir que a célula foi selecionada

# Colar o conteúdo da área de transferência como valores
pyautogui.hotkey('ctrl', 'alt', 'v')  # Abrir a janela "Colar Especial"
time.sleep(2)  # Aguarda 2 segundos para garantir que a janela seja aberta
pyautogui.press('v')  # Selecionar "Valores"
time.sleep(1)  # Pequena pausa antes de confirmar
pyautogui.press('enter')  # Confirmar a colagem como valores
time.sleep(2)  # Garantir que a ação foi concluída