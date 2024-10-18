import tkinter as tk
import time

# Função para criar a splash screen
def create_splash_screen():
    # Cria a janela splash
    splash = tk.Tk()
    splash.title("Splash Screen")

    # Define o tamanho e a posição da janela
    width, height = 300, 200
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    splash.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    # Desabilita redimensionamento da janela
    splash.resizable(False, False)

    # Adiciona um rótulo com texto ou imagem na splash screen
    label = tk.Label(splash, text="Carregando...", font=("Helvetica", 18))
    label.pack(expand=True)

    # Exibe a janela splash
    splash.update()

    # Espera alguns segundos (simula o tempo de carregamento)
    time.sleep(3)

    # Fecha a janela splash e retorna
    splash.destroy()

# Função para criar a janela principal
def create_main_window():
    # Cria a janela principal
    main_window = tk.Tk()
    main_window.title("Janela Principal")

    # Define o tamanho da janela principal
    main_window.geometry("400x300")

    # Adiciona um rótulo na janela principal
    label = tk.Label(main_window, text="Bem-vindo à Janela Principal", font=("Helvetica", 16))
    label.pack(expand=True)

    # Exibe a janela principal
    main_window.mainloop()

# Função principal
def main():
    # Cria a splash screen
    create_splash_screen()

    # Cria a janela principal após a splash
    create_main_window()

if __name__ == '__main__':
    main()
