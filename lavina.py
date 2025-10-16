import random
import string
import sys
import importlib


def atsitiktinis_string(ilgis):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=ilgis))

def pakeisk_viena_simboli(s):
    poz = random.randint(0, len(s) - 1)
    simboliai = string.ascii_letters + string.digits
    naujas = random.choice([c for c in simboliai if c != s[poz]])
    return s[:poz] + naujas + s[poz+1:]

def skirtingi_bitai(h1, h2):
    # Konvertuojam į int ir XORinam, tada suskaičiuojam 1 bitus
    return bin(int(h1, 16) ^ int(h2, 16)).count('1')

def skirtingi_hexai(h1, h2):
    return sum(a != b for a, b in zip(h1, h2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Pasirink su kuria hash funkcija atlikti lavinos testa: main (mano hash), sha256 (SHA256)")
        sys.exit(1)
    
    hash_module_name = sys.argv[1] 

    try:
        hash_module = importlib.import_module(hash_module_name)
        hash_generator_func = hash_module.hash_generator
    except ImportError:
        print(f"Klaida: Modulis '{hash_module_name}' nerastas. Patikrinkite pavadinimą.")
        sys.exit(1)
    except AttributeError:
        print(f"Klaida: Modulyje '{hash_module_name}' nerasta 'hash_generator' funkcijos.")
        sys.exit(1)
    
    
    print(f"Vykdomas lavinos testas su '{hash_module_name}'") # Pridėjau informatyvų pranešimą


    poru_kiekis = 100_000
    ilgis = 64  # Galite keisti pagal poreikį

    bitu_skirtingumai = []
    hexu_skirtingumai = []

    for _ in range(poru_kiekis):
        s1 = atsitiktinis_string(ilgis)
        s2 = pakeisk_viena_simboli(s1)
        h1 = hash_generator_func(s1) 
        h2 = hash_generator_func(s2)
        bitu = skirtingi_bitai(h1, h2)
        hexu = skirtingi_hexai(h1, h2)
        bitu_skirtingumai.append(bitu)
        hexu_skirtingumai.append(hexu)

    # Statistika
    min_bit = min(bitu_skirtingumai)
    max_bit = max(bitu_skirtingumai)
    vid_bit = sum(bitu_skirtingumai) / poru_kiekis

    min_hex = min(hexu_skirtingumai)
    max_hex = max(hexu_skirtingumai)
    vid_hex = sum(hexu_skirtingumai) / poru_kiekis

    print(f"\nRezultatai '{hash_module_name}':") # Pridėjau informatyvų pranešimą
    print(f"Bitų lygmeniu: min={min_bit}, max={max_bit}, vid={vid_bit:.2f}")
    print(f"Hex lygmeniu: min={min_hex}, max={max_hex}, vid={vid_hex:.2f}")