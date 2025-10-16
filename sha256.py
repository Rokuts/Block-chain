import hashlib

def hash_generator(tekstas):
    
    # Generuoja SHA-256 hašą iš duoto teksto.
    
    return hashlib.sha256(tekstas.encode('utf-8')).hexdigest()