import requests


class Singer:
    def __init__(self, name):
        self.name = name

    def musics(self):
        try:
            url = 'http://api.codebazan.ir/music'
            params = {
                'type': 'search',
                'query': self.name,
                'page': 1
            }
            response = requests.get(url=url, params=params)
            musics = response.json().get('Result')
            return musics
        except Exception as e:
            return f'Exception : {e}'

