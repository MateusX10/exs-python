from conta import ContaInvestimento

conta1 = ContaInvestimento(1000, 10)
for cont in range(0,5):
    conta1.AdcionarJuros()
conta1.StatusConta()