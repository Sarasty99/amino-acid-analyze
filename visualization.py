import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data import amino_acids
import numpy as np
from tkinter import ttk, messagebox
import tkinter as tk
from analysis import calculate_gravy, find_amyloid_regions

def plot_amino_acid_distribution(seq, parent_frame):
    """Строит гистограмму распределения аминокислот (игнорирует неизвестные)."""
    counts = {aa: 0 for aa in amino_acids.keys()}
    for residue in seq:
        if residue in counts:
            counts[residue] += 1
        else:
            print(f"Пропущена неизвестная аминокислота: {residue}")

    labels = [amino_acids[aa].name for aa in counts.keys()]
    values = list(counts.values())

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color="#d4a574")
    ax.set_title("Распределение аминокислот", fontsize=12, fontweight="bold")
    ax.set_xlabel("Аминокислоты", fontsize=10)
    ax.set_ylabel("Количество", fontsize=10)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def plot_mass_share(seq, parent_frame):
    """Строит круговую диаграмму массовой доли (игнорирует неизвестные)."""
    total_mass = 0
    mass_shares = {}

    for aa in set(seq):
        if aa in amino_acids:
            mass_shares[aa] = amino_acids[aa].mass * seq.count(aa)
            total_mass += mass_shares[aa]
        else:
            print(f"Пропущена неизвестная аминокислота: {aa}")

    if not mass_shares:
        messagebox.showerror("Ошибка", "Нет известных аминокислот для анализа!")
        return

    mass_shares = {aa: (mass_shares[aa] * 100) / total_mass for aa in mass_shares}
    labels = [f"{amino_acids[aa].name} ({mass_shares[aa]:.1f}%)" for aa in mass_shares.keys()]
    values = list(mass_shares.values())

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=plt.cm.Pastel1.colors)
    ax.set_title("Массовая доля аминокислот", fontsize=12, fontweight="bold")
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def plot_hydrophobicity(seq, parent_frame):
    """Строит столбчатую диаграмму гидрофобности (игнорирует неизвестные)."""
    hydrophobic = ["G", "A", "V", "L", "I", "M", "F", "W", "P"]
    hydrophilic = ["S", "T", "C", "Y", "N", "Q", "D", "E", "K", "R", "H"]

    hydro_count = 0
    philic_count = 0
    unknown_count = 0

    for aa in seq:
        if aa in hydrophobic:
            hydro_count += 1
        elif aa in hydrophilic:
            philic_count += 1
        else:
            unknown_count += 1
            print(f"Пропущена неизвестная аминокислота: {aa}")

    labels = ["Гидрофобные", "Гидрофильные", "Неизвестные"]
    values = [hydro_count, philic_count, unknown_count]
    colors = ["#d4a574", "#a8c686", "#e0e0e0"]

    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(labels, values, color=colors)
    ax.set_title("Гидрофобность/Гидрофильность", fontsize=12, fontweight="bold")
    ax.set_ylabel("Количество аминокислот", fontsize=10)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def plot_gravy(seq, parent_frame):
    """График GRAVY для окна скольжения"""
    window_size = 7
    gravy_values = []

    for i in range(len(seq) - window_size + 1):
        window = seq[i:i+window_size]
        gravy = calculate_gravy(window)
        gravy_values.append(gravy)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(range(1, len(gravy_values)+1), gravy_values, color="#d4a574")
    ax.axhline(y=0, color='gray', linestyle='--')
    ax.set_title("GRAVY по окну скольжения", fontsize=12, fontweight="bold")
    ax.set_xlabel("Позиция", fontsize=10)
    ax.set_ylabel("GRAVY", fontsize=10)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def plot_amyloid_regions(seq, parent_frame):
    """Визуализация амилоидных участков"""
    regions = find_amyloid_regions(seq)
    if not regions:
        messagebox.showinfo("Информация", "Амилоидные участки не найдены")
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    for start, end, _ in regions:
        ax.axvspan(start, end, color='red', alpha=0.3)

    ax.set_title("Амилоидные участки", fontsize=12, fontweight="bold")
    ax.set_xlabel("Позиция в последовательности", fontsize=10)
    ax.set_ylim(0, 1)
    plt.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    