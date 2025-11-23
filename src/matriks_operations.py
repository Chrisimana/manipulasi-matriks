class MatriksOperations:
    @staticmethod
    # Membuat matriks baru dengan ukuran tertentu
    def buat_matriks(baris, kolom, nilai_default=0):
        return [[nilai_default for _ in range(kolom)] for _ in range(baris)]
    
    @staticmethod
    # Validasi apakah dua matriks memiliki ukuran yang sama
    def validasi_ukuran(matriks_a, matriks_b):
        if not matriks_a or not matriks_b:
            return False
        return len(matriks_a) == len(matriks_b) and len(matriks_a[0]) == len(matriks_b[0])
    
    @staticmethod
    # Menjumlahkan dua matriks
    def tambah_matriks(matriks_a, matriks_b):
        if not MatriksOperations.validasi_ukuran(matriks_a, matriks_b):
            raise ValueError("Ukuran matriks tidak sama!")
        
        hasil = MatriksOperations.buat_matriks(len(matriks_a), len(matriks_a[0]))
        for i in range(len(matriks_a)):
            for j in range(len(matriks_a[0])):
                hasil[i][j] = matriks_a[i][j] + matriks_b[i][j]
        return hasil
    
    @staticmethod
    # Mengurangkan dua matriks
    def kurangi_matriks(matriks_a, matriks_b):
        if not MatriksOperations.validasi_ukuran(matriks_a, matriks_b):
            raise ValueError("Ukuran matriks tidak sama!")
        
        hasil = MatriksOperations.buat_matriks(len(matriks_a), len(matriks_a[0]))
        for i in range(len(matriks_a)):
            for j in range(len(matriks_a[0])):
                hasil[i][j] = matriks_a[i][j] - matriks_b[i][j]
        return hasil
    
    @staticmethod
    # Mengalikan dua matriks
    def kali_matriks(matriks_a, matriks_b):
        if not matriks_a or not matriks_b:
            raise ValueError("Matriks tidak boleh kosong!")
        
        if len(matriks_a[0]) != len(matriks_b):
            raise ValueError("Jumlah kolom matriks A harus sama dengan jumlah baris matriks B!")
        
        hasil = MatriksOperations.buat_matriks(len(matriks_a), len(matriks_b[0]))
        for i in range(len(matriks_a)):
            for j in range(len(matriks_b[0])):
                for k in range(len(matriks_b)):
                    hasil[i][j] += matriks_a[i][k] * matriks_b[k][j]
        return hasil
    
    @staticmethod
    # Mentranspose matriks
    def transpose_matriks(matriks):
        if not matriks:
            return []
        
        baris = len(matriks)
        kolom = len(matriks[0])
        hasil = MatriksOperations.buat_matriks(kolom, baris)
        
        for i in range(baris):
            for j in range(kolom):
                hasil[j][i] = matriks[i][j]
        return hasil
    
    @staticmethod
    # Memformat matriks untuk ditampilkan
    def format_matriks(matriks, nama="Matriks"):
        if not matriks:
            return f"{nama}: Matriks kosong\n"
        
        result = f"{nama} ({len(matriks)}x{len(matriks[0])}):\n"
        for i, baris in enumerate(matriks):
            baris_str = " | ".join(f"{elem:>8.2f}" if isinstance(elem, float) else f"{elem:>8}" for elem in baris)
            result += f"Baris {i + 1:2}: [ {baris_str} ]\n"
        return result