#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jazmin


from sqlalchemy import DateTime, Integer, String, Column
from app import db
from cuenta import Cuenta, CuentaJoven
import datetime
import clima_fecha


def convertir_fecha(string_fecha):
    try:
        anio = string_fecha[0:4]
        mes = string_fecha[5:7]
        dia = string_fecha[8:10]
        return datetime.date(int(anio), int(mes), int(dia))
    except Exception as error:
        print(error)
        return f"fecha no válida"


class Persona(db.Model):
    __tablename__ = 'personas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    dni = Column(String(8), nullable=False)
    ciudad = Column(String(100), nullable=False)
    monto = Column(Integer, primary_key=True)

    def __init__(self, dni, nombre, str_fecha_nacimiento, ciudad):
        self.nombre = nombre
        self.fecha_nacimiento = convertir_fecha(str_fecha_nacimiento)
        self.dni = dni
        self.cuentas = []
        self.ciudad = ciudad
        self.gastos = []
        self.depositos = []
        self.transferencias = []

    def __str__(self):
        return f'Nombre: {self.nombre}'

    @property
    def edad(self):
        hoy = datetime.date.today()
        delta = hoy - self.fecha_nacimiento
        return int(delta.days/365)

    def es_mayor_de_edad(self):
        return self.edad >= 18

    def crear_cuenta(self):
        if self.es_mayor_de_edad():
            cuenta = Cuenta()
            self.cuentas.append(cuenta)
        else:
            cuenta = CuentaJoven()
            self.cuentas.append(cuenta)
        return cuenta

    def obtener_todos_los_movimientos(self):
        todos_los_movimientos = []
        for cuenta in self.cuentas:
            todos_los_movimientos += cuenta.movimientos
        return todos_los_movimientos

    def saludo(self):
        ciudad = self.ciudad
        try:
            # no toma el parametro de la ciudad por lo tanto renderea la excepcion
            return f"¡Bienvenid@! {self.nombre}, estos son tus movimientos al {clima_fecha.traer_fecha()} , " \
                   f"{clima_fecha.obtener_estado_tiempo(ciudad):.2f}:"
        except Exception as error:
            print(error)
            return f"¡Bienvenid@! {self.nombre}, estos son tus movimientos al {clima_fecha.traer_fecha()} , " \
                   f"en la ciudad de {self.ciudad}:"
