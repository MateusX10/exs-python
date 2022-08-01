from func import Funcionario, Salar, Chefe, Pagador

chefe1 = Chefe("SR. BOSS", "RUIM")
paga1 = Pagador(10000)

func1 = Funcionario("Bernardo")
func1.adcionar_salario(606, 606)
func1.adcionar_salario(paga1, paga1)
print(func1.ExibirSalario())

func2 = Funcionario("Rovs")
func2.adcionar_salario(1250, 1250)
print(func2.ExibirSalario())

func3 = Funcionario("Vitor")
func3.adcionar_salario(1900, 1900)
print(func3.ExibirSalario())



print(chefe1.humor)
func1.algo = chefe1
func1.algo.aumento()


print('..slskslak')
for algo in range(1,10):
    print(algo)

