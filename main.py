import matplotlib
matplotlib.use("TkAgg")  # Указываем бэкенд для matplotlib

from interface import AminoAcidAnalyzerApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = AminoAcidAnalyzerApp(root)
    root.mainloop()