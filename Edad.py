# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Edad():

    def calculaEdad(self, edad):

        if(edad < 0):
            return 'No existes'

        elif (edad < 13 and edad > 0):
            return 'Eres un niño'

        elif (edad < 18 and edad > 12):
            return 'Eres adolescente'

        elif (edad < 65 and edad > 17):
            return 'Eres adulto'

        elif (edad < 120 and edad > 64):
            return 'Eres adulto mayor'

        else:
            return 'Eres Mumm-Ra'
