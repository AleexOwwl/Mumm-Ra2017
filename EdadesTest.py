# !/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from Edad import Edad


class EdadesTest(unittest.TestCase):

    def setUp(self):
        self.edades = Edad()

    def test_si_es_menor_de_0(self):
        self.assertEquals(self.edades.calculaEdad(-1), 'No existes')

    def test_si_es_menor_de_13(self):
        self.assertEquals(self.edades.calculaEdad(12), 'Eres un niño')

    def test_si_es_menor_de_18(self):
        self.assertEquals(self.edades.calculaEdad(17), 'Eres adolescente')

    def test_si_es_menor_de_65(self):
        self.assertEquals(self.edades.calculaEdad(50), 'Eres adulto')

    def test_si_es_menor_de_120(self):
        self.assertEquals(self.edades.calculaEdad(100), 'Eres adulto mayor')

    def test_De_lo_contrario_eres_MummRa(self):
        self.assertEquals(self.edades.calculaEdad(1000), 'Eres Mumm-Ra')


if __name__ == '__main__':
    unittest.main()
