# OOP & Inheritance Quiz
# MIT 6.100L Lecture 19 odaklı

score = 0
total = 10

print("OOP & INHERITANCE QUIZ\n")

# ------------------ SORU 1 ------------------
print("1) Aşağıdakilerden hangisi inheritance için DOĞRUDUR?")
print("a) Subclass parent'tan sadece data attribute alır")
print("b) Subclass parent'tan sadece method alır")
print("c) Subclass parent'tan data ve method alır")
print("d) Subclass parent'tan hiçbir şey almaz")

ans = input("Cevap: ").lower()
if ans == "c":
    score += 1

# ------------------ SORU 2 ------------------
print("\n2) Getter kullanmanın ana sebebi nedir?")
print("a) Daha hızlı çalışması")
print("b) Information hiding ve bakım kolaylığı")
print("c) Daha az kod yazmak")
print("d) Python zorunlu kıldığı için")

ans = input("Cevap: ").lower()
if ans == "b":
    score += 1

# ------------------ SORU 3 ------------------
print("\n3) Aşağıdaki kod çalışır mı? (evet/hayır)")
print("""
class Cat(Animal):
    def speak(self):
        print("meow")
""")

ans = input("Cevap: ").lower()
if ans == "evet":
    score += 1

# ------------------ SORU 4 ------------------
print("\n4) Bir subclass kendi __init__ metodunu yazıyorsa ne yapmalıdır?")
print("a) Hiçbir şey")
print("b) Parent __init__'ini çağırmalıdır")
print("c) Getter yazmalıdır")
print("d) Class variable tanımlamalıdır")

ans = input("Cevap: ").lower()
if ans == "b":
    score += 1

# ------------------ SORU 5 ------------------
print("\n5) Class variable ile ilgili hangisi DOĞRU?")
print("a) Her instance için farklıdır")
print("b) Sadece parent class kullanabilir")
print("c) Tüm instance'lar paylaşır")
print("d) Sadece method içinde tanımlanır")

ans = input("Cevap: ").lower()
if ans == "c":
    score += 1

# ------------------ SORU 6 ------------------
print("\n6) Method override ne demektir?")
print("a) Method silmek")
print("b) Parent'taki methodu aynen kullanmak")
print("c) Parent'taki methodu yeniden tanımlamak")
print("d) Yeni attribute eklemek")

ans = input("Cevap: ").lower()
if ans == "c":
    score += 1

# ------------------ SORU 7 ------------------
print("\n7) __str__ metodu ne zaman çağrılır?")
print("a) input() kullanıldığında")
print("b) print(obj) çağrıldığında")
print("c) obj == other")
print("d) obj + other")

ans = input("Cevap: ").lower()
if ans == "b":
    score += 1

# ------------------ SORU 8 ------------------
print("\n8) Aşağıdakilerden hangisi special method DEĞİLDİR?")
print("a) __init__")
print("b) __add__")
print("c) __eq__")
print("d) get_age")

ans = input("Cevap: ").lower()
if ans == "d":
    score += 1

# ------------------ SORU 9 ------------------
print("\n9) Method arama sırası nasıldır?")
print("a) Parent → Subclass")
print("b) Subclass → Parent")
print("c) Rastgele")
print("d) Alphabetical")

ans = input("Cevap: ").lower()
if ans == "b":
    score += 1

# ------------------ SORU 10 ------------------
print("\n10) Hangisi kötü OOP pratiğidir?")
print("a) Getter kullanmak")
print("b) Subclass kullanmak")
print("c) Dışarıdan obj.age = 999 yapmak")
print("d) __str__ yazmak")

ans = input("Cevap: ").lower()
if ans == "c":
    score += 1

# ------------------ SONUÇ ------------------
print("\n-------------------------")
print(f"PUAN: {score} / {total}")

if score == total:
    print("🔥 Mükemmel! Bu konu sende.")
elif score >= 7:
    print("✅ İyi gidiyorsun, biraz tekrar yeter.")
elif score >= 5:
    print("⚠️ Orta seviye, örnek kod yazmalısın.")
else:
    print("❌ Bu konuyu baştan çalışmanı öneririm.")
