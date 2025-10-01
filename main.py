import time

import sys

def hash_generator(tekstas):

    # Paverčiam tekstą į sąrašą skaičių (ASCII)
    skaiciai = [ord(c) for c in tekstas]   # skaiciu masyvas

    # Atlik keletą matematikos operacijų
    pirminis = 828930167
    suma = pirminis  # pradinis sumos reikšmė
    for i, skaicius in enumerate(skaiciai):
        suma = suma ^ (skaicius * pirminis)  # XOR su kiekvienu skaičiumi * pirminis
        suma = (suma * pirminis) % 0x100000000  # daliname is Ox100000000, kad isvengtume per daug simboliu hash

    hash = f"{suma:08x}" # skaiciaus formatavimas i hex su 8 simboliais
    return hash

if __name__ == "__main__":
    if len(sys.argv) > 1:
        failo_pavadinimas = sys.argv[1]
        try:
            with open(failo_pavadinimas, "r", encoding="utf-8") as f:   # atidaromo failo pavadinimas, rezimas (read), failo koduote
                tekstas = f.read()
        except FileNotFoundError:
            print(f"Klaida: failas '{failo_pavadinimas}' nerastas.")
            sys.exit(1)
    else:
        tekstas = input("Įvesk tekstą: ")

    start = time.perf_counter_ns()
    hash = hash_generator(tekstas)
    end = time.perf_counter_ns()
    print(f"Hash generavimas užtruko {(end - start)/1000000} sekundžių.")

    print("Tavo hash:", hash)
