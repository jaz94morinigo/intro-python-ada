#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jazmin

from sqlalchemy import Integer, String, Column
from app import db


class Transferencia(db.Model):
    __tablename__ = 'transferencias'
    dni = Column(String(8), nullable=False)
    monto_transferencia = Column(Integer, primary_key=True)

    def __init__(self, dni, monto_transferencia):
        self.dni = dni
        self.monto_transferencia = monto_transferencia
