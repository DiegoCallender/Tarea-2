
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

print("""
¡Bienvenido a Arepas Dinamicas!
+---------- - ------ ---------+
Indique que cantidad de ingredientes posee: 
    """)

cantidad_de_agua=int(input("Número de Tzas de Agua: "));
if cantidad_de_agua==0 or cantidad_de_agua < 0:
    while cantidad_de_agua==0 or cantidad_de_agua < 0:
        print("Se necesita este ingrediente para hacer la receta")
        cantidad_de_agua=int(input("Número de Tzas de Agua: "))

cantidad_de_harina_pan=int(input("Número de Tzas de Harina Pan: "));
if cantidad_de_harina_pan==0 or cantidad_de_harina_pan < 0:
    while cantidad_de_harina_pan==0 or cantidad_de_harina_pan < 0:
        print("Se necesita este ingrediente para hacer la receta")
        cantidad_de_harina_pan=int(input("Número de Tzas de Harina Pan: "));

cantidad_de_sal=int(input("Número de cdta de sal: "));

cantidad_de_aceite=int(input("Número de cda de aceite: "));

"""
Conversion de Unidades:
1 Tza=236,6 ml
1 Cda=14,79 ml
1 Cdta=4,929 ml
"""

cantidad_de_agua_ml=cantidad_de_agua*236.6;
cantidad_de_harina_pan_ml=cantidad_de_harina_pan*236.6;
cantidad_de_sal_ml=cantidad_de_sal*4.929
cantidad_de_aceite_ml=cantidad_de_aceite*14.79;


print("""
Ahora sigue los siguientes pasos:
En un bol, se vierte el agua, la harina y, si uso, la sal
Se mezcla hasta que quede uniforme\nSe le da a la mezcla forma de disco
En caso de usarlo, se coloca con el aceite en un budare hasta dorar
Se voltea y repite
Se sirve en un plato
Recordar que el uso de la sal y el aceite es de su preferencia
      """)

input("Presione Enter una vez terminado los pasos")

"""
Se determina el volumen total despues de la perdida
"""
volumen_de_la_arepa_sin_perdida=cantidad_de_agua_ml+cantidad_de_harina_pan_ml+cantidad_de_sal_ml+cantidad_de_aceite_ml
volumen_de_la_arepa_con_perdida=volumen_de_la_arepa_sin_perdida*0.90

print(f"El volumen de la masa al finalizar será de {volumen_de_la_arepa_con_perdida} ml")

input()