import tkinter as tk
from tkinter import ttk, messagebox
from analysis import analyse
from data import amino_acids
from visualization import plot_amino_acid_distribution, plot_mass_share, plot_hydrophobicity
from styles import configure_styles  # Импортируем стили

class AminoAcidAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализ аминокислотных последовательностей")
        self.root.geometry("900x700")  # Увеличиваем размер окна
        self.root.resizable(False, False)  # Запрещаем изменение размера

        # Применяем стили
        self.style = configure_styles()
        self.root.configure(bg="#f0f0f0")  # Фон окна

        self.sequence_data = {}

        self.create_widgets()

    def create_widgets(self):
        # Главный контейнер с отступами
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Вкладки (Notebook)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Вкладка "Анализ"
        self.analysis_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.analysis_tab, text="Анализ")

        # Вкладка "Сравнение"
        self.comparison_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.comparison_tab, text="Сравнение")

        # Вкладка "Поиск"
        self.search_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.search_tab, text="Поиск")

        # Вкладка "Визуализация"
        self.visualization_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.visualization_tab, text="Визуализация")

        # Настройка вкладок
        self.setup_analysis_tab()
        self.setup_comparison_tab()
        self.setup_search_tab()
        self.setup_visualization_tab()

    def setup_analysis_tab(self):
        # Контейнер для центрирования
        container = ttk.Frame(self.analysis_tab)
        container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Метка и поле ввода
        ttk.Label(container, text="Введите последовательность:").pack(pady=10)
        self.seq_entry = ttk.Entry(container, width=50)
        self.seq_entry.pack(pady=10)

        # Кнопка анализа
        ttk.Button(container, text="Проанализировать", command=self.analyze_sequence).pack(pady=20)

        # Текстовое поле для результатов
        self.result_text = tk.Text(container, height=15, width=70, wrap=tk.WORD)
        self.result_text.pack(pady=10)

    def setup_comparison_tab(self):
        container = ttk.Frame(self.comparison_tab)
        container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Первая последовательность
        ttk.Label(container, text="Первая последовательность:").pack(pady=10)
        self.seq1_entry = ttk.Entry(container, width=50)
        self.seq1_entry.pack(pady=10)

        # Вторая последовательность
        ttk.Label(container, text="Вторая последовательность:").pack(pady=10)
        self.seq2_entry = ttk.Entry(container, width=50)
        self.seq2_entry.pack(pady=10)

        # Кнопка сравнения
        ttk.Button(container, text="Сравнить", command=self.compare_sequences).pack(pady=20)

        # Текстовое поле для результатов
        self.comparison_text = tk.Text(container, height=15, width=70, wrap=tk.WORD)
        self.comparison_text.pack(pady=10)

    def setup_search_tab(self):
        container = ttk.Frame(self.search_tab)
        container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Выбор последовательности
        ttk.Label(container, text="Выберите последовательность:").pack(pady=10)
        self.seq_var = tk.StringVar()
        self.seq_combobox = ttk.Combobox(container, textvariable=self.seq_var, width=47)
        self.seq_combobox.pack(pady=10)

        # Поле для поиска подпоследовательности
        ttk.Label(container, text="Искомая подпоследовательность:").pack(pady=10)
        self.part_entry = ttk.Entry(container, width=50)
        self.part_entry.pack(pady=10)

        # Кнопка поиска
        ttk.Button(container, text="Найти", command=self.search_subsequence).pack(pady=20)

        # Текстовое поле для результатов
        self.search_text = tk.Text(container, height=15, width=70, wrap=tk.WORD)
        self.search_text.pack(pady=10)

    def update_search_combobox(self):
        """Обновляет Combobox в вкладке 'Поиск' доступными последовательностями."""
        self.seq_combobox['values'] = list(self.sequence_data.keys())
        if self.sequence_data:
            self.seq_combobox.current(0)

    def analyze_sequence(self):
        seq = self.seq_entry.get().upper()
        if not seq:
            messagebox.showerror("Ошибка", "Введите последовательность!")
            return

        result = analyse(seq)
        self.sequence_data[seq] = result  # Сохраняем в словарь

        # Обновляем Combobox в вкладке "Поиск"
        self.update_search_combobox()

        # Вывод результатов
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Последовательность: {seq}\n")
        self.result_text.insert(tk.END, f"Общая масса: {result['total_mass']:.2f}\n")
        self.result_text.insert(tk.END, f"Количество аминокислот: {result['total_amino']}\n")
        self.result_text.insert(tk.END, f"Изоэлектрическая точка (pI): {result['pi']}\n")
        self.result_text.insert(tk.END, f"Список аминокислот: {', '.join(result['aminos'])}\n")

    def compare_sequences(self):
        seq1 = self.seq1_entry.get().upper()
        seq2 = self.seq2_entry.get().upper()

        if not seq1 or not seq2:
            messagebox.showerror("Ошибка", "Введите обе последовательности!")
            return

        result1 = analyse(seq1)
        result2 = analyse(seq2)

        general = list(set(result1['aminos']) & set(result2['aminos']))
        uniq1 = list(set(result1['aminos']) - set(result2['aminos']))
        uniq2 = list(set(result2['aminos']) - set(result1['aminos']))

        # Вывод результатов
        self.comparison_text.delete(1.0, tk.END)
        self.comparison_text.insert(tk.END, f"Общие аминокислоты: {', '.join(general)}\n")
        self.comparison_text.insert(tk.END, f"Уникальные для первой: {', '.join(uniq1)}\n")
        self.comparison_text.insert(tk.END, f"Уникальные для второй: {', '.join(uniq2)}\n")

    def search_subsequence(self):

        if not self.sequence_data:
            messagebox.showerror("Ошибка", "Сначала проанализируйте хотя бы одну последовательность!")
            return

        seq = self.seq_var.get().upper()
        part = self.part_entry.get().upper()

        if not seq or not part:
            messagebox.showerror("Ошибка", "Выберите последовательность и введите подпоследовательность!")
            return

        if seq not in self.sequence_data:
            messagebox.showerror("Ошибка", "Эта последовательность не была проанализирована!")
            return

        result = analyse(seq, find_part=part)
        self.sequence_data[seq] = result  # Обновляем данные

        # Вывод результатов
        self.search_text.delete(1.0, tk.END)
        self.search_text.insert(tk.END, f"Позиции вхождения: {result['positions']}\n")

    def setup_visualization_tab(self):
        container = ttk.Frame(self.visualization_tab)
        container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

        # Кнопки для выбора типа графика
        ttk.Label(container, text="Выберите тип визуализации:").pack(pady=10)

        btn_frame = ttk.Frame(container)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Распределение аминокислот", command=lambda: self.show_plot("distribution")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Массовая доля", command=lambda: self.show_plot("mass_share")).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Гидрофобность", command=lambda: self.show_plot("hydrophobicity")).pack(side=tk.LEFT, padx=5)

        # Контейнер для графиков
        self.plot_container = ttk.Frame(container)
        self.plot_container.pack(fill=tk.BOTH, expand=True)

    # Добавляем метод show_plot()
    def show_plot(self, plot_type):
        """Отображает выбранный график."""
        # Очищаем контейнер
        for widget in self.plot_container.winfo_children():
            widget.destroy()

        # Если нет проанализированных последовательностей
        if not self.sequence_data:
            messagebox.showerror("Ошибка", "Сначала проанализируйте последовательность!")
            return

        # Получаем последнюю проанализированную последовательность
        seq = next(iter(self.sequence_data.keys()))

        # Строим график в зависимости от типа
        if plot_type == "distribution":
            plot_amino_acid_distribution(seq, self.plot_container)
        elif plot_type == "mass_share":
            plot_mass_share(seq, self.plot_container)
        elif plot_type == "hydrophobicity":
            plot_hydrophobicity(seq, self.plot_container)