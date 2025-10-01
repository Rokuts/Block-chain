import main
inputas = input("Įvesk teksta: ")
salt = "X7f9!"
print("Hash:", main.hash_generator(inputas + salt))
# Kitiems parodyk tik hash, bet ne input ir salt.