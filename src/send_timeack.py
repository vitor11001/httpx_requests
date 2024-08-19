import httpx

def send_timeack(token_access: str, mac: str):

    # Definir a URL
    url = 'http://127.0.0.1:8000/device_communication/connection_timeack'

    payload = {
        'mac': mac.lower(),
    }
    topic = 'senfio/qs/+/connection/timeack'
    topic_wildcard = payload['mac'].replace(':', '')

    data = str({
            'topic': topic,
            'payload': str(payload),
            'topic_wildcard': topic_wildcard,
        })

    # Definir cabeçalhos
    headers = {
        'Content-Type': 'text/plain', 
        'Authorization': 'Bearer ' + token_access
    }

    # Enviar a requisição POST
    response = httpx.post(url, data=data, headers=headers)

    print(response.status_code)
    print(response.json())
