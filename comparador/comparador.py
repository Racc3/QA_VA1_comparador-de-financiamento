def calcular_consorcio(valor, taxa_admin, prazo, reajuste_anual=5):
    if valor <= 0 or taxa_admin < 0 or prazo <= 0:
        raise ValueError("Valores inválidos")

    taxa = taxa_admin / 100
    parcela_base = (valor * (1 + taxa)) / prazo

    total = 0
    parcelas = []

    for mes in range(1, prazo + 1):
        anos_passados = (mes - 1) // 12
        fator_reajuste = (1 + reajuste_anual / 100) ** anos_passados
        parcela_corrigida = parcela_base * fator_reajuste

        parcelas.append(parcela_corrigida)
        total += parcela_corrigida

    return parcelas, total


def calcular_financiamento(valor, juros_mensal, prazo):
    if valor <= 0 or juros_mensal < 0 or prazo <= 0:
        raise ValueError("Valores inválidos")

    i = juros_mensal / 100
    parcela = valor * (i * (1 + i) ** prazo) / ((1 + i) ** prazo - 1)
    total = parcela * prazo
    return parcela, total
