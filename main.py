
import sys

def hash_generator(tekstas):

    # Paverčiam tekstą į sąrašą skaičių (ASCII)
    skaiciai = [ord(c) for c in tekstas]   # skaiciu masyvas

    # Atlik keletą matematikos operacijų
    pirminis = 1109
    suma = pirminis * pirminis
    for i, skaicius in enumerate(skaiciai):
        suma = suma ^ skaicius  # XOR su kiekvienu skaičiumi
        suma = (suma * pirminis) % 0x100000000  # daliname is Ox100000000, kad isvengtume per daug simboliu hash

    hash = f"{suma: 08x}" # skaiciaus formatavimas i hex su 8 simboliais
    return hash

if __name__ == "__main__":
   tekstas = input("Įvesk tekstą: ")
   print("Tavo hash:", hash_generator(tekstas))
