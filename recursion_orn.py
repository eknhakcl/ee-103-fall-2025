# def countdown(n):
#     if n < 0:
#         return n
#     else:
#         print(n)
#         countdown(n - 1)
#         return 
    
# print(countdown(5))

########################################################

# def liste_top(liste):
#     total = 0
#     if len(liste) == 0: 
#         return 0 
#     else:
#         return liste[0] + liste_top(liste[1:])
    

# print(liste_top([20,30,40,50,60]))


#######################################################

# def ters_cevirme(word):
#     if len (word) == 0:
#         return ""
#     else:
#         return word[-1] + ters_cevirme(word[:-1])
    
# print(ters_cevirme("yeteeeeeeeeer"))

########################################################   

# def duzlestirme(liste):
#     son_liste = []
#     for i in liste:
#         if isinstance(i, list):
#             son_liste.extend(duzlestirme(i))
#         else:
#             son_liste.append(i)
#     return son_liste

# print(duzlestirme([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

#########################################################


# def koloni_yemek_hesapla(isim, aile_agaci):
#     """
#     isim: Şu an incelediğimiz Tribble'ın adı (string)
#     aile_agaci: Kimin kimin çocuğu olduğunu gösteren sözlük (dict)
    
#     Return: O Tribble ve tüm soyu için gereken toplam mama miktarı.
#     """
    
#     # Her Tribble (kendisi) 10 birim yer. Bu cepte.
#     toplam_mama = 10 
    
#     # --- BASE CASE (Durma Noktası) ---
#     # Eğer bu ismin sözlükte kaydı yoksa veya çocukları boş listeyse,
#     # sadece kendi yediğini (10) döndür ve bitir.
#     if isim not in aile_agaci or aile_agaci[isim] == []:
#         return 10

#     # --- RECURSIVE STEP (Kendini Çağırma) ---
#     # Çocuğu olanlar için: Her bir çocuğun da kendi alt soyunu hesaplaması lazım.
#     cocuklar = aile_agaci[isim]
    
#     for cocuk in cocuklar:
#         # Fonksiyonu çocuk için tekrar çağırıyoruz!
#         # Bu satır, ağacın en altına inene kadar devam eder.
#         toplam_mama += koloni_yemek_hesapla(cocuk, aile_agaci)
        
#     return toplam_mama

# # --- TEST VERİSİ (Senaryo) ---
# # 'Zorg' dedemiz. Onun çocukları 'Blorp' ve 'Glarp'.
# # 'Blorp'un çocuğu 'Xyloph'.
# # 'Xyloph'un ikizleri var: 'Quark' ve 'Quasar'.
# tribble_ailesi = {
#     'Zorg': ['Blorp', 'Glarp'],
#     'Blorp': ['Xyloph'],
#     'Glarp': [],            # Çocuğu yokconda activate ee
#     'Xyloph': ['Quark', 'Quasar'],
#     'Quark': [],            # Çocuğu yok
#     'Quasar': []            # Çocuğu yok
# }

# # --- ÇALIŞTIRMA ---
# lider = 'Zorg'
# sonuc = koloni_yemek_hesapla(lider, tribble_ailesi)

# print(f"{lider} ve tüm kolonisi için gereken mama: {sonuc} birim.")


# def kargo_degeri(esya_veya_kutu):
#     """
#     esya_veya_kutu: Ya tek bir string (örn: 'elmas') ya da bir liste (örn: ['tas', 'altın'])
#     Return: Toplam değer (int)
#     """
    
#     toplam = 0
    
#     # DURUM 1: Eğer elimizdeki şey bir LİSTE ise (yani bir kutuysa)
#     if isinstance(esya_veya_kutu, list):
#         # Kutu içindeki her şeye tek tek bakmamız lazım
#         for eleman in esya_veya_kutu:
#             # --- BURAYI DOLDUR ---
#             # İpucu: Burada 'recursion' yapmalısın. 
#             # 'eleman'ın değerini bulup 'toplam'a ekle.
#             toplam+= kargo_degeri(eleman)
            

#             # (Bu satırı silip kodunu yaz)
            
#     # DURUM 2: Eğer elimizdeki şey liste DEĞİLSE (yani tek bir eşyaysa - Base Case)
#     else:
#         # --- BURAYI DOLDUR ---
#         # Eğer eşya 'elmas' ise değerini döndür, 'altın' ise değerini döndür.
#         # Değersizse 0 döndür.
#         if esya_veya_kutu =="elmas":
#             toplam +=50
#         elif esya_veya_kutu == "altın":
#             toplam += 20 # (Bu satırı silip kodunu yaz)
#         else :
#             pass

#     return toplam

# # --- TEST VERİSİ ---
# # Bazı kutular çok derin! ([[[...]]])
# ele_gecirilen_kargo = [
#     "tas", 
#     ["altın", "corap"], 
#     "elmas", 
#     [["elmas"], "tas", ["altın", ["altın"]]]
# ]

# # Beklenen Sonuç: 
# # 1 tane dışarıda elmas (50)
# # 1 tane kutuda altın (20)
# # 1 tane derin kutuda elmas (50)
# # 2 tane en dipte altın (20 + 20)
# # Toplam = 160 olması lazım.

# sonuc = kargo_degeri(ele_gecirilen_kargo)
# print(f"Kargonun toplam değeri: {sonuc} Kredi") 


# def sinyali_temizle(sinyal):
#     """
#     sinyal: İçinde '#' işaretleri olan bozuk bir string (örn: "Y#a#r#d##ı#m")
#     Return: Temizlenmiş string (örn: "Yardım")
#     """
    
#     # --- BASE CASE (Durma Noktası) ---
#     # Eğer sinyal tamamen boşaldıysa (""), temizleyecek bir şey kalmamıştır.
#     if len(sinyal) == 0:
#         return ""
    
#     # --- RECURSIVE STEP (Kendini Çağırma) ---
    
#     # İlk harfi (karakteri) elimize alalım
#     ilk_karakter = sinyal[0]
    
#     # SENİN GÖREVİN BURADA BAŞLIYOR:
    
#     # DURUM 1: Eğer ilk karakter bir parazitse ('#')
#     if ilk_karakter == '#':
#         # Bu karakteri çöpe at ve geri kalanına bak.
#         # İpucu: return sinyali_temizle(...) 
#         # Parantez içine sinyalin geri kalanını (sinyal[1:]) yazmalısın.
#         return sinyali_temizle(sinyal[1:])# -- BURAYI DOLDUR --

#     # DURUM 2: Eğer ilk karakter normal bir harfse
#     else:
#         # Bu karakteri saklamalıyız! 
#         # İpucu: return ilk_karakter + sinyali_temizle(...)
#         return ilk_karakter + sinyali_temizle(sinyal[1:])# -- BURAYI DOLDUR --


# # --- TEST ---
# gelen_mesaj = "H#ou##s#t##o#n## #S#o#r#u#n##u#m#u#z# #V#a#r#"

# # Beklenen Sonuç: "Houston Sorunumuz Var"
# temiz_mesaj = sinyali_temizle(gelen_mesaj)

# print(f"Orijinal Mesaj: {gelen_mesaj}")
# print(f"Temizlenmiş Hali: {temiz_mesaj}")


# def hazine_hesapla(icerik):
#     # icerik: Ya bir liste (mağara) ya da bir string (eşya) olabilir.
    
#     toplam_deger = 0
    
#     # SENARYO 1: Eğer 'icerik' bir LİSTE ise (yani bir mağaranın içindeyiz)
#     if isinstance(icerik, list):
        
#         # TODO 1: Listenin içindeki her bir öğeyi gezmek için döngü kur
#         for oge in icerik:
            
#             # TODO 2: Recursive çağrı yap (öğenin değerini hesaplat)
#             # (Sonucu bir değişkene ata)
#             if isinstance(oge , str):
#                 hazine_hesapla(oge) 
#             else:
#                 hazine_hesapla(oge)
#             # TODO 3: Gelen sonucu toplama ekle
            
            
#         # TODO 4: Döngü bitti. Mağara kuralını uygula:
#         # (Bulduğun toplamı 2 ile çarpıp geri döndür)
        

#     # SENARYO 2: Eğer 'icerik' bir STRING ise (yani tek bir eşya bulduk - Base Case)
#     else:
#         # TODO 5: Eğer eşya "altin" ise kaç döndüreceksin?
#         if icerik == "altin" :
#             toplam_deger += 10
        
#         # TODO 6: Eğer eşya "elmas" ise kaç döndüreceksin?
#         elif icerik == " elmas" :
#             toplam_deger+= 50 
        
#         # TODO 7: Hiçbiri değilse ("cop" vs.) ne döndüreceksin?
#         else:
#             pass

# # --- TEST ---
# # Bu mağara yapısı:
# # - Yüzeyde bir "cop" var (0)
# # - Bir alt mağarada (x2) bir "altin" var (10) -> Burası 20 getirmeli.
# # - Başka bir mağarada (x2) bir "elmas" (50) ve daha da dipte (x2 * x2 = x4) bir "altin" (10) var.
# okyanus_tabani = ["cop", ["altin"], ["elmas", ["altin"]]]

# # Beklenen Hesap:
# # "cop" -> 0
# # ["altin"] -> 10 * 2 = 20
# # ["elmas", ["altin"]] -> ("elmas": 50) + (["altin"]: 10 * 2 = 20) -> Toplam 70. 
# # Bu 70 puan da bir liste içinde olduğu için tekrar 2 ile çarpılır -> 140.
# # Genel Toplam: 0 + 20 + 140 = 160 olmalı.

# sonuc = hazine_hesapla(okyanus_tabani)
# print(f"Toplam Hazine Değeri: {sonuc}")







def x_temizle_ve_say(dosya_ismi):
    """
    Görevi: Bir string alır. Baştaki 'X'leri atar.
    Geriye temiz halinin UZUNLUĞUNU (int) döndürür.
    Örn: "XXData" -> "Data" kalır -> 4 döndürür.
    Bunu döngü kullanmadan, RECURSION ve SLICING ile yapmalısın.
    """
    
    # --- BASE CASE ---
    # TODO 1: Eğer dosya_ismi boş bir string ise (""), uzunluğu nedir?
    if dosya_ismi == "":
        return 0 # (Burası basit, ipucu olsun)
    
    # --- RECURSIVE STEPS ---
    ilk_harf = dosya_ismi[0]
    
    # TODO 2: Eğer ilk harf 'X' ise (bozuk kısımsa):
    if ilk_harf == 'X':
        # O harfi saymamalıyız (0 puan).
        # Stringin geri kalanını (slicing: dosya_ismi[1:]) fonksiyona tekrar gönder.
        # Sadece dönen sonucu geri ver (return et).
        return x_temizle_ve_say(dosya_ismi[1:]) # ... BURAYI DOLDUR ...

    # TODO 3: Eğer ilk harf 'X' DEĞİLSE (yani geçerli bir veri ise):
    else:
        # Bu harf geçerli! (+1 puan).
        # 1 + geri kalanın sonucunu döndür.
        return dosya_ismi # ... BURAYI DOLDUR ...


def sistemi_tara(veri_yapisi):
    """
    Görevi: İç içe listeleri (klasörleri) gezer.
    Her dosya (string) bulduğunda yukarıdaki 'x_temizle_ve_say' fonksiyonunu çağırır.
    Toplam boyutu hesaplar.
    """
    
    toplam_boyut = 0
    
    # --- BASE CASE (String ise) ---
    # Duyuruda "break into smaller subproblems" denmiş.
    # Eğer elimizdeki veri bir liste değil, direkt bir string ise (Dosya ise):
    
    # TODO 4: Verinin tipini kontrol et. Eğer 'list' değilse (yani string ise):
    if not isinstance(veri_yapisi, list):
        
        # TODO 5: Yukarıda yazdığın 'x_temizle_ve_say' fonksiyonunu çağır.
        # Sonucu direkt return et.
        return # ... BURAYI DOLDUR ...

    # --- RECURSIVE STEP (Liste ise) ---
    # TODO 6: Eğer buraya geldiysek, 'veri_yapisi' bir listedir (Klasördür).
    # Listenin içindeki her elemanı gezmek için bir döngü kur.
    # (Not: Burada for döngüsü kullanabilirsin, çünkü bu "structure traversal")
    
    # ... FOR DÖNGÜSÜNÜ BURAYA KUR ... (for eleman in veri_yapisi:)
        
        # TODO 7: Döngü içindesin. Elindeki 'eleman'ın ne olduğunu bilmiyorsun.
        # (Belki dosya, belki başka bir klasör).
        # Kendini (sistemi_tara fonksiyonunu) bu 'eleman' ile çağır.
        # Gelen sonucu bir değişkene (örn: alt_sonuc) ata.
        
        # ... KODU BURAYA YAZ ...
        
        # TODO 8: Gelen 'alt_sonuc'u 'toplam_boyut'a ekle.
        
        # ... KODU BURAYA YAZ ...
            
    # TODO 9: Döngü bitti. Tüm alt klasörlerden gelen toplamı döndür.
    return # ... BURAYI DOLDUR ...


# --- TEST SENARYOSU ---
# "XXResim" -> Temizlenince "Resim" (5 karakter)
# "Kod" -> "Kod" (3 karakter)
# "XXXVeri" -> "Veri" (4 karakter)
# Toplam beklenen: 5 + 3 + 4 = 12

sunucu_yedegi = [
    "XXResim",
    ["Kod", ["XXXVeri"]],
    [] # Boş klasör (0 getirmeli)
]

print("Hesaplama Başlıyor...")
sonuc = sistemi_tara(sunucu_yedegi)
print(f"Toplam Kurtarılan Veri Boyutu: {sonuc}")

# Beklenen Çıktı: 12