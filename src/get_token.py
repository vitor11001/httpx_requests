import httpx

def get_token():

    # Definir a URL
    url = 'http://0.0.0.0:8000/api/token/'

    data = {'email': 'jose.leao@senfio.com', 'password': 'admin'}

    # Definir cabeçalhos
    headers = {'Content-Type': 'application/json'}

    # Enviar a requisição POST
    response = httpx.post(url, json=data, headers=headers)

    print(response.status_code)
    print(response.json())
    response_access_token = response.json()['access']
    print(response_access_token)
    return response_access_token
