import json
import requests


def buscar_cotacao():


    moeda = input("Digite a moeda(USD, BRL, EURO, BTc)"
            ).upper().strip()
    if moeda == "EURO":
        moeda = "EUR";
    
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        chave_moeda = f"{moeda}BRL"
        dados= resposta.json()[f"{moeda}BRL"]
        
        relatorio = {
            "moeda": f" ({moeda}/BRL)",
            "valor_compra":float(dados["bid"]),
            "valor_maximo_dia": float(dados["high"]),
            "valor_minimo_dia":float(dados["low"]),
            "data atualizacao": dados["create_date"],
        }
        with open("relatorio_cotacao.json", "w", encoding="utf-8") as arquivo:
            json.dump(relatorio, arquivo, indent=4, ensure_ascii=False)

        print("✅ Dados obtidos e 'relatorio_cotacao.json' gerado com sucesso!\n")
        print(json.dumps(relatorio, indent=4, ensure_ascii=False))

    except requests.exceptions.RequestException as erro:
        print(f"Erro ao conectar à API: {erro}")
    except KeyError:
        print(
            f"A moeda '{moeda}' não foi encontrada ou o formato da resposta é inválido."
        )
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")


if __name__ == "__main__":
    buscar_cotacao()
