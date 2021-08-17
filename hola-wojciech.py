# -*- coding: utf-8 -*- 
"""
escribir script que pregunte el nombre del usario en la consola y un numero entero e imprima 
por pantalla en lineas distintas el nombre del usario tantas veces como el numero introducido.

"""
name = input("como te llamas:")
n = input("introduce un numero entero: ")
print ((name + "\n") * int(n))
