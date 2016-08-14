class Aresta(object):
	"""docstring for Aresta"""
	def __init__(self, identificador1, identificador2):
		super(Aresta, self).__init__()
		self.identificador1 = identificador1
		self.identificador2 = identificador2

	def __str__(self):
		return '['+self.identificador1.__str__()+', '+self.identificador2.__str__()+']'

	def str(self):
		return '['+self.identificador1.__str__()+', '+self.identificador2.__str__()+']'

class ArestaValorada(Aresta):
	"""docstring for ArestaValor"""
	def __init__(self, identificador1, identificador2, valor):
		Aresta.__init__(self, identificador1, identificador2)
		self.valor = valor
	
	def __str__(self):
		return '['+self.identificador1.__str__()+', '+self.identificador2.__str__()+'] {'+self.valor.__str__()+'}'

	def str(self):
		return '['+self.identificador1.__str__()+', '+self.identificador2.__str__()+'] {'+self.valor.__str__()+'}'