class Edad(object):

	def __init__(self):
		self.resultado = ''

	def calculaEdad(self, edad):

		if(edad < 0):
			self.resultado = 'No existes'

		elif (edad < 13 and edad > 0):
			self.resultado = 'Eres un nino'

		elif (edad < 18 and edad > 12):
			self.resultado = 'Eres adolescente'

		elif (edad < 65 and edad > 17):
			self.resultado = 'Eres adulto'

		elif (edad < 120 and edad > 64):
			self.resultado = 'Eres adulto mayor'

		else:
			self.resultado = 'Eres Mumm-Ra'

	def obtener_resultado(self):
		return self.resultado
