import httpx
from faker import Faker

fake = Faker()

def send_data(token_access: str, mac: str):

    # Definir a URL
    url = 'http://127.0.0.1:8000/device_communication/connection_data'

    payload = {
        'mac': mac.lower(),
        'pt100': fake.pyfloat(left_digits=2, right_digits=2),
        'battery': fake.pyfloat(left_digits=1, right_digits=1, positive=True),
        'rssi': fake.pyint(min_value=-100, max_value=-30),
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
