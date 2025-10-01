import main
import time

if __name__ == "__main__":
    with open("konstitucija.txt", "r", encoding="utf-8") as f:
        eilutes = f.readlines()

    n = 1
    while n <= len(eilutes):
        grupes_tekstas = ''.join(eilutes[:n])
        start = time.perf_counter_ns()  # Nanosekundžių tikslumas
        hashas = main.hash_generator(grupes_tekstas)
        end = time.perf_counter_ns()
        elapsed_ns = end - start
        print(f"Eilutės 1-{n} hash: {hashas} (laikas: {elapsed_ns/1e6} ms)")
        n *= 2