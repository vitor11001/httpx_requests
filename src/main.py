from send_data import send_data
from send_timeack import send_timeack
from get_token import get_token

def main():
    print('Obtendo token...')
    access_token = get_token()
    print('Enviando timeack...')
    send_timeack(access_token)
    print('Enviando dados...')
    send_data(access_token)

main()