Teste de API - Tailscale OAuth Token
Este documento descreve como foi realizado o teste de autenticação com a API do Tailscale utilizando o fluxo client_credentials para obter um token de acesso.

Objetivo
O objetivo deste teste é verificar a autenticação com a API do Tailscale por meio do envio de uma requisição POST ao endpoint de geração de token OAuth 2.0.


Explicação
Endpoint: Utilizamos o endpoint https://api.tailscale.com/api/v2/oauth/token para autenticação via OAuth.

Método: POST

Dados enviados (payload):

client_id: ID do cliente registrado no Tailscale.

client_secret: Chave secreta do cliente.

grant_type: Definido como client_credentials para esse tipo de autenticação.

Resposta esperada: Um JSON contendo o access_token se a autenticação for bem-sucedida.


