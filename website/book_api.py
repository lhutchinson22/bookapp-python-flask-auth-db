import requests

def search_books(query):
    response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}')
    if response.status_code == 200:
        return response.json().get('items', [])
    return []
