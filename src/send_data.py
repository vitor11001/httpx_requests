import httpx
from faker import Faker
from datetime import datetime

fake = Faker()


def send_data(token_access: str, mac: str):

    # Definir a URL
    url = 'http://127.0.0.1:8000/device_communication/connection_data'

    payload = {
        'MAC': mac.lower(),
        "data": datetime.now().strftime('%d/%m/%y %H:%M:%S'),
        'pt100': round(fake.pyfloat(left_digits=0, right_digits=2, positive=True) * 0.5, 2),
        'bateria': fake.pyfloat(left_digits=1, right_digits=1, positive=True),
        'rssi': fake.pyint(min_value=-100, max_value=-30),
    }
    topic = 'senfio/qs/+/connection/data'
    topic_wildcard = payload['MAC'].replace(':', '')

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
