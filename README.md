#cotação IA - API Rest de Cotações de Moedas em Tempo Real

Aplicação Back-End desenvolvida em Python com FastAPI para consulta e tratamento de dados de moedas dinâmicas via REST API.

##Funcionalidades
- **Endpoint GET `/`**: Status do servidor e verificação de saúde da aplicação.
- **Endpoint GET `/cotacao/{moeda}`**: Retorna valores atualizados de compra, máxima, mínima e data de atualização de qualquer moeda (ex: USD, EUR, BTC) formatados em JSON.
- **Documentação Automática**: Interface Swagger UI interativa integrada.
- **Tratamento de Erros HTTP**: Respostas com códigos de status adequados (`404` para moeda não encontrada, `500` para falhas de conexão).

##Tecnologias Utilizadas
- **Python 3.13**
- **FastAPI**: Framework web moderno e de alto desempenho.
- **Uvicorn**: Servidor ASGI para execução da API.
- **Requests**: Consumo de serviço externo HTTP (AwesomeAPI).

##Como executar a aplicação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/cotacao-ia.git](https://github.com/SEU_USUARIO/cotacao-ia.git)
