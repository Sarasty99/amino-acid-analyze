import tkinter as tk
from tkinter import ttk

def configure_styles():
    """Настройка стилей для Tkinter в тёплых пастельных тонах."""
    style = ttk.Style()

    # Основные цвета (тёплая палитра)
    BG_COLOR = "#f9f5f0"          # Светлый бежевый фон
    BTN_COLOR = "#d4a574"         # Мягкий золотистый (для кнопок)
    BTN_HOVER = "#c49564"         # Более тёмный оттенок при наведении
    TEXT_COLOR = "#5e4a3a"        # Тёмно-коричневый текст
    ENTRY_COLOR = "#fefbf6"       # Кремовый фон для полей ввода
    ACCENT_COLOR = "#a8c686"      # Мягкий зелёный (для акцентов)

    # Настройка темы
    style.theme_use("clam")  # Используем тему "clam" для гибкости

    # Стиль для основного окна
    style.configure("TFrame", background=BG_COLOR)

    # Стиль для вкладок (Notebook)
    style.configure("TNotebook", background=BG_COLOR)
    style.configure("TNotebook.Tab",
                    padding=[15, 8],
                    background="#e8dcc0",  # Светло-бежевый
                    foreground=TEXT_COLOR,
                    font=("Arial", 10))
    style.map("TNotebook.Tab",
              background=[("selected", BTN_COLOR)],  # Активная вкладка
              foreground=[("selected", "white")])

    # Стиль для кнопок
    style.configure("TButton",
                    background=BTN_COLOR,
                    foreground="white",
                    borderwidth=1,
                    focusthickness=3,
                    focuscolor=BTN_HOVER,
                    font=("Arial", 10, "bold"),
                    padding=10,
                    borderradius=5)  # Округлые углы (если поддерживается)
    style.map("TButton",
              background=[("active", BTN_HOVER)],  # Цвет при наведении
              foreground=[("active", "white")])

    # Стиль для меток (Label)
    style.configure("TLabel",
                    background=BG_COLOR,
                    foreground=TEXT_COLOR,
                    font=("Arial", 10),
                    padding=5)

    # Стиль для полей ввода (Entry)
    style.configure("TEntry",
                    fieldbackground=ENTRY_COLOR,
                    foreground=TEXT_COLOR,
                    insertcolor=TEXT_COLOR,
                    padding=8,
                    font=("Arial", 10),
                    borderwidth=1,
                    relief="solid")

    # Стиль для Combobox
    style.configure("TCombobox",
                    fieldbackground=ENTRY_COLOR,
                    foreground=TEXT_COLOR,
                    padding=8,
                    font=("Arial", 10),
                    arrowcolor=TEXT_COLOR)

    # Стиль для текстового поля (Text)
    style.configure("TText",
                    background=ENTRY_COLOR,
                    foreground=TEXT_COLOR,
                    padding=10,
                    font=("Arial", 10),
                    borderwidth=1,
                    relief="solid")

    return style