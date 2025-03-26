def atm_menusu():
    print("""
    ATM Ana Menü:
    1. Bakiye Sorgulama
    2. Para Yatırma
    3. Para Çekme
    4. Çıkış
    """)


bakiye = 0  # Başlangıçtaki bakiye

while True:
    atm_menusu()
    try:
        secim = int(input("\nBir işlem seçin (1-4): "))

        if secim == 1:
            # Bakiye sorgulama
            print(f"\nBakiyeniz: {bakiye} TL")

        elif secim == 2:
            # Para yatırma
            miktar = float(input("Yatırmak istediğiniz miktarı girin: "))
            if miktar > 0:
                bakiye += miktar
                print(f"{miktar} TL başarıyla yatırıldı. Güncel bakiyeniz: {bakiye} TL")
            else:
                print("Geçersiz miktar! Lütfen pozitif bir sayı girin.")

        elif secim == 3:
            # Para çekme
            miktar = float(input("Çekmek istediğiniz miktarı girin: "))
            if miktar > 0:
                if miktar <= bakiye:
                    bakiye -= miktar
                    print(f"{miktar} TL başarıyla çekildi. Güncel bakiyeniz: {bakiye} TL")
                else:
                    print("Yetersiz bakiye!")
            else:
                print("Geçersiz miktar! Lütfen pozitif bir sayı girin.")

        elif secim == 4:
            # Çıkış
            print("ATM'den çıkış yapılıyor. İyi günler dileriz!")
            break

        else:
            print("Geçersiz seçim! Lütfen 1 ile 4 arasında bir sayı girin.")

    except ValueError:
        print("Lütfen geçerli bir sayı girin!")

    # Her işlem sonrası başka işlem yapmak için sor
    cevap = input("\nBaşka bir işlem yapmak ister misiniz? (evet/hayır): ").strip().lower()
    if cevap == "hayır":
        print("ATM'den çıkış yapılıyor. İyi günler dileriz!")
        break
    elif cevap == "evet":
        continue
    else:
        print("Geçersiz giriş! Program sonlandırılıyor.")
        break
