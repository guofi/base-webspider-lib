import requests

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            print(response.text)
            return response.text
    except ConnectionError:
        return None


'''
94.142.142.140:3128
'''
if __name__ == '__main__':
    get_proxy()
