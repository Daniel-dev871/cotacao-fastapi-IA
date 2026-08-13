# API de Cotações em Tempo Real com Análise Inteligente (Gemini AI)

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Gemini AI](https://img.shields.io/badge/Google%20Gemini-3.5%20Flash-8E75B2?style=for-the-badge&logo=googlecloud&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI-499848?style=for-the-badge&logo=uvicorn&logoColor=white)

API RESTful desenvolvida em FastAPI para consulta de dados do mercado financeiro em tempo real e geração de análises técnicas e conselhos práticos através do modelo de linguagem Google Gemini (3.5 Flash).

---

## Funcionalidades

- **Cotação em Tempo Real:** Consulta de taxas de câmbio (Dólar, Euro, etc.) via AwesomeAPI.
- **Análise Financeira via IA:** Prompts estruturados para o Gemini atuar como um analista financeiro sênior.
- **Documentação Interativa:** Interface Swagger UI integrada e pronta para testes no endpoint `/docs`.
- **Execução Assíncrona:** Alta performance e baixo tempo de resposta com Uvicorn e FastAPI.

---

## Arquitetura e Tecnologias

- **Linguagem:** Python 3.13+
- **Framework Web:** FastAPI
- **Servidor ASGI:** Uvicorn
- **Modelos de IA:** `google-generativeai` (Gemini 3.5 Flash)
- **Cliente HTTP:** Requests
- **Gerenciamento de Ambiente:** `python-dotenv`

---

## Instalação e Execução

### Pré-requisitos
- Python 3.10 ou superior
- Chave de API ativa no Google AI Studio

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
   cd NOME-DO-REPOSITORIO

   Criar e ativar o ambiente virtual:Bash# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate

Instalar as dependências:
Bash
pip install -r requirements.txt
Configurar variáveis de ambiente:
Crie um arquivo .env na raiz do projeto:
Snippet de códigoGEMINI_API_KEY=sua_chave_aqui

Iniciar o servidor:
Bash
python -m uvicorn main:app --reload
Acessar a documentação:Navegue até http://127.0.0.1:8000/docs para testar os endpoints interativamente.Endpoints da AplicaçãoMétodoRotaDescriçãoGET/Status da API e mensagem de confirmação do servidorGET/cotacao/{moeda}Retorna os dados atualizados da moeda especificada (ex: USD, EUR)GET/cotacao/{moeda}/analise-iaRetorna os dados financeiros combinados com a análise da IAExemplo de Resposta (/cotacao/usd/analise-ia)JSON{
  "dados_financeiros": {
    "sucesso": true,
    "moeda": "Dólar Americano/Real Brasileiro",
    "codigo": "USD",
    "valor_compra": 5.1899,
    "valor_maximo_dia": 5.2284,
    "valor_minimo_dia": 5.17129,
    "data_atualizacao": "2026-08-13 15:00:08"
  },
  "analise_ia": "O mercado cambial hoje apresenta uma volatilidade expressiva..."
}
Autor
Desenvolvido por Daniel Duarte
LinkedIn:(https://www.linkedin.com/in/daniel-duarte-020625306/)
GitHub:Daniel-dev871
