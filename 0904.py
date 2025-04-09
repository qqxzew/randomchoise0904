import random

moznosti = ["telefon", "notebook", "sluchátka", "kamera", "tablet", "mikrovlnka", "chleb", "bicykl", "auto"]
for i in range(10):
    osoba1volba = random.choice(moznosti)
    osoba2volba = random.choice(moznosti)
    print(f"Kupme {osoba1volba}")
    
    if osoba1volba == osoba2volba:
        print(f"Ne, kupme jiný {osoba1volba}")
    else:
        print(f"Ne, kupme {osoba2volba}")
