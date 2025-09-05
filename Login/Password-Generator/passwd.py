import random
import string
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def rastgele_sifre_olustur(uzunluk):
    karakterler = string.ascii_letters + string.digits  # Özel karakterler kaldırıldı
    return ''.join(random.choice(karakterler) for _ in range(uzunluk))

def sifreyi_goster(event):
    uzunluk = uzunluk_cubugu.get()
    sifre = rastgele_sifre_olustur(uzunluk)
    sifre_label.config(text=f"Oluşturulan Şifre: {sifre}")

def sifre_olustur_ve_kaydet():
    uzunluk = uzunluk_cubugu.get()
    sifre = rastgele_sifre_olustur(uzunluk)
    tarih_saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bilgi = bilgi_giris.get()
    dosya_adi = "sifreler.txt"
    
    with open(dosya_adi, "a") as dosya:
        dosya.write(f"{tarih_saat} - {sifre} - {bilgi}\n")
    
    messagebox.showinfo("Başarılı", f"Şifre oluşturuldu ve {dosya_adi} dosyasına kaydedildi!")

# Arayüz oluşturma
root = tk.Tk()
root.title("Rastgele Şifre Oluşturucu")
root.geometry("500x350")
root.configure(bg="#2c3e50")

etiket = tk.Label(root, text="Şifre Uzunluğunu Seçin:", fg="white", bg="#2c3e50", font=("Arial", 12, "bold"))
etiket.pack(pady=10)

uzunluk_cubugu = tk.Scale(root, from_=8, to=40, orient=tk.HORIZONTAL, length=300, bg="#34495e", fg="white", highlightbackground="#2c3e50")
uzunluk_cubugu.pack(pady=5)
uzunluk_cubugu.bind("<B1-Motion>", sifreyi_goster)  # Sadece sürüklenirken güncellenecek
uzunluk_cubugu.set(8)  # Başlangıçta minimum uzunlukta bir şifre göster

# İlk şifreyi oluştur ve göster
sifre_label = tk.Label(root, text=f"Oluşturulan Şifre: {rastgele_sifre_olustur(8)}", fg="white", bg="#2c3e50", font=("Arial", 12, "bold"))
sifre_label.pack(pady=5)

bilgi_etiket = tk.Label(root, text="Şifre Hakkında Bilgi Girin:", fg="white", bg="#2c3e50", font=("Arial", 12, "bold"))
bilgi_etiket.pack(pady=5)

bilgi_giris = tk.Entry(root, width=40, font=("Arial", 12))
bilgi_giris.pack(pady=5)

buton = tk.Button(root, text="Şifre Oluştur ve Kaydet", command=sifre_olustur_ve_kaydet, bg="#27ae60", fg="white", font=("Arial", 12, "bold"), padx=10, pady=5)
buton.pack(pady=15)

root.mainloop()