import tkinter as tk
from tkinter import ttk

def configure_styles():
    """Настройка стилей для Tkinter (округлые рамки, цвета, шрифты)."""
    style = ttk.Style()

    # Основные цвета
    BG_COLOR = "#f0f0f0"  # Светло-серый фон
    BTN_COLOR = "#4a7a8c"  # Синий цвет для кнопок
    TEXT_COLOR = "#333333"  # Тёмный текст
    ENTRY_COLOR = "#ffffff"  # Белый фон для полей ввода

    # Настройка стиля для основного окна
    style.theme_use("clam")  # Используем тему "clam" для гибкости

    # Стиль для вкладок (Notebook)
    style.configure("TNotebook", background=BG_COLOR)
    style.configure("TNotebook.Tab", padding=[10, 5], background="#e0e0e0", foreground=TEXT_COLOR)
    style.map("TNotebook.Tab", background=[("selected", BTN_COLOR)], foreground=[("selected", "white")])

    # Стиль для кнопок
    style.configure("TButton",
                    background=BTN_COLOR,
                    foreground="white",
                    borderwidth=1,
                    focusthickness=3,
                    focuscolor="#2a4a5c",
                    font=("Arial", 10, "bold"),
                    padding=10)
    style.map("TButton",
              background=[("active", "#3a6a7c")],  # Цвет при наведении
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
                    padding=5,
                    font=("Arial", 10))

    # Стиль для Combobox
    style.configure("TCombobox",
                    fieldbackground=ENTRY_COLOR,
                    foreground=TEXT_COLOR,
                    padding=5,
                    font=("Arial", 10))

    # Стиль для текстового поля (Text)
    style.configure("TText",
                    background=ENTRY_COLOR,
                    foreground=TEXT_COLOR,
                    padding=10,
                    font=("Arial", 10))

    return style