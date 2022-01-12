#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaz

from sqlalchemy import Integer, String, Column
from app import db


class Deposito(db.Model):
    __tablename__ = 'depositos'
    dni = Column(String(8), nullable=False)
    monto_deposito = Column(Integer, primary_key=True)

    def __init__(self, dni, monto_deposito):
        self.dni = dni
        self.monto_deposito = monto_deposito
