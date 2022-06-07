radioEsfera = int(input("Escribe el radio de la esfera: "))
area = 4 * radioEsfera * radioEsfera
volumen = 4 * radioEsfera * radioEsfera * radioEsfera 
print("El area de la esfera es de: ",area,"π")
print("El volumen de la esfera es de: ",volumen,"π")
division = input("Dividir en 3? (Si/No): ")
if division == "Si":
    print("El volumen dividido de la esfera es de: ",volumen/3,"π")
