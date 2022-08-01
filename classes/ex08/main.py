from macacoo import Macaco

macaco1 = Macaco("Ted", "vazio")
macaco2 = Macaco("Git", "vazio")

macaco1.VerBucho()
macaco2.VerBucho()
macaco1.show()
macaco2.show()
macaco1.comer()
macaco1.digerir("banana")
macaco2.comer("maçã")
macaco2.bucho = "vazio"
macaco1.bucho = 'vazio'
macaco1.comer("abacate")
macaco2.comer('limão')
macaco2.digerir("maçã")
macaco1.PararComer()
macaco1.PararComer()
macaco1.digerir()
macaco2.PararComer()
macaco1.VerBucho()
macaco2.VerBucho()
macaco1.canibalismo(macaco2)