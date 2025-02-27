"""
Programa: ex19_retorno
Descrição: Este programa calcula o retorno esperado de um ativo.
Autor: Mayara Binsfeld
Data: 27/02/2025
Versão: 0.0.1

"""

# Alocação de memória
rf = 0
rm = 0
bi = 0

# Entrada de dados
rf = float(input("Qual é o retorno do ativo sem risco (%): ?"))
rm = float(input("Qual é o retorno da carteira de mercado (%) ?"))
bi = float(input("Qual é o coeficiente de sensibilidade de retorno do ativo a variações?"))

# Processamento de dados

retorno = rf + bi*(rm-rf)

# Saída de dados

print(f"O retorno esperado do ativo é {retorno: .2f}%")
