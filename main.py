#fastapi: Framework web para criar rotas e gerenciar requisições
from fastapi import FastAPI, HTTPException

#biblioteca HTTP para consumir APIs esternas
import requests


# inicialização da aplicação
app = FastAPI(
    title="API de cotações com IA",
    description="servidor back-end para consulta de moedas em tempo real",
    version="1.0.0",
)

#Rota 1: pagina inicial
@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "API de Cotações rodando com sucesso! Acesse /docs para testar as rotas.",
    }
# consulta de moeda dinamica(get /cotacao/{moeda})

@app.get("/cotacao/{moeda}")
def busca_cotacao_moeda(moeda:str):
    moeda_limpa = moeda.strip().upper()

    if moeda_limpa == "EURO":
        moeda_limpa = "EUR"

    url = f"https://economia.awesomeapi.com.br/last/{moeda_limpa}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        chave = f"{moeda_limpa}BRL"
        dados = resposta.json()[chave]

        return{
            "sucesso": True,
            "moeda": dados["name"],
            "codigo":  moeda_limpa,
            "valor_compra": float(dados["bid"]),
            "valor_maximo_dia": float(dados["high"]),
            "valor_minimo_dia": float(dados["low"]),
            "data_atualizacao": dados["create_date"],
        }
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=500,
            detail="Erro ao conectar com o serviço externo de cotações",
        )
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"A moeda '{moeda_limpa}'não foi encontrada ou não e suportada."
        )