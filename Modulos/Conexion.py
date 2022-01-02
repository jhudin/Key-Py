# -*- coding: utf-8 -*-
def conexionBd(user, baseDatos):
    global dato
    dato = []
    dato = {
        'user': user,
        'password': '',
        'database': baseDatos,
        'host': 'localhost', }
    return dato
