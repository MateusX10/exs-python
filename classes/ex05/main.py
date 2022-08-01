from conta_corrente import ContaCorrente

corrente1 = ContaCorrente("conta", "Enzo", "R$100")
corrente1.AltNome("nova conta")
print(corrente1.nome_conta)
print(corrente1.nome_correntista)
print(corrente1.saldo)
resp = corrente1.VerDepósito()
if resp == "S":
    quant = float(input('Sacar quanto? '))
    corrente1.Sacar(quant)
    print(f'Agora você tem R${corrente1.saldo:.2f} em sua conta bancária')
print('\033[1;32m<<< Volte Sempre! >>>\033[m')
