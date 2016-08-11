import types
from No import No, NoArvore
from Situacao import Situacao

class Arvore(object):
	"""docstring for Arvore"""
	def __init__(self, raiz):
		super(Arvore, self).__init__()
		self.raiz = raiz
		self.nos = []

	def insertNo(self, no):
		if type(no) == NoArvore:
			self.nos.append(no)
			return Situacao(True, "No inserido com sucesso")
		return Situacao(False, "No n eh do tipo NoArvore")

	def __str__(self):
		string = "Raiz: "+self.raiz.str()
		string += "\nCorpo: "
		if len(self.nos) >= 1:
			string += self.nos[0].str()
		for no in self.nos[1:]:
			string += ", " + no.str()
		return string