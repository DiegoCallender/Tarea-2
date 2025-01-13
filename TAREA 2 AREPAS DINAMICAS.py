
""""
TAREA 2 AREPAS DINAMICAS
Escriba un programa en Python que pida al usuario las cantidades de ingredientes de una arepa y calcule el volumen de la arepa terminada.

La receta oficial de Empresas Polar para una arepa es:

Ingredientes
1 tza agua
1 tza harina PAN
1 cdta sal
1 cda aceite
Preparación
En un bol, se vierte el agua, la harina y la sal
Se mezcla hasta que quede uniforme
Se le da a la mezcla forma de disco
Se coloca con el aceite en un budare hasta dorar
Se voltea y repite
Se sirve en un plato
Considere las siguientes reglas de cocina en su programa:

1 cda = 3 cdtas
1 tza = 16 cda
El 10% del volmen se evapora en el proceso de cocción//

"""

print("¡Bienvenido a Arepas Dinamicas!\n+---------- - ------ ---------+\nIndique que cantidad de ingredientes posee: ")

cantidad_de_agua=int(input("Número de Tzas de Agua: "));
if cantidad_de_agua==0 or cantidad_de_agua < 0:
    print("Se necesita este ingrediente para hacer la receta")
    while cantidad_de_agua==0 or cantidad_de_agua < 0:
        cantidad_de_agua=int(input("Número de Tzas de Agua: "))

cantidad_de_harina_pan=int(input("Número de Tzas de Harina Pan: "));
if cantidad_de_harina_pan==0 or cantidad_de_harina_pan < 0:
    print("Se necesita este ingrediente para hacer la receta")
    while cantidad_de_harina_pan==0 or cantidad_de_harina_pan < 0:
        cantidad_de_harina_pan=int(input("Número de Tzas de Harina Pan: "));

cantidad_de_sal=int(input("Número de cdta de sal: "));
if cantidad_de_sal < 0:
    print("No se puede ingresar unidades negativas")
    while  cantidad_de_sal < 0:
        cantidad_de_sal=int(input("Número de cdta de sal: "));
    

cantidad_de_aceite=int(input("Número de cda de aceite: "));
if cantidad_de_aceite < 0:
    print("No se puede ingresar unidades negativas")
    while  cantidad_de_aceite < 0:
        cantidad_de_aceite=int(input("Número de cda de aceite: "));

cantidad_de_agua_ml=cantidad_de_agua*236.6;
cantidad_de_harina_pan_ml=cantidad_de_harina_pan*236.6;
cantidad_de_sal_ml=cantidad_de_sal*4.929
cantidad_de_aceite_ml=cantidad_de_aceite*14.79;


print("\nAhora sigue los siguientes pasos:\nEn un bol, se vierte el agua, la harina y, si uso, la sal\nSe mezcla hasta que quede uniforme\nSe le da a la mezcla forma de disco\nEn caso de usarlo, se coloca con el aceite en un budare hasta dorar\nSe voltea y repite\nSe sirve en un plato\nRecordar que el uso de la sal y el aceite es de su preferencia\n")

input("Presione Enter una vez terminado los pasos")


if  cantidad_de_sal == 0 and cantidad_de_aceite_ml== 0:
    volumen_de_la_arepa_sin_perdida=cantidad_de_agua_ml+cantidad_de_harina_pan_ml
    volumen_de_la_arepa_con_perdida=volumen_de_la_arepa_sin_perdida*0.90
    print("\nEl volumen de la arepa terminada será de: \n",volumen_de_la_arepa_con_perdida,"ml\n")

elif cantidad_de_sal == 0:
    volumen_de_la_arepa_sin_perdida=cantidad_de_agua_ml+cantidad_de_harina_pan_ml+cantidad_de_aceite_ml
    volumen_de_la_arepa_con_perdida=volumen_de_la_arepa_sin_perdida*0.90
    print("\nEl volumen de la arepa terminada será de: \n",volumen_de_la_arepa_con_perdida,"ml\n")

elif cantidad_de_aceite_ml == 0:
    volumen_de_la_arepa_sin_perdida=cantidad_de_agua_ml+cantidad_de_harina_pan_ml+cantidad_de_sal_ml
    volumen_de_la_arepa_con_perdida=volumen_de_la_arepa_sin_perdida*0.90
    print("\nEl volumen de la arepa terminada será de: \n",volumen_de_la_arepa_con_perdida,"ml\n")
else:
    volumen_de_la_arepa_sin_perdida=cantidad_de_agua_ml+cantidad_de_harina_pan_ml+cantidad_de_sal_ml+cantidad_de_aceite_ml
    volumen_de_la_arepa_con_perdida=volumen_de_la_arepa_sin_perdida*0.90
    print("\nEl volumen de la arepa terminada será de: \n",volumen_de_la_arepa_con_perdida,"ml\n")


input()