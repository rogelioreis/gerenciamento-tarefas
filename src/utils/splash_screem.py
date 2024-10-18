import tkinter as tk
import time

def create_splash_screen():
    splash = tk.Tk()
    splash.title("Splash Screen")

    width, height = 300, 200
    screen_width = splash.winfo_screenwidth()
    screen_height = splash.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    splash.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

    splash.resizable(False, False)

    label = tk.Label(splash, text="Carregando...", font=("Helvetica", 18))
    label.pack(expand=True)

    splash.update()

    time.sleep(3)

    splash.destroy()

def create_main_window():
    main_window = tk.Tk()
    main_window.title("Janela Principal")

    main_window.geometry("400x300")

    label = tk.Label(main_window, text="Bem-vindo à Janela Principal", font=("Helvetica", 16))
    label.pack(expand=True)

    main_window.mainloop()

def main():
    create_splash_screen()
    create_main_window()

if __name__ == '__main__':
    main()
