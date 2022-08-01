from bomba import BombaCombustivel

bomb_comb1 = BombaCombustivel("gasolina", 7.24, 5)
bomb_comb2 = BombaCombustivel("etanol", 5, 8)
bomb_comb3 = BombaCombustivel("diesel", 7, 2)

bomb_comb1.ViewInfo()
bomb_comb2.ViewInfo()
bomb_comb3.ViewInfo()
bomb_comb1.AlterarLitro()
bomb_comb1.AlterarQuant()
bomb_comb1.AbastecerValor()
bomb_comb1.AbasterLitro()