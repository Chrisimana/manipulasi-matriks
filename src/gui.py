import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class MatriksGUI:
    def __init__(self, root, operations, history):
        self.root = root
        self.operations = operations
        self.history = history
        
        self.matriks_a = []
        self.matriks_b = []
        self.matriks_hasil = []
        
        self.setup_gui()
    
    def setup_gui(self):
        self.root.title("Manipulasi Matriks")
        self.root.geometry("1000x700")
        self.root.configure(bg='#2c3e50')
        
        # Style configuration
        style = ttk.Style()
        style.configure('TFrame', background='#2c3e50')
        style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10), padding=5)
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        
        # Header
        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10)
        
        title_label = ttk.Label(header_frame, text="MANIPULASI MATRIKS", style='Header.TLabel')
        title_label.pack()
        
        # Main container
        main_container = ttk.Frame(self.root)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left frame - Controls
        left_frame = ttk.Frame(main_container)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Right frame - Display
        right_frame = ttk.Frame(main_container)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.setup_controls(left_frame)
        self.setup_display(right_frame)
    
    # Setup panel kontrol
    def setup_controls(self, parent):
        # Matriks A controls
        a_frame = ttk.LabelFrame(parent, text="Matriks A", padding=10)
        a_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(a_frame, text="Baris:").grid(row=0, column=0, sticky=tk.W)
        self.a_baris = ttk.Entry(a_frame, width=10)
        self.a_baris.grid(row=0, column=1, padx=5)
        
        ttk.Label(a_frame, text="Kolom:").grid(row=0, column=2, sticky=tk.W)
        self.a_kolom = ttk.Entry(a_frame, width=10)
        self.a_kolom.grid(row=0, column=3, padx=5)
        
        ttk.Button(a_frame, text="Buat Matriks A", 
                  command=self.buat_matriks_a).grid(row=0, column=4, padx=5)
        
        # Matriks B controls
        b_frame = ttk.LabelFrame(parent, text="Matriks B", padding=10)
        b_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(b_frame, text="Baris:").grid(row=0, column=0, sticky=tk.W)
        self.b_baris = ttk.Entry(b_frame, width=10)
        self.b_baris.grid(row=0, column=1, padx=5)
        
        ttk.Label(b_frame, text="Kolom:").grid(row=0, column=2, sticky=tk.W)
        self.b_kolom = ttk.Entry(b_frame, width=10)
        self.b_kolom.grid(row=0, column=3, padx=5)
        
        ttk.Button(b_frame, text="Buat Matriks B", 
                  command=self.buat_matriks_b).grid(row=0, column=4, padx=5)
        
        # Operations frame
        ops_frame = ttk.LabelFrame(parent, text="Operasi Matriks", padding=10)
        ops_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(ops_frame, text="A + B (Penjumlahan)", 
                  command=self.tambah_matriks).pack(fill=tk.X, pady=2)
        ttk.Button(ops_frame, text="A - B (Pengurangan)", 
                  command=self.kurangi_matriks).pack(fill=tk.X, pady=2)
        ttk.Button(ops_frame, text="A × B (Perkalian)", 
                  command=self.kali_matriks).pack(fill=tk.X, pady=2)
        ttk.Button(ops_frame, text="Transpose A", 
                  command=self.transpose_a).pack(fill=tk.X, pady=2)
        ttk.Button(ops_frame, text="Transpose B", 
                  command=self.transpose_b).pack(fill=tk.X, pady=2)
        
        # Edit frame
        edit_frame = ttk.LabelFrame(parent, text="Edit Nilai", padding=10)
        edit_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(edit_frame, text="Edit Matriks A", 
                  command=self.edit_matriks_a).pack(fill=tk.X, pady=2)
        ttk.Button(edit_frame, text="Edit Matriks B", 
                  command=self.edit_matriks_b).pack(fill=tk.X, pady=2)
        
        # History frame
        hist_frame = ttk.LabelFrame(parent, text="History", padding=10)
        hist_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(hist_frame, text="Tampilkan History", 
                  command=self.tampilkan_history).pack(fill=tk.X, pady=2)
        ttk.Button(hist_frame, text="Hapus History", 
                  command=self.hapus_history).pack(fill=tk.X, pady=2)
        
        # Visualization frame
        viz_frame = ttk.LabelFrame(parent, text="Visualisasi", padding=10)
        viz_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(viz_frame, text="Visualisasi Matriks A", 
                  command=lambda: self.visualisasi_matriks(self.matriks_a, "Matriks A")).pack(fill=tk.X, pady=2)
        ttk.Button(viz_frame, text="Visualisasi Matriks B", 
                  command=lambda: self.visualisasi_matriks(self.matriks_b, "Matriks B")).pack(fill=tk.X, pady=2)
    
    # Setup panel display
    def setup_display(self, parent):
        # Text area for matrix display
        self.text_display = scrolledtext.ScrolledText(parent, width=50, height=20, font=('Courier', 10))
        self.text_display.pack(fill=tk.BOTH, expand=True)
        
        # Status bar
        self.status_var = tk.StringVar(value="Siap menggunakan program matriks...")
        status_bar = ttk.Label(parent, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(fill=tk.X, pady=5)
    
    # Update text display
    def update_display(self, content):
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(1.0, content)
    
    # Membuat matriks A
    def buat_matriks_a(self):
        try:
            baris = int(self.a_baris.get())
            kolom = int(self.a_kolom.get())
            
            if baris <= 0 or kolom <= 0:
                messagebox.showerror("Error", "Jumlah baris dan kolom harus positif!")
                return
            
            self.matriks_a = self.operations.buat_matriks(baris, kolom)
            self.update_display(self.operations.format_matriks(self.matriks_a, "Matriks A"))
            self.status_var.set(f"Matriks A ({baris}x{kolom}) berhasil dibuat!")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan harus berupa bilangan bulat!")
    
    # Membuat matriks B
    def buat_matriks_b(self):
        try:
            baris = int(self.b_baris.get())
            kolom = int(self.b_kolom.get())
            
            if baris <= 0 or kolom <= 0:
                messagebox.showerror("Error", "Jumlah baris dan kolom harus positif!")
                return
            
            self.matriks_b = self.operations.buat_matriks(baris, kolom)
            self.update_display(self.operations.format_matriks(self.matriks_b, "Matriks B"))
            self.status_var.set(f"Matriks B ({baris}x{kolom}) berhasil dibuat!")
            
        except ValueError:
            messagebox.showerror("Error", "Masukkan harus berupa bilangan bulat!")
    
    # Menjumlahkan matriks A dan B
    def tambah_matriks(self):
        try:
            hasil = self.operations.tambah_matriks(self.matriks_a, self.matriks_b)
            self.matriks_hasil = hasil
            
            display_text = self.operations.format_matriks(self.matriks_a, "Matriks A")
            display_text += self.operations.format_matriks(self.matriks_b, "Matriks B")
            display_text += self.operations.format_matriks(hasil, "Hasil A + B")
            
            self.update_display(display_text)
            self.history.simpan_operasi("Penjumlahan A + B", self.matriks_a, self.matriks_b, hasil)
            self.status_var.set("Penjumlahan matriks berhasil!")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    # Mengurangkan matriks A dan B
    def kurangi_matriks(self):
        try:
            hasil = self.operations.kurangi_matriks(self.matriks_a, self.matriks_b)
            self.matriks_hasil = hasil
            
            display_text = self.operations.format_matriks(self.matriks_a, "Matriks A")
            display_text += self.operations.format_matriks(self.matriks_b, "Matriks B")
            display_text += self.operations.format_matriks(hasil, "Hasil A - B")
            
            self.update_display(display_text)
            self.history.simpan_operasi("Pengurangan A - B", self.matriks_a, self.matriks_b, hasil)
            self.status_var.set("Pengurangan matriks berhasil!")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    # Mengalikan matriks A dan B
    def kali_matriks(self):
        try:
            hasil = self.operations.kali_matriks(self.matriks_a, self.matriks_b)
            self.matriks_hasil = hasil
            
            display_text = self.operations.format_matriks(self.matriks_a, "Matriks A")
            display_text += self.operations.format_matriks(self.matriks_b, "Matriks B")
            display_text += self.operations.format_matriks(hasil, "Hasil A × B")
            
            self.update_display(display_text)
            self.history.simpan_operasi("Perkalian A × B", self.matriks_a, self.matriks_b, hasil)
            self.status_var.set("Perkalian matriks berhasil!")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    # Transpose matriks A
    def transpose_a(self):
        if not self.matriks_a:
            messagebox.showerror("Error", "Matriks A belum dibuat!")
            return
        
        hasil = self.operations.transpose_matriks(self.matriks_a)
        self.matriks_hasil = hasil
        
        display_text = self.operations.format_matriks(self.matriks_a, "Matriks A (Original)")
        display_text += self.operations.format_matriks(hasil, "Matriks A (Transpose)")
        
        self.update_display(display_text)
        self.history.simpan_operasi("Transpose A", self.matriks_a, None, hasil)
        self.status_var.set("Transpose matriks A berhasil!")
    
    # Transpose matriks B
    def transpose_b(self):
        if not self.matriks_b:
            messagebox.showerror("Error", "Matriks B belum dibuat!")
            return
        
        hasil = self.operations.transpose_matriks(self.matriks_b)
        self.matriks_hasil = hasil
        
        display_text = self.operations.format_matriks(self.matriks_b, "Matriks B (Original)")
        display_text += self.operations.format_matriks(hasil, "Matriks B (Transpose)")
        
        self.update_display(display_text)
        self.history.simpan_operasi("Transpose B", self.matriks_b, None, hasil)
        self.status_var.set("Transpose matriks B berhasil!")
    
    # Membuka window edit untuk matriks A
    def edit_matriks_a(self):
        if not self.matriks_a:
            messagebox.showerror("Error", "Matriks A belum dibuat!")
            return
        self.buka_window_edit(self.matriks_a, "Matriks A")
    
    # Membuka window edit untuk matriks B
    def edit_matriks_b(self):
        if not self.matriks_b:
            messagebox.showerror("Error", "Matriks B belum dibuat!")
            return
        self.buka_window_edit(self.matriks_b, "Matriks B")
    
    # Membuka window untuk mengedit matriks
    def buka_window_edit(self, matriks, nama):
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit {nama}")
        edit_window.geometry("500x400")
        
        # Frame untuk input
        input_frame = ttk.Frame(edit_window)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Buat entry untuk setiap elemen matriks
        entries = []
        for i in range(len(matriks)):
            row_entries = []
            for j in range(len(matriks[0])):
                entry = ttk.Entry(input_frame, width=8)
                entry.insert(0, str(matriks[i][j]))
                entry.grid(row=i, column=j, padx=2, pady=2)
                row_entries.append(entry)
            entries.append(row_entries)
        
        # Menyimpan perubahan nilai matriks
        def simpan_perubahan():
            try:
                for i in range(len(matriks)):
                    for j in range(len(matriks[0])):
                        matriks[i][j] = float(entries[i][j].get())
                
                self.update_display(self.operations.format_matriks(matriks, nama))
                self.status_var.set(f"{nama} berhasil diupdate!")
                edit_window.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Masukkan harus berupa angka!")
        
        # Tombol simpan
        ttk.Button(edit_window, text="Simpan Perubahan", 
                  command=simpan_perubahan).pack(pady=10)
    
    # Menampilkan history operasi
    def tampilkan_history(self):
        history_text = self.history.tampilkan_history()
        self.update_display(history_text)
        self.status_var.set("History operasi ditampilkan")
    
    # Menghapus history operasi
    def hapus_history(self):
        result = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus semua history?")
        if result:
            message = self.history.hapus_history()
            self.status_var.set(message)
    
    # Menampilkan visualisasi matriks menggunakan matplotlib
    def visualisasi_matriks(self, matriks, nama):
        if not matriks:
            messagebox.showerror("Error", f"{nama} belum dibuat!")
            return
        
        # Konversi ke numpy array untuk visualisasi
        np_matriks = np.array(matriks)
        
        # Buat figure
        fig = Figure(figsize=(6, 5))
        ax = fig.add_subplot(111)
        
        # Buat heatmap
        cax = ax.matshow(np_matriks, cmap='viridis')
        fig.colorbar(cax)
        
        # Tambahkan nilai di setiap sel
        for i in range(len(matriks)):
            for j in range(len(matriks[0])):
                ax.text(j, i, f'{matriks[i][j]:.1f}', ha='center', va='center', 
                       color='white' if matriks[i][j] > np_matriks.max()/2 else 'black')
        
        ax.set_title(f'Visualisasi {nama}')
        ax.set_xlabel('Kolom')
        ax.set_ylabel('Baris')
        
        # Tampilkan di window baru
        viz_window = tk.Toplevel(self.root)
        viz_window.title(f"Visualisasi {nama}")
        
        canvas = FigureCanvasTkAgg(fig, master=viz_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)