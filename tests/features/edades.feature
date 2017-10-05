Feature: Consulta edades
	Como usuario de Calcula edades
	deseo realizar la consulta de edad
	para obtener el tipo de edad

	Scenario: Edad menos 1
		Dado que ingreso la edad "-1"
		cuando realizo la consulta
		entonces obtengo el resultado "No existes"

	Scenario: Edad 12
		Dado que ingreso la edad "12"
		cuando realizo la consulta
		entonces obtengo el resultado "Eres un nino"

	Scenario: Edad 17
		Dado que ingreso la edad "17"
		cuando realizo la consulta
		entonces obtengo el resultado "Eres adolescente"

	Scenario: Edad 50
		Dado que ingreso la edad "50"
		cuando realizo la consulta
		entonces obtengo el resultado "Eres adulto"

	Scenario: Edad 100
		Dado que ingreso la edad "100"
		cuando realizo la consulta
		entonces obtengo el resultado "Eres adulto mayor"

	Scenario: Edad 1000
		Dado que ingreso la edad "1000"
		cuando realizo la consulta
		entonces obtengo el resultado "Eres Mumm-Ra"
