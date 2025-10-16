import time
import sys
import importlib

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Pataisytas pranešimas, kad atspindėtų minimalų reikalavimą
        print("Pasirink su kuria hash funkcija atlikti lavinos testa: main (tavo hash), sha256 (SHA256)")
        sys.exit(1)

    hash_module_name = sys.argv[1]

    try:
        hash_module = importlib.import_module(hash_module_name)
        hash_generator_func = hash_module.hash_generator
    except ImportError:
        print(f"Klaida: Modulis '{hash_module_name}' nerastas.")
        sys.exit(1)
    except AttributeError:
        print(f"Klaida: Modulyje '{hash_module_name}' nerasta 'hash_generator' funkcijos.")
        sys.exit(1)

    
    with open("konstitucija.txt", "r", encoding="utf-8") as f:
        eilutes = f.readlines()

    n = 1
    
    print(f"Vykdomas konstitucijos testas su '{hash_module_name}'")
    while n <= len(eilutes):
        grupes_tekstas = ''.join(eilutes[:n])
        start = time.perf_counter_ns()  # Nanosekundžių tikslumas
        hashas = hash_generator_func(grupes_tekstas) # Dinamiškai pasirinktos funkcijos kvietimas
        end = time.perf_counter_ns()
        elapsed_ns = end - start
        print(f"Eilutės 1-{n} hash: {hashas} (laikas: {elapsed_ns/1e6} ms)")
        n *= 2