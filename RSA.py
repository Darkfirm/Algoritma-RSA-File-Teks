import random
import os

# fungsi untuk mencari nilai PBB(a,b)
def pbb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# fungsi untuk mengecek apakah bilangan prima atau tidak
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(n**0.5) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# fungsi untuk mencari nilai invers modulo
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# random p dan q bilangan prima
def generate_pq():
    while True:
        p = random.randrange(1, 1000)
        if isPrime(p):
            break
    while True:
        q = random.randrange(1, 1000)
        if isPrime(q):
            break
    return p, q

# fungsi mereturn kunci publik dan kunci privat
def generate_key(p, q):
    n = p * q
    m = (p - 1) * (q - 1)
    e = random.randrange(1, m)
    g = pbb(e, m)
    while True:
        e = random.randrange(1, m)
        g = pbb(e, m)
        d = mod_inverse(e, m)
        if g == 1 and e != d:
            break
    d = mod_inverse(e, m)
    return (e, n), (d, n)

# fungsi untuk mengenkripsi teks
def encrypt(en, plaintext):
    e, n = en
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# fungsi untuk mendekripsi teks
def decrypt(dn, ciphertext):
    d, n = dn
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

# fungsi utama yang menyatukan semua fungsi
def programUtama():
    print("Pilih tujuan Anda:\n 1. Enkripsi\n 2. Dekripsi")
    pil = int(input("Masukkan pilihan Anda: "))
    while pil not in [1, 2]:
        print("Pilihan tidak valid")
        pil = int(input("Masukkan pilihan Anda: "))
    
    if pil == 1:
        p, q = generate_pq()
        print("Hasil nilai p dan q (bilangan prima):")
        print("p = ", p)
        print("q = ", q)
        public, private = generate_key(p, q)
        print("Kunci publik Anda (tidak bersifat rahasia): ", public)
        print("Kunci privat Anda (mohon simpan dengan baik): ", private)
        print("Pilih input teks Anda:\n 1. File\n 2. Ketik sendiri")
        pil = int(input("Masukkan pilihan Anda: "))
        while pil not in [1, 2]:
            print("Pilihan tidak valid")
            pil = int(input("Masukkan pilihan Anda: "))
        if pil == 1:
            path = os.getcwd()
            files = os.listdir(path + "\\files")
            namafile = input("Masukkan nama file Anda yang terlatak di folder bernama \"files\": ")
            while namafile not in files:
                print("File tidak ditemukan")
                namafile = input("Masukkan nama file Anda yang terlatak di folder bernama \"files\": ")
            namafile = path + "\\files\\" + namafile
            f = open(namafile, "r")
            text = f.read()
            f.close()
            print("Teks yang akan dienkripsi:\n", text)
        else:
            text = input("Masukkan pesan untuk dienkripsi:\n")
        encrypted_text = encrypt(public, text)
        print("Teks hasil enkripsi:\n", ' '.join(str(c) for c in encrypted_text))
    else:
        d = int(input("Masukkan d dalam kunci privat Anda (d,n): "))
        n = int(input("Masukkan n dalam kunci privat Anda (d,n): "))
        private = (d, n)
        pil = int(input("Pilih input teks Anda:\n 1. File\n 2. Ketik sendiri\nMasukkan pilihan Anda: "))
        while pil not in [1, 2]:
            print("Pilihan tidak valid")
            pil = int(input("Masukkan pilihan Anda: "))
        if pil == 1:
            path = os.getcwd()
            files = os.listdir(path + "\\files")
            namafile = input("Masukkan nama file Anda yang terlatak di folder bernama \"files\": ")
            while namafile not in files:
                print("File tidak ditemukan")
                namafile = input("Masukkan nama file Anda yang terlatak di folder bernama \"files\": ")
            namafile = path + "\\files\\" + namafile
            f = open(namafile, "r")
            encrypted_text = f.read()
            f.close()
            print("Teks yang akan didekripsi:\n", encrypted_text)
        else:
            encrypted_text = input("Masukkan pesan hasil enkripsi: ")
        encrypted_text = encrypted_text.split(' ')
        encrypted_text = list(map(int, encrypted_text))
        print("Teks hasil dekripsi :\n", decrypt(private, encrypted_text))

# program utama
if __name__ == '__main__':
    programUtama()
    print("Apakah Anda ingin mengulang program? (y/n)")
    ulang = input("Masukkan pilihan Anda: ")
    while ulang not in ['y', 'n']:
        print("Pilihan tidak valid")
        ulang = input("Masukkan pilihan Anda: ")
    while ulang == 'y':
        print()
        programUtama()
        print("Apakah Anda ingin mengulang program? (y/n)")
        ulang = input("Masukkan pilihan Anda: ")
        while ulang not in ['y', 'n']:
            print("Pilihan tidak valid")
            ulang = input("Masukkan pilihan Anda: ")
    