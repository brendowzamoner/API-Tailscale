import requests

# URL do endpoint
url = "https://api.tailscale.com/api/v2/oauth/token"

# Dados da autenticação
payload = {
    "client_id": "kZpLyZBA5811CNTRL",
    "client_secret": "tskey-client-kZpLyZBA5811CNTRL-3sWY8a3dH2dPXXV2cHqG2din1PBT7zL5A",
    "grant_type": "client_credentials"
}

# Enviando a requisição POST
response = requests.post(url, data=payload)

# Verificando a resposta
if response.status_code == 200:
    data = response.json()
    print("Token de acesso:", data["access_token"])
else:
    print("Erro:", response.status_code)
    print(response.text)
