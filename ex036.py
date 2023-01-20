valor_casa = float(input("Qual o valor da casa? R$"))
salario_comprador = float(input("Salário do funcionário: R$"))
anos_financiamento = int(input("Quantos anos de financiamento? "))

prestacao = valor_casa / (anos_financiamento * 12)

print(f'''Para comprar uma casa de R${valor_casa:.2f} com um salário de 
R${salario_comprador:.2f} em {anos_financiamento} anos, a prestração será de R${prestacao:.2f}''')

if prestacao > (salario_comprador * 30 / 100):
    print("\033[1;31mEmpréstimo negado!\033[m")
else:
    print("\033[1;32mEmpréstimo aprovado!\033[m")
