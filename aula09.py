frase = "    dragão de fogo e gelada       "

print(frase.count("o"))
print(frase.count("A"))
print(frase.count("f"))
print(frase.count(""))
print(frase.count(" "))
print(frase.count(frase))
print(frase.count("nome"))
frase = frase.replace("fogo", "vento")
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.upper().isupper())
if frase.upper().isupper():
    print("É maiúsculo")
else:
    print("É minúsculo")
print(len(frase.replace("dragão", "dino").strip()))
if len(frase) >= 20:
    frase = frase.replace("dragão", "dinossauro")
else:
    frase = frase.replace("dragão", "dinossauro")
print(frase)
if "dinossauro" in frase:
    print("QUE PERIGOSO!")
elif "dino" in frase:
    print("Tem que crescer...")
elif "dragão" in frase:
    print("Mijei nas calças...")

print("a" in frase)
print(frase.find("a"))
dividido = frase.split()
print(frase, dividido)
print(dividido[2][3])
print("=".join(dividido))