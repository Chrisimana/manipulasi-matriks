# 🧮 Manipulasi Matriks

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange)

**Aplikasi manipulasi matriks canggih dengan GUI modern, sistem history**

</div>

## 📋 Daftar Isi

- [Gambaran Umum](#-gambaran-umum)
- [Fitur](#-fitur)
- [Instalasi](#-instalasi)
- [Penggunaan](#-penggunaan)
- [Dokumentasi](#-dokumentasi)
- [Contoh Penggunaan](#-contoh-penggunaan)
- [FAQ](#-faq)

## 🚀 Gambaran Umum

**Manipulasi Matriks** adalah aplikasi komprehensif untuk operasi matriks yang dibangun dengan Python. Aplikasi ini menawarkan interface grafis modern, visualisasi data, sistem penyimpanan history, dan berbagai operasi matriks yang powerful.

### ✨ Highlights

- 🎨 **GUI Modern** dengan tema dark yang professional
- 📊 **Visualisasi Matriks** dengan heatmap interaktif
- 💾 **Sistem History** otomatis dengan penyimpanan JSON
- 🧮 **Operasi Lengkap** - penjumlahan, pengurangan, perkalian, transpose
- 🔄 **Edit Real-time** - ubah nilai matriks dengan mudah
- 📈 **Multi-window** - tampilan terpisah untuk setiap fitur

## 🌟 Fitur

### 🧮 Core Operations
- **Penjumlahan Matriks** - Operasi A + B dengan validasi ukuran
- **Pengurangan Matriks** - Operasi A - B 
- **Perkalian Matriks** - Operasi A × B dengan validasi dimensi
- **Transpose Matriks** - Mengubah baris menjadi kolom
- **Pembuatan Matriks** - Buat matriks custom dengan ukuran bebas

### 💾 Data Management
- **Auto-save History** - Setiap operasi tersimpan otomatis
- **JSON Storage** - Format penyimpanan terstruktur
- **History Management** - Lihat dan hapus riwayat operasi
- **Session Management** - Kelola multiple matriks sessions

### 📊 Visualization
- **Heatmap Interaktif** - Visualisasi matriks dengan warna
- **Nilai Cell** - Menampilkan nilai di setiap sel matriks
- **Color Mapping** - Skema warna yang informatif
- **Multiple Windows** - Visualisasi terpisah untuk setiap matriks

### 🎨 GUI Features
- **Dark Theme** - Tema gelap modern dan eye-friendly
- **Responsive Design** - Adaptif berbagai ukuran layar
- **Real-time Updates** - Perubahan nilai langsung terlihat
- **Intuitive Controls** - Interface yang user-friendly
- **Status Bar** - Informasi status operasi

## 📥 Instalasi

### Prerequisites

- Python 3.7 atau lebih tinggi
- pip (Python package manager)

### Dependencies

```txt
matplotlib>=3.5.0
numpy>=1.21.0
tkinter (standard library)
json (standard library)
datetime (standard library)
os (standard library)
```

### Step-by-Step Installation

1. **Download Repository**
   ```bash
   git clone https://github.com/username/program-matriks-super.git
   cd program-matriks-super
   ```

2. **Buat Virtual Environment (Recommended)**
   ```bash
   python -m venv matriks_env
   # Windows
   matriks_env\Scripts\activate
   # Linux/Mac
   source matriks_env/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install matplotlib numpy
   ```

4. **Verifikasi Instalasi**
   ```bash
   python main.py
   ```

### Quick Install (Windows)
```bash
# Download dan ekstrak project
pip install matplotlib numpy
python main.py
```

## 🎮 Penggunaan

### Menjalankan Aplikasi

```bash
python main.py
```

### Basic Workflow

1. **Membuat Matriks**
   - Input jumlah baris dan kolom untuk Matriks A & B
   - Klik "Buat Matriks A" atau "Buat Matriks B"

2. **Edit Nilai Matriks**
   - Klik "Edit Matriks A" atau "Edit Matriks B"
   - Ubah nilai di window edit yang muncul
   - Klik "Simpan Perubahan"

3. **Operasi Matriks**
   - Pilih operasi yang diinginkan:
     - "A + B (Penjumlahan)"
     - "A - B (Pengurangan)" 
     - "A × B (Perkalian)"
     - "Transpose A/B"

4. **Visualisasi**
   - Klik "Visualisasi Matriks A/B" untuk melihat heatmap

### Operasi yang Didukung

| Operasi | Syarat | Hasil |
|---------|---------|--------|
| A + B | Ukuran sama | Matriks dengan ukuran sama |
| A - B | Ukuran sama | Matriks dengan ukuran sama |
| A × B | Kolom A = Baris B | Matriks (baris A × kolom B) |
| Transpose | - | Matriks (kolom × baris) |

### Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| Focus Input | Tab |
| Simpan Edit | Enter |
| Tutup Window | Escape |

## 📚 Dokumentasi

### File Descriptions

| File | Description |
|------|-------------|
| `main.py` | Inisialisasi dan menjalankan aplikasi utama |
| `matriks_operations.py` | Kelas operasi matriks dan utility functions |
| `history_manager.py` | Manajemen penyimpanan dan load history |
| `gui.py` | Interface pengguna dengan Tkinter dan matplotlib |
| `history.json` | Penyimpanan history operasi (auto-generated) |


## 💡 Contoh Penggunaan

### Basic Matriks Operations

```python
# Contoh penggunaan melalui GUI
"""
1. Buat Matriks A: 2x3
   [1, 2, 3]
   [4, 5, 6]

2. Buat Matriks B: 2x3  
   [2, 3, 4]
   [5, 6, 7]

3. A + B = 
   [3, 5, 7]
   [9, 11, 13]

4. Transpose A =
   [1, 4]
   [2, 5] 
   [3, 6]
"""
```

### Advanced Operations

```python
# Perkalian Matriks
"""
Matriks A (2x3):
[1, 2, 3]
[4, 5, 6]

Matriks B (3x2):
[7, 8]
[9, 10]
[11, 12]

A × B =
[58, 64]
[139, 154]
"""
```

### Error Handling Examples

```python
# Validasi ukuran matriks
"""
Penjumlahan matriks 2x3 dengan 3x2:
→ Error: "Ukuran matriks tidak sama!"

Perkalian matriks 2x3 dengan 2x3:
→ Error: "Jumlah kolom matriks A harus sama dengan jumlah baris matriks B!"
"""
```

## ❓ FAQ

### Q: Apakah program ini bisa menangani matriks berukuran besar?
**A:** Ya, program bisa menangani matriks hingga ratusan baris/kolom, tergantung resources komputer.

### Q: Bagaimana cara backup data history?
**A:** Data history tersimpan di `data/history.json`. Backup file ini untuk menyimpan riwayat.

### Q: Apakah support bilangan kompleks?
**A:** Saat ini hanya support bilangan real.

### Q: Bagaimana cara reset semua data?
**A:** Hapus file `data/history.json` dan restart aplikasi.

### Q: Bisakah diintegrasikan dengan Jupyter Notebook?
**A:** Ya, modul `MatriksOperations` bisa diimport langsung di Jupyter.

### Performance Tips

- Untuk matriks besar (>100x100), gunakan visualisasi selectively
- Close visualization windows ketika tidak digunakan
- Restart aplikasi periodically untuk membersihkan memory

---

<div align="center">

### ⭐ Jika project ini membantu, jangan lupa beri bintang! ⭐

**🧮 Happy Matrix Calculating! 🧮**

[Kembali ke Atas](#-manipulasi-matriks)

</div>