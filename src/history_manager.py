import json
import os
from datetime import datetime

class HistoryManager:
    def __init__(self, filename="data/history.json"):
        self.filename = filename
        self.ensure_directory_exists()
    
    def ensure_directory_exists(self):
        """Memastikan direktori data exists"""
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
    
    def simpan_operasi(self, operasi, matriks_a, matriks_b=None, hasil=None):
        """Menyimpan operasi ke history"""
        history = self.muat_history()
        
        # Format data operasi
        data_operasi = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operasi": operasi,
            "matriks_a": matriks_a,
            "matriks_b": matriks_b,
            "hasil": hasil
        }
        
        history.append(data_operasi)
        
        # Simpan ke file (maksimal 50 operasi terakhir)
        if len(history) > 50:
            history = history[-50:]
        
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    
    def muat_history(self):
        """Memuat history dari file"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def tampilkan_history(self):
        """Menampilkan history operasi"""
        history = self.muat_history()
        if not history:
            return "Belum ada history operasi."
        
        result = "HISTORY OPERASI MATRIKS:\n"
        result += "=" * 60 + "\n"
        
        for i, operasi in enumerate(reversed(history), 1):
            result += f"{i}. {operasi['timestamp']} - {operasi['operasi']}\n"
            if operasi['matriks_a']:
                ukuran_a = f"{len(operasi['matriks_a'])}x{len(operasi['matriks_a'][0])}"
                result += f"   Matriks A ({ukuran_a})\n"
            if operasi['matriks_b']:
                ukuran_b = f"{len(operasi['matriks_b'])}x{len(operasi['matriks_b'][0])}"
                result += f"   Matriks B ({ukuran_b})\n"
            if operasi['hasil']:
                ukuran_h = f"{len(operasi['hasil'])}x{len(operasi['hasil'][0])}"
                result += f"   Hasil ({ukuran_h})\n"
            result += "-" * 40 + "\n"
        
        return result
    
    def hapus_history(self):
        """Menghapus semua history"""
        try:
            os.remove(self.filename)
            return "History berhasil dihapus."
        except FileNotFoundError:
            return "History sudah kosong."