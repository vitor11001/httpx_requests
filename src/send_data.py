import httpx

def send_data(token_access: str):

    # Definir a URL
    url = 'http://127.0.0.1:8000/device_communication/connection_data'

    payload = {
        'mac': '00:1A:2B:3C:4D:5E'.lower(),
        'pt100': 50.2,
        'battery': 4.2,
        'rssi': 37,
    }
    topic = 'senfio/qs/+/connection/data'
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
