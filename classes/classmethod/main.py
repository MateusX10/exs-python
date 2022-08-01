from classes import Livro

livro1 = Livro.set_pag("Os Aventureiros", 240)

print(f'O livro "{livro1.titulo}" tem {livro1.paginas} páginas')    
livro1.virar_frente(300)
livro1.virar_tras(400)