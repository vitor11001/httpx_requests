from send_data import send_data
from send_timeack import send_timeack
from get_token import get_token

def main():
    print('Obtendo token...')
    access_token = get_token()
    macs = [
        '00:1A:2B:3C:4D:5E',
        '00:1A:2B:3C:4D:60'
    ]
    for mac in macs:
        for _ in range(4):
            print('Enviando timeack...')
            send_timeack(access_token, mac)
            print('Enviando dados...')
            send_data(access_token, mac)

main()