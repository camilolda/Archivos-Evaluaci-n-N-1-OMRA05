print("Evaluación N°1 Redes Avanzadas I")
print("Integrantes: Benjamin Pacheco - Felipe Amaro - Camilo Gonzales")
Integrantes = input ("nombre de los integrantes: ")
CodigodeSeccion = input ("Codigo de Seccion: ")
Sede = input ("Sede: ")

print(Integrantes,CodigodeSeccion,Sede)



def verificar_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        print("ACL Estándar")
    elif numero_acl >= 100 and numero_acl <= 199:
        print("ACL Extendida")
    elif numero_acl >=200:
        print("número no corresponde a una lista de acceso ")
numero_acl = int(input("Ingrese el número de ACL IPv4: "))
verificar_acl(numero_acl)