import main
import random
import string

def atsitiktinis_string(ilgis):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=ilgis))

def rasti_kolizijas(ilgis, poru_kiekis=100_000):
    koliziju = 0
    for _ in range(poru_kiekis):
        s1 = atsitiktinis_string(ilgis)
        s2 = atsitiktinis_string(ilgis)
        h1 = main.hash_generator(s1)
        h2 = main.hash_generator(s2)
        if h1 == h2:
            koliziju += 1
    return koliziju

if __name__ == "__main__":
    ilgiai = [10, 100, 500, 1000]
    poru_kiekis = 100_000
    for ilgis in ilgiai:
        koliziju = rasti_kolizijas(ilgis, poru_kiekis)
        print(f"Ilgis: {ilgis}, porų: {poru_kiekis}, kolizijų: {koliziju}")