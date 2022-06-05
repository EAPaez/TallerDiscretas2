#######################################################
#     @Autores:                                       #
#            Isabella Marin Gutierrez 1958555         #
#            Eduardo Arturo Paez Molina 1968133       #
#            Jesus Alberto Gil Ayala  1968231         #
#            Kevin Steven Victoria Ospina 1968140     #
#                                                     #
#######################################################

# Punto Numero 1.2

# En este metodo llenamos el conjunto universal hasta el numero ingresado por el usuario.
def llenar(n):
    p = set()
    p = {n}
    for i in range(1, n + 1):
        p.add(i)
    return p


# En este metodo se haya un numero entre el conjunto.
def existe(n, k):
    existe = False
    for i in k:
        if i == n:
            existe = True
            break
        else:
            continue
    return existe


# En este meto se suman los elementos del conjunto.
def sum(U):
    suma = 0
    for i in U:
        suma += i
    return suma


# Este es el metodo principal en el cual se evaluan los valores de entrada y se realiza la operación
# que permite determinar y desarrollar la condición planteada en el ejercicio.

def main():
    n = 0
    k = 0
    while n < 1:
        n = int(input("Ingrese el último número: "))
    while k < 1:
        k = int(input("Ingrese la suma que desea encontrar: "))
    U = llenar(n)
    print(f"U = {U} -> Suma: {sum(U)}")
    suma = sum(U)
    if suma < k:
        print("NO")
    else:
        objetivo = k
        C = set()
        C = {0}
        acc = 0
        for i in U:
            acc += i
            C.add(i)
            if acc > objetivo:
                C.discard(acc - objetivo)
                C.discard(0)
                break
            else:
                C.discard(0)
                continue

        print(f"C = {C} -> Suma: {sum(C)}")


main()