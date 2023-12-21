import json
import math

def calcular_investimento(valor_total, dados_acoes):
    
    quantidade_acoes = len(dados_acoes["acoes"])
    valor_por_acao = valor_total / quantidade_acoes
    resultados_acoes = {}
    proventos_totais = 0

    for acao, info in dados_acoes["acoes"].items():
        quantidade_cotas = int(math.floor(valor_por_acao / info["valor_medio"]))
        valor_aporte = quantidade_cotas * info["valor_medio"]
        proventos = quantidade_cotas * info["proventos"]
        resultados_acoes[acao] = {
            'preco_medio': info["valor_medio"],
            'quantidade_cotas': quantidade_cotas,
            'valor_aporte': valor_aporte,
            'valor_total_gasto': valor_total,
            'proventos': proventos
        }
        proventos_totais += proventos

    resultados_acoes['proventos_totais'] = proventos_totais
    return resultados_acoes

if __name__ == "__main__":
    
    with open("acoes.json", "r") as file:
        dados_acoes = json.load(file)

    valor_total = float(input("Digite o valor total a ser investido em reais: "))

    resultados = calcular_investimento(valor_total, dados_acoes)
    print("\nResultados:")
    for acao, info in resultados.items():
        if acao == 'proventos_totais':
            continue
        print(f"\nAção: {acao}")
        print(f"Preço Médio: R${info['preco_medio']:.2f}")
        print(f"Quantidade de Cotas: {info['quantidade_cotas']}")
        print(f"Valor do Aporte: R${info['valor_aporte']:.2f}")
        print(f"Valor Total Gasto: R${info['valor_total_gasto']:.2f}")
        print(f"Proventos: R${info['proventos']:.2f}")

    print(f"\nProventos Totais: R${resultados['proventos_totais']:.2f}")
