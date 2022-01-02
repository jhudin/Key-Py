import hashlib
clacenorm=input("Ingrese clave\n")
n=hashlib.md5()
n.update((clacenorm).encode('utf-8'))
clave=n.hexdigest()
print(clave)