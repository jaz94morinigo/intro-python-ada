#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaz

import csv
from persona import Persona
from gasto import Gasto
from deposito import Deposito
from transferencia import Transferencia


def crear_cuentas():
    """
    param: None
    :return: Lista de diccionarios
    """
    personas = {}
    archivo = open("personas.csv", "r")
    archivo_csv = csv.reader(archivo)
    for nombre, dni, fecha_nacimiento, ciudad in archivo_csv:
        persona = Persona(dni, nombre, fecha_nacimiento, ciudad)
        persona.crear_cuenta()
        # La parte mas importante donde agrego al diccionario
        # con clave = dni el objecto persona
        personas[dni] = persona
    archivo.close()
    return personas


def procesar_gastos(cuenta, monto):
    gastos = {}
    personas = {}
    archivo = open("gastos.csv", "r")
    archivo_csv = csv.reader(archivo)
    for dni, monto in archivo_csv:
        gasto = Gasto(dni, monto)
        gasto.aplicar_gasto()
        personas[dni] = gastos
    archivo.close()
    return gastos
    # Return: debe devolver las cuentas actualizadas
    pass


def procesar_depositos(cuenta, monto):
    depositos = {}
    personas = {}
    archivo = open("depositos.csv", "r")
    archivo_csv = csv.reader(archivo)
    for dni, monto in archivo_csv:
        deposito = Deposito(dni, monto)
        deposito.aplicar_deposito()
        personas[dni] = depositos
    archivo.close()
    return depositos
    # Return: debe devolver las cuentas actualizadas
    pass


def procesar_transferencias(cuenta, monto):
    transferencias = {}
    personas = {}
    archivo = open("transferencias.csv", "r")
    archivo_csv = csv.reader(archivo)
    for dni, monto in archivo_csv:
        transferencia = Transferencia(dni, monto)
        transferencia.aplicar_deposito()
        personas[dni] = transferencias
    archivo.close()
    return transferencias
    # Return: debe devolver las cuentas actualizadas
    pass
