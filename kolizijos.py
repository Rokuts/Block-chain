import random
import string
import sys
import importlib # Leidžia dinamiškai importuoti modulius

def atsitiktinis_string(ilgis):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=ilgis))

# Funkcija rasti kolizijoms, dabar priima hash_generator_func kaip argumentą
def rasti_kolizijas(hash_generator_func, ilgis, poru_kiekis=100_000):
    koliziju = 0
    
    for _ in range(poru_kiekis):
        s1 = atsitiktinis_string(ilgis)
        s2 = atsitiktinis_string(ilgis)
        
        # Naudojame perduotą hash_generator_func
        h1 = hash_generator_func(s1) 
        h2 = hash_generator_func(s2)
        
        if h1 == h2:
            koliziju += 1
    return koliziju

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pasirink su kuria hash funkcija atlikti lavinos testa: main (tavo hash), sha256 (SHA256)")
        sys.exit(1)

    hash_module_name = sys.argv[1] # Paimame modulio pavadinimą iš komandinės eilutės argumento

    try:
        # Dinamiškai importuojame pasirinktą hešavimo modulį
        hash_module = importlib.import_module(hash_module_name)
        hash_generator_func = hash_module.hash_generator
    except ImportError:
        print(f"Klaida: Modulis '{hash_module_name}' nerastas. Patikrinkite pavadinimą.")
        sys.exit(1)
    except AttributeError:
        print(f"Klaida: Modulyje '{hash_module_name}' nerasta 'hash_generator' funkcijos.")
        sys.exit(1)

    print(f"Vykdomas kolizijų testas su '{hash_module_name}'")

    ilgiai = [10, 100, 500, 1000]
    poru_kiekis = 100_000 # Šis skaičius turėtų būti didelis, kad būtų galima rasti kolizijas.

    print(f"Generuojama porų: {poru_kiekis}")
    print("-" * 30)

    for ilgis in ilgiai:
        # Perduodame pasirinktą hash_generator_func funkcijai rasti_kolizijas
        koliziju = rasti_kolizijas(hash_generator_func, ilgis, poru_kiekis)
        print(f"Teksto ilgis: {ilgis}, kolizijų: {koliziju}")
    
    print("-" * 30)
    print(f"Kolizijų testas su '{hash_module_name}' baigtas.")