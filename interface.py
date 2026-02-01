import tkinter as tk
from tkinter import ttk, messagebox
from analysis import analyse
from data import amino_acids

sequence_data = {}

def compare_sequences(seq1, seq2):
    result1 = analyse(seq1)
    result2 = analyse(seq2)

    general = list(set(result1['aminos']) & set(result2['aminos']))
    uniq1 = list(set(result1['aminos']) - set(result2['aminos']))
    uniq2 = list(set(result2['aminos']) - set(result1['aminos']))

    print('А/к в обеих цепях:', general)
    print('Уникальные для первой:', uniq1)
    print('Уникальные для второй:', uniq2)

class AminoAcidAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Анализ аминокислотных последовательностей")
        self.root.geometry("800x600")

        self.sequence_data = {}  # Хранение проанализированных последовательностей

        self.create_widgets()

    def create_widgets(self):
        # Главное меню (вкладки)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Вкладка "Анализ"
        self.analysis_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.analysis_tab, text="Анализ")

        # Вкладка "Сравнение"
        self.comparison_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.comparison_tab, text="Сравнение")

        # Вкладка "Поиск"
        self.search_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.search_tab, text="Поиск")

        # Настройка вкладок
        self.setup_analysis_tab()
        self.setup_comparison_tab()
        self.setup_search_tab()

    def setup_analysis_tab(self):
        # Поле для ввода последовательности
        ttk.Label(self.analysis_tab, text="Введите последовательность:").pack(pady=5)
        self.seq_entry = ttk.Entry(self.analysis_tab, width=50)
        self.seq_entry.pack(pady=5)

        # Кнопка анализа
        ttk.Button(self.analysis_tab, text="Проанализировать", command=self.analyze_sequence).pack(pady=10)

        # Поле для вывода результатов
        self.result_text = tk.Text(self.analysis_tab, height=20, width=70)
        self.result_text.pack(pady=10)

    def analyze_sequence(self):
        seq = self.seq_entry.get().upper()
        if not seq:
            messagebox.showerror("Ошибка", "Введите последовательность!")
            return

        result = analyse(seq)
        self.sequence_data[seq] = result
        self.update_search_combobox()

        # Вывод результатов
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Последовательность: {seq}\n")
        self.result_text.insert(tk.END, f"Общая масса: {result['total_mass']:.2f}\n")
        self.result_text.insert(tk.END, f"Количество аминокислот: {result['total_amino']}\n")
        self.result_text.insert(tk.END, f"Изоэлектрическая точка (pI): {result['pi']}\n")
        self.result_text.insert(tk.END, f"Список аминокислот: {', '.join(result['aminos'])}\n")


    def update_search_combobox(self):
        """Обновляет Combobox в вкладке 'Поиск' доступными последовательностями."""
        self.seq_combobox['values'] = list(self.sequence_data.keys())
        if self.sequence_data:
            self.seq_combobox.current(0)  # Выбираем первую последовательность по умолчанию

    def setup_comparison_tab(self):
        # Первая последовательность
        ttk.Label(self.comparison_tab, text="Первая последовательность:").pack(pady=5)
        self.seq1_entry = ttk.Entry(self.comparison_tab, width=50)
        self.seq1_entry.pack(pady=5)

        # Вторая последовательность
        ttk.Label(self.comparison_tab, text="Вторая последовательность:").pack(pady=5)
        self.seq2_entry = ttk.Entry(self.comparison_tab, width=50)
        self.seq2_entry.pack(pady=5)

        # Кнопка сравнения
        ttk.Button(self.comparison_tab, text="Сравнить", command=self.compare_sequences).pack(pady=10)

        # Поле для вывода результатов
        self.comparison_text = tk.Text(self.comparison_tab, height=20, width=70)
        self.comparison_text.pack(pady=10)

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


    def setup_search_tab(self):
        # Выбор последовательности
        ttk.Label(self.search_tab, text="Выберите последовательность:").pack(pady=5)
        self.seq_var = tk.StringVar()
        self.seq_combobox = ttk.Combobox(self.search_tab, textvariable=self.seq_var, width=47)
        self.seq_combobox.pack(pady=5)

        # Поле для поиска подпоследовательности
        ttk.Label(self.search_tab, text="Искомая подпоследовательность:").pack(pady=5)
        self.part_entry = ttk.Entry(self.search_tab, width=50)
        self.part_entry.pack(pady=5)

        # Кнопка поиска
        ttk.Button(self.search_tab, text="Найти", command=self.search_subsequence).pack(pady=10)

        # Поле для вывода результатов
        self.search_text = tk.Text(self.search_tab, height=20, width=70)
        self.search_text.pack(pady=10)

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