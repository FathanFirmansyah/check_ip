#!/usr/bin/env python3

import socket
import sys
import os

# Warna ANSI
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Header
def print_header():
    print(f"{GREEN}{'=' * 50}")
    print(f"{'Check IP Domain by SOC'.center(50)}")
    print(f"{'=' * 50}{RESET}")

# Fungsi untuk mendapatkan IP dari domain
def get_ip_from_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return None

# Fungsi untuk menampilkan bantuan
def print_help():
    print_header()
    print(f"{YELLOW}Usage:{RESET}")
    print(f"  check_ip <domain> [output_file]       # Untuk satu domain")
    print(f"  check_ip <file.txt> [output_file]    # Untuk daftar domain dari file")
    print(f"\n{YELLOW}Options:{RESET}")
    print(f"  -h, --help              # Menampilkan bantuan ini")
    print(f"  [output_file]           # (Opsional) Nama file untuk menyimpan hasil")
    print("\nExamples:")
    print(f"  check_ip example.com                  # Output ke terminal")
    print(f"  check_ip example.com results.txt      # Output ke file")
    print(f"  check_ip domains.txt                  # Output ke terminal")
    print(f"  check_ip domains.txt results.txt      # Output ke file")
    sys.exit(0)

# Fungsi utama
def main():
    # Header
    print_header()

    # Cek jumlah argumen
    if len(sys.argv) < 2:
        print(f"{RED}[Error] Argumen tidak valid.{RESET}")
        print(f"Gunakan opsi {YELLOW}-h{RESET} atau {YELLOW}--help{RESET} untuk bantuan.\n")
        sys.exit(1)

    input_arg = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) == 3 else None

    terminal_results = []  # Untuk hasil terminal
    file_results = []      # Untuk hasil file

    # Jika argumen adalah file
    if os.path.isfile(input_arg):
        try:
            with open(input_arg, "r") as file:
                domains = file.readlines()
            for domain in domains:
                domain = domain.strip()
                if domain:
                    ip = get_ip_from_domain(domain)
                    if ip:
                        terminal_results.append(f"{domain}: {ip}")
                        file_results.append(ip)
                    else:
                        terminal_results.append(f"{domain}: Invalid domain")
                        file_results.append("Invalid Domain")
        except Exception as e:
            print(f"{RED}[Error] Tidak dapat membaca file: {e}{RESET}")
            sys.exit(1)
    else:
        # Menganggap argumen sebagai domain
        domain = input_arg.strip()
        ip = get_ip_from_domain(domain)
        if ip:
            terminal_results.append(f"{domain}: {ip}")
            file_results.append(ip)
        else:
            terminal_results.append(f"{domain}: Invalid domain")
            file_results.append("Invalid Domain")

    # Output ke terminal
    print("\nHasil:")
    for result in terminal_results:
        print(f"{GREEN}{result}{RESET}")

    # Output ke file jika diminta
    if output_file:
        try:
            with open(output_file, "w") as file:
                file.write("\n".join(file_results) + "\n")
            print(f"\n{GREEN}Hasil disimpan ke file: {output_file}{RESET}")
        except Exception as e:
            print(f"{RED}[Error] Tidak dapat menyimpan ke file: {e}{RESET}")

if __name__ == "__main__":
    # Menangani opsi -h atau --help
    if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
        print_help()
    main()
