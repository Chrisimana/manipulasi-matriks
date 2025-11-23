import tkinter as tk
from matriks_operations import MatriksOperations
from history_manager import HistoryManager
from gui import MatriksGUI

# Fungsi utama program
def main():
    # Inisialisasi komponen
    operations = MatriksOperations()
    history = HistoryManager()
    
    # Buat GUI
    root = tk.Tk()
    app = MatriksGUI(root, operations, history)
    
    # Jalankan aplikasi
    root.mainloop()

if __name__ == "__main__":
    main()