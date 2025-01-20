# Check IP Domain 

**Check IP Domain** adalah alat sederhana berbasis Python untuk melakukan resolusi domain ke alamat IP. Alat ini dirancang untuk menampilkan hasil di terminal atau menyimpannya ke file. Cocok untuk keperluan monitoring, analisis jaringan, atau pengujian di lingkungan keamanan seperti Kali Linux.

## Fitur

- Resolusi IP dari satu domain atau daftar domain dalam file.
- Menampilkan hasil di terminal dalam format: `example.com: IP`.
- Menyimpan hasil ke file dalam format IP saja.
- Dukungan untuk penanganan kesalahan jika domain tidak valid.

## Cara Instalasi

1. **Clone Repositori**
   ```bash
   git clone https://github.com/<username>/<repository-name>.git
   cd <repository-name>
   ```
2. **Berikan Izin Eksekusi**
   ```bash
   chmod +x check_ip.py
   ```
3. **Pindahkan ke Direktori Global Agar dapat digunakan sebagai perintah di mana saja:**
    ```bash
   sudo mv check_ip.py /usr/local/bin/check_ip
   ```

## Cara Penggunaan

1. **Untuk Satu Domain:**
   ```bash
   check_ip example.com
   ```
2. **Untuk Daftar Domain:**
   ```bash
   check_ip domains.txt
   ```
3. **Dengan Output ke File:**
   ```bash
   check_ip example.com results.txt
   ```
4. **Untuk menampilkan bantuan:**
   ```bash
   check_ip -h
   ```
   
## Contoh Output
- Di Terminal
```bash
==================================================
             Check IP Domain               
==================================================

Hasil:
example.com: 93.184.216.34
google.com: 142.250.190.78
invalid-domain: Invalid domain
```

- Output ke File (results.txt)
```bash
93.184.216.34
142.250.190.78
```

## Kebutuhan Sistem
- Python 3.x
- OS: Linux/Unix (termasuk Kali Linux) atau Windows dengan terminal yang mendukung ANSI.
