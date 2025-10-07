import pytest
from comparador import calcular_consorcio, calcular_financiamento

def test_reajuste_anual_consorcio():
    parcelas, _ = calcular_consorcio(valor=100000, taxa_admin=10, prazo=24, reajuste_anual=5)
    primeira = parcelas[0]
    parcela_13 = parcelas[12]  # início do segundo ano

    esperado = round(primeira * 1.05, 2)
    resultado = round(parcela_13, 2)

    assert pytest.approx(resultado, 0.01) == esperado

def test_calculo_financiamento_juros_compostos():
    parcela, total = calcular_financiamento(valor=100000, juros_mensal=1, prazo=12)

    # A parcela deve ser maior que 1/12 do valor (pois há juros)
    assert parcela > (100000 / 12)

    # O total pago deve ser maior que o valor solicitado
    assert total > 100000


def test_total_consorcio_deve_ser_menor_que_financiamento():
    _, total_cons = calcular_consorcio(valor=100000, taxa_admin=10, prazo=80)
    _, total_fin = calcular_financiamento(valor=100000, juros_mensal=1.2, prazo=60)

    # Com juros altos, o consórcio deve ser mais barato
    assert total_cons < total_fin


