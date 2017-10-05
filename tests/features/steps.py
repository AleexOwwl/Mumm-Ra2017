# -*- coding: utf-8 -*-
from lettuce import step, world
from Edad import Edad


@step(u'cuando realizo la consulta')
def cuando_realizo_la_consulta(step):
    pass

@step(u'Dado que ingreso la edad "([^"]*)"')
def dado_que_ingreso_la_edad_group1(step, num1):
    world.edades = Edad()
    world.edades.calculaEdad(int(num1))

@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.edades.obtener_resultado()
    assert esperado == obtenido,'El resultado esperado es '+esperado+" y el obtenido es "+obtenido
