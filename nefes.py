import time
import sys

def nefes_sayaci():
    print("\n--- 4-7-8 NEFES TEKNİĞİ BAŞLIYOR ---")
    print("Rahat bir pozisyon al. Başlamak için hazırlan...")
    time.sleep(2)
    
    tur_sayisi = 4
    
    try:
        for i in range(1, tur_sayisi + 1):
            print(f"\n================ TUR {i} / {tur_sayisi} ================")
            
            # --- 4 Saniye Nefes Al ---
            print("BURUNDAN AL (4 sn)")
            for s in range(1, 5):
                print(f"  🟢 {s}") 
                time.sleep(1)
            
            # --- 7 Saniye Tut ---
            print("TUT (7 sn)")
            for s in range(1, 8):
                print(f"  🔴 {s}")
                time.sleep(1)
                
            # --- 8 Saniye Ver ---
            print("AĞIZDAN VER (8 sn - 'Vuuu' sesiyle)")
            for s in range(1, 9):
                print(f"  🔵 {s}")
                time.sleep(1)
                
        print("\n--- Egzersiz Bitti. Harika iş çıkardın! ---")
        
    except KeyboardInterrupt:
        print("\nProgram durduruldu.")

# Programın hemen kapanmaması için bekleme ekliyoruz
input("\nÇıkmak için Enter tuşuna basınız...")