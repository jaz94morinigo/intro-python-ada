#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Jaz

from sqlalchemy import Integer, String, Column
from app import db


class Gasto(db.Model):
    __tablename__ = 'gastos'
    dni = Column(String(8), nullable=False)
    monto_gasto = Column(Integer, primary_key=True)

    def __init__(self, dni, monto_gasto):
        self.dni = dni
        self.monto_gasto = monto_gasto
