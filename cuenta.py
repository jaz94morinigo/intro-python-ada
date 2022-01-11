#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jazmin

import datetime
import proceso_cuentas


class Cuenta(object):

    def __init__(self, monto_inicio=0, numero_de_cuenta=0):  # contructor, siempre de la misma forma
        self.cantidad = monto_inicio
        self.numero_de_cuenta = numero_de_cuenta
        self.movimientos = []
        self.activa = True

    def aplicar_gasto(self, monto_gasto):  # retirar
        if self.activa:
            try:
                self.cantidad = self.cantidad - monto_gasto
                self.crear_movimiento("Estamos aplicando un gasto", monto_gasto)
                self.movimientos = proceso_cuentas.procesar_gastos()
                return self.movimientos
            except Exception as error:
                print(error)
                return f"Saldo insuficiente para realizar transacción"

    def aplicar_deposito(self, monto_deposito):  # ingresar
        if self.activa:
            try:
                self.cantidad = self.cantidad + monto_deposito
                self.crear_movimiento("Estamos aplicando un deposito", monto_deposito)
                self.movimientos = proceso_cuentas.procesar_depositos()
                return self.movimientos
            except Exception as error:
                print(error)
                estado = self.desactivar(0)
                return estado

    def desactivar(self, cantidad):
        if cantidad == 0:
            self.activa = False
        return f"Cuenta desactivada por saldo insuficiente"

    def activar(self, cantidad):
        if cantidad > 0:
            self.activa = True
        return f"Cuenta Activa"

    def crear_movimiento(self, descripcion, monto):
        movimiento = MovimientoCuenta(descripcion, monto)
        self.movimientos.append(movimiento)

    def __str__(self):
        return f"Tipo de cuenta: CUENTA COMÚN - Saldo: $ {self.cantidad}"


class CuentaJoven(Cuenta):

    def __init__(self, bonificacion, monto_inicio=0, numero_de_cuenta=0):
        Cuenta.__init__(self, monto_inicio, numero_de_cuenta)
        self.bonificacion = bonificacion

    def __str__(self):
        return f"Tipo de cuenta: CUENTA JOVEN - Saldo: $ {self.cantidad}"


class MovimientoCuenta(object):

    def __init__(self, descripcion, monto_del_movimiento):
        self.fecha_y_hora = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto_del_movimiento

    def __str__(self):
        if proceso_cuentas.procesar_gastos():
            self.descripcion = "Gasto"
        if proceso_cuentas.procesar_depositos():
            self.descripcion = "Depósito en cuenta"
        if proceso_cuentas.procesar_transferencias():
            self.descripcion = "Transferencia"
        return f"{self.fecha_y_hora} - {self.descripcion} por el monto de ${self.monto}"
