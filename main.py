import os
from fastapi import FastAPI, HTTPException
import requests
from dotenv import load_dotenv
import google.generativeai as genai

#Carrega as variáveis do arquivo .env
load_dotenv()

#Configura a chave do Gemini
gemini_key = os.getenv("GEMINI_API_KEY")

if gemini_key:
    genai.configure(api_key=gemini_key)

#Inicialização da aplicação FastAPI
app = FastAPI(
    title="API de Cotações com IA",
    description="Servidor back-end para consulta de moedas em tempo real e análise de mercado com Gemini.",
    version="1.0.0",
)

#ROTAS 

#Página inicial
@app.get("/")
def home():
    return {
        "status": "online",
        "mensagem": "API de Cotações rodando com sucesso! Acesse /docs para testar as rotas.",
    }

#Consulta simples de moeda
@app.get("/cotacao/{moeda}")
def busca_cotacao_moeda(moeda: str):
    moeda_limpa = moeda.strip().upper()

    if moeda_limpa == "EURO":
        moeda_limpa = "EUR"

    url = f"https://economia.awesomeapi.com.br/last/{moeda_limpa}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        chave = f"{moeda_limpa}BRL"
        dados = resposta.json()[chave]

        return {
            "sucesso": True,
            "moeda": dados["name"],
            "codigo": moeda_limpa,
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
            detail=f"A moeda '{moeda_limpa}' não foi encontrada ou não é suportada.",
        )

#Análise inteligente com Gemini
@app.get("/cotacao/{moeda}/analise-ia")
def analise_ia(moeda: str):
    if not gemini_key:
        raise HTTPException(
            status_code=500,
            detail="Chave do Gemini não configurada no servidor.",
        )
        
    dados_cotacao = busca_cotacao_moeda(moeda)

    prompt = f"""
    Atue como um analista financeiro sênior.
    Analise os seguintes dados em tempo real da moeda {dados_cotacao['moeda']} ({dados_cotacao['codigo']}):
    - Valor Atual (compra): R$ {dados_cotacao['valor_compra']}
    - Máxima do dia: R$ {dados_cotacao['valor_maximo_dia']}
    - Mínima do dia: R$ {dados_cotacao['valor_minimo_dia']}

    Forneça um resumo dinâmico, direto e claro em português (máximo de 3 parágrafos) explicando o que esses números representam no mercado hoje e um conselho simplificado para investidores ou pessoas comuns.
    """

    try:
        model = genai.GenerativeModel('models/gemini-3.5-flash')
        response = model.generate_content(prompt)

        return {
            "dados_financeiros": dados_cotacao,
            "analise_ia": response.text,
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao gerar análise com IA: {str(e)}",
        )
