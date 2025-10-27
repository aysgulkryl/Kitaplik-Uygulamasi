 #Menü oluşturma fonksiyonu

def menu_ac():
  print("Kitaplık Uygulaması")
  print("\n")
  print("1. Kitap Ara")
  print("2. Kitap Ekle")
  print("3. Kitap Listele")
  print("4. Çıkış")
  print("\n")

# Kitap arama fonksiyonu


def kitap_ara():
    arama = input("Aradığınız kitabın adını giriniz: ").strip().lower()
    print("\n")

    bulundu = False

    try:
        with open("kitaplar.txt", "r", encoding="utf-8") as dosya:
            for satir in dosya:
                kitap_adi_satir = satir.split("|")[0].strip().lower()
                if arama == kitap_adi_satir:
                    bulundu = True
                    print("Aradığınız kitap dosyada bulunmaktadır:\n")
                    print(satir.strip())
                    print("\n")
                    break

            if not bulundu:
                print("Aradığınız kitap dosyada bulunmamaktadır.\n")

    except FileNotFoundError:
        print("Henüz kitap eklenmemiş. Dosya bulunamadı.\n")

# Kitap ekleme fonksiyonu

def kitap_ekle():
  kitap_adi = input("Eklemek istediğiniz kitabın adını giriniz: ").strip()
  print("\n")
  yazar = input("Eklemek istediğiniz kitabın yazarını giriniz: ").strip()
  print("\n")
  tur = input("Eklemek istediğiniz kitabın türünü giriniz: ").strip()
  print("\n")
  yayin_evi = input("Eklemek istediğiniz kitabın yayınevini giriniz: ").strip()
  print("\n")
  basim_yili =input("Eklemek istediğiniz kitabın basım yılını giriniz: ").strip()
  print("\n")

  yeni_kayit = f"{kitap_adi} | {yazar} | {tur} | {yayin_evi} | {basim_yili}"
  print("\n")

  with open ("kitaplar.txt", "a", encoding="utf-8") as dosya:
    dosya.write(yeni_kayit + "\n")

  print("Yeni kitap kaydı eklendi. \n")

# Kitap listeleme fonksiyonu

def kitap_listele():
  print("Kitap Listesi")
  print("\n")

  try:
    with open("kitaplar.txt", "r", encoding="utf-8") as dosya:
      kitaplar = dosya.readlines()
      if not kitaplar:
        print("Henüz kitap eklenmemiş.\n")
      else:
       for satir in kitaplar:
        print(satir.strip())
        print("\n")

  except FileNotFoundError:
    print(" Kitaplar dosyasında kayıt bulunamadı. Lütfen önce kitap ekleyin.")
    print("\n")


# Menü oluşturma

while True:
  menu_ac()
  secim = input("Kitaplık uygulamasına hoşgeldiniz. Lütfen yapmak istediğiniz işlemi seçiniz (1,2,3,4): ")
  print("\n")

  if secim == "1":
    print("Kitap arama işlemi seçildi.")
    print("\n")
    kitap_ara()


  elif secim == "2":
   print("Kitap ekleme işlemi seçildi.")
   print("\n")
   kitap_ekle()


  elif secim == "3":
   print("Kitap listeleme işlemi seçildi.")
   print("\n")
   kitap_listele()

  elif secim == "4":
   print("Çıkış işlemi seçildi. Program sonlandırılıyor...")
   break

  else:
   print("Geçersiz seçim yaptınız. Yapmak istediğiniz işleme göre 1-4 arasında bir sayı seçiniz." )
   print("\n")
